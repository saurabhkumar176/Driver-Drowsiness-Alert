# Driver-Drowsiness-Alert

## 🚀 Overview
The **Drowsiness Detection System** is a real-time application designed to detect driver fatigue and prevent accidents. Using **computer vision and machine learning**, this system continuously monitors eye movements and triggers an alert if drowsiness is detected.

## 📌 Features
- **Real-time Eye Tracking**: Uses **MediaPipe Face Mesh** to detect facial landmarks.
- **Eye Aspect Ratio (EAR) Calculation**: Measures eye openness to determine drowsiness.
- **Audio Alert System**: Triggers an alarm when the EAR value falls below a threshold.
- **Live Video Feed**: Processes video from a webcam for real-time analysis.

## 🛠️ Technologies Used
- **Python** 🐍
- **OpenCV** (for image processing)
- **MediaPipe** (for face landmark detection)
- **NumPy** (for numerical calculations)
- **playsound** (for alert sound playback)

## 📂 Project Structure
```
Drowsiness-Detection-System/
│── main.py                 # Main script for running the detection
│── requirements.txt        # List of dependencies
│── alert2.mp3              # Audio alert file
└── README.md               # Project documentation
```

## 🔧 Installation & Setup
### Prerequisites
Ensure you have **Python 3.x** installed. Then, install the required dependencies:
```sh
pip install opencv-python mediapipe numpy playsound
```

### Running the Project
Run the following command to start the detection system:
```sh
python main.py
```
Press **'q'** to exit the application.

## 🚀 How It Works
1. **Captures Video Input** from the webcam.
2. **Detects Facial Landmarks** using MediaPipe.
3. **Computes EAR (Eye Aspect Ratio)** to analyze eye openness.
4. **Triggers an Alarm** if EAR falls below the drowsiness threshold.

## 💡 Future Improvements
- Enhance accuracy using **deep learning**.
- Implement **mobile compatibility**.
- Add **head pose estimation** for better fatigue analysis.

## 📜 License
This project is **open-source** and available under the MIT License.

---
**📬 Connect with Me**  
[LinkedIn](https://www.linkedin.com/in/saurabh-kumar-121b04342) | [GitHub](https://github.com/your-github-username)

