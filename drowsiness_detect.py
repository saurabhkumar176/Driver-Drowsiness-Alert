import cv2
import numpy as np
import mediapipe as mp
from playsound import playsound

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1)

def eye_aspect_ratio(eye):    
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    
    print(f"A: {A}, B: {B}, C: {C}")  # Debug output
    ear = (A + B) / (2.0 * C)
    print(f"EAR: {ear}")  # Debug output
    return ear

left_eye_indices = [33, 160, 158, 157, 154, 153]
right_eye_indices = [362, 384, 381, 359, 386, 387]

cap = cv2.VideoCapture(0)
alert_played = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            left_eye = np.array([[landmarks.landmark[i].x * frame.shape[1],
                                   landmarks.landmark[i].y * frame.shape[0]] for i in left_eye_indices])
            right_eye = np.array([[landmarks.landmark[i].x * frame.shape[1],
                                    landmarks.landmark[i].y * frame.shape[0]] for i in right_eye_indices])

            print("Left Eye Landmarks Coordinates:", left_eye)
            print("Right Eye Landmarks Coordinates:", right_eye)

            left_ear = eye_aspect_ratio(left_eye)
            right_ear = eye_aspect_ratio(right_eye)
            ear = (left_ear + right_ear) / 2.0

            print(f"Left EAR: {left_ear}, Right EAR: {right_ear}, Average EAR: {ear}")  # Debug output

            if left_ear < 0.50 and right_ear < 0.50:  # Check both ears
                cv2.putText(frame, "Drowsy!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                if not alert_played:
                    playsound(r"C:\Users\saur1\OneDrive\Desktop\Drowsy_project\Drowsy_project\alert2.mp3", block=True)
                    alert_played = True
            else:
                alert_played = False

            # Visualize left and right eye landmarks
            for idx, i in enumerate(left_eye_indices):
                cv2.circle(frame, (int(left_eye[idx][0]), int(left_eye[idx][1])), 3, (255, 0, 0), -1)
            for idx, i in enumerate(right_eye_indices):
                cv2.circle(frame, (int(right_eye[idx][0]), int(right_eye[idx][1])), 3, (255, 0, 0), -1)

    cv2.imshow('Drowsiness Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
