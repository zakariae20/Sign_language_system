# Real-Time Sign Language Translation System

<img src="https://github.com/user-attachments/assets/159035cf-63b9-4c68-b921-7b4e4846b426" alt="welcome" width="400"/>

## Overview

<img src="https://github.com/user-attachments/assets/ccb13216-a726-4d27-97c0-029a288f42f2" alt="sign_language" width="400"/>

In virtual environments, communication barriers exist for individuals who rely on sign language, limiting their ability to interact effectively with others who do not understand sign language. Our solution is a real-time sign language translation system that leverages machine learning and computer vision technologies to bridge this communication gap.

This system recognizes sign language gestures and translates them into spoken or written language in real-time, enhancing accessibility and enabling inclusive communication within the metaverse. Users who rely on sign language can now fully engage and participate in virtual interactions.

## Project Path
<img src="https://github.com/user-attachments/assets/4f812fcc-c683-4ef7-913b-bfdbc0a70799" alt="project_path" width="500"/>



### 1. **Image Collection**
- **Description**: Capturing frames from real-time video using a camera ensures that the dataset is tailored to the specific requirements of our system.
- **Process**:
  - Set up a camera and environment with good lighting and a plain background.
  - Record videos of sign language gestures.
  - Extract frames using video processing tools like OpenCV.

### 2. **Dataset Creation and Annotation**
- **Description**: Using MediaPipe for hand detection and tracking, we extract hand landmarks from images and store them with corresponding labels representing the sign.
- **Process**:
  - Initialize MediaPipe Hands Module.
  - Load and prepare data.
  - Extract hand landmarks and store data and labels.
  - Save the dataset for model training.

### 3. **Model Training and Evaluation**
- **Description**: Train a RandomForestClassifier model on the extracted hand landmarks to recognize sign language gestures.
- **Process**:
  - Load the preprocessed dataset.
  - Split the dataset into training and testing sets.
  - Train and evaluate the model.
  - Save the trained model for real-time predictions.

### 4. **Real-Time Gesture Recognition**
- **Description**: Set up a real-time gesture recognition system using a webcam feed and a pre-trained model to classify hand gestures.
- **Process**:
  - Import necessary libraries (pickle, OpenCV, MediaPipe, numpy).
  - Load the pre-trained model and initialize MediaPipe Hands.
  - Capture real-time video and process it to detect hand landmarks.
  - Predict and display gestures on the video feed.

### 5. **GUI Integration**
- **Description**: Integrate the real-time gesture translation system with a GUI using Tkinter.
- **Process**:
  - Set up a Tkinter window with a canvas to display the video feed and recognized gestures.
  - Use threading for real-time video processing to keep the GUI responsive.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/repo-name.git
   cd repo-name
2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Change paths**
4. **run run_app.py file**



