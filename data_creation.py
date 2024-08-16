import os
import pickle
import mediapipe as mp
import cv2

# Initialize MediaPipe Hands system and drawing utilities.
mp_hands_system = mp.solutions.hands
mp_drawing_utils = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Create a hand detection model with specified parameters.
hand_detection_model = mp_hands_system.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Define the path where the image data is stored.
DATA_PATH = './Our_Data'

# Lists to store extracted features and corresponding labels.
extracted_features = []
category_labels = []

# Loop through each category directory in the data path.
for category_dir in os.listdir(DATA_PATH):
    # Loop through each image file in the current category directory.
    for img_file in os.listdir(os.path.join(DATA_PATH, category_dir)):
        hand_coordinates = []  # List to store hand coordinates for the current image.
        x_values = []  # List to store x-coordinates of hand landmarks.
        y_values = []  # List to store y-coordinates of hand landmarks.

        # Read the image from the file.
        img = cv2.imread(os.path.join(DATA_PATH, category_dir, img_file))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert the image from BGR to RGB format.

        # Perform hand detection on the RGB image.
        hand_detection_results = hand_detection_model.process(img_rgb)
        if hand_detection_results.multi_hand_landmarks:  # Check if hand landmarks are detected.
            # Loop through each detected hand's landmarks.
            for hand_landmarks in hand_detection_results.multi_hand_landmarks:
                # Loop through each landmark point in the hand.
                for point_idx in range(len(hand_landmarks.landmark)):
                    x_coord = hand_landmarks.landmark[point_idx].x  # Get the x-coordinate.
                    y_coord = hand_landmarks.landmark[point_idx].y  # Get the y-coordinate.

                    x_values.append(x_coord)  # Store x-coordinate.
                    y_values.append(y_coord)  # Store y-coordinate.

                # Normalize hand coordinates relative to the minimum x and y values.
                for point_idx in range(len(hand_landmarks.landmark)):
                    x_coord = hand_landmarks.landmark[point_idx].x
                    y_coord = hand_landmarks.landmark[point_idx].y
                    hand_coordinates.append(x_coord - min(x_values))  # Normalize x-coordinate.
                    hand_coordinates.append(y_coord - min(y_values))  # Normalize y-coordinate.
            
            extracted_features.append(hand_coordinates)  # Add the normalized hand coordinates to features list.
            category_labels.append(category_dir)  # Add the category label for this image.

# Save the extracted features and labels to a pickle file.
file = open('extracted_features_labels.pickle', 'wb')
pickle.dump({'data': extracted_features, 'labels': category_labels}, file)
file.close()
