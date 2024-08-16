from pathlib import Path
from tkinter import Tk, Canvas, Label, PhotoImage
import pickle
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageTk

# Load the pre-trained Random Forest model from a pickle file
model_dict = pickle.load(open('./random_forest.p', 'rb'))
model = model_dict['model']  # Extract the model from the dictionary

# Initialize Mediapipe Hands for hand landmark detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils  # Utility for drawing hand landmarks
mp_drawing_styles = mp.solutions.drawing_styles  # Utility for drawing styles

# Initialize Mediapipe Hands with static image mode and a minimum detection confidence
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Define a dictionary to map prediction outputs to corresponding sign language characters
labels_dict = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
    11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U',
    21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: ' ', 27: 'I love you', 28: 'Hello', 29: 'Thank you'
}

# Initialize strings to store predicted text and characters
predicted_text = ""
predicted_character = ""

# Tkinter GUI setup
OUTPUT_PATH = Path(__file__).parent  # Define the output path based on the current script location
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Desktop\Sign_language_system\build\assets\frame0")  # Define the path for GUI assets

# Helper function to get the path to assets relative to the current script
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Initialize the main Tkinter window
window = Tk()
window.geometry("1280x720")  # Set the window size
window.configure(bg="#FFFFFF")  # Set the background color

# Create a canvas widget for adding images and text
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Load and display images on the GUI
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(1152.0, 60.0, image=image_image_1)

# Add title text to the canvas
canvas.create_text(
    45.0,
    50.0,
    anchor="nw",
    text="Real-Time Sign Language Translation System",
    fill="#000000",
    font=("NunitoSans", 20, "bold")
)

# Add instruction text to the canvas
canvas.create_text(
    45.0,
    666.0,
    anchor="nw",
    text="- Click On ‘Q’ To Quit                                                - Click On ‘S’ To Delete Text                                  - Click On ‘A’ To Confirm",
    fill="#000000",
    font=("NunitoSans Black", 20 * -1)
)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
canvas.create_image(1024.0, 360.0, image=image_image_2)

# Create a label to display the video feed
video_label = Label(window)
video_label.place(x=50, y=100, width=640, height=480)

window.resizable(False, False)  # Disable window resizing

# Function to update the video feed in the Tkinter window
def update_video_feed():
    global predicted_text, predicted_character

    ret, frame = cap.read()  # Capture a frame from the webcam
    if not ret:
        print("Error: Could not read frame.")
        return

    hand_coordinates = []  # Auxiliary list to store landmark coordinates
    x_values = []  # List to store x-coordinates of landmarks
    y_values = []  # List to store y-coordinates of landmarks

    H, W, _ = frame.shape  # Get the height and width of the frame
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert the frame from BGR to RGB
    results = hands.process(frame_rgb)  # Process the frame with Mediapipe Hands

    if results.multi_hand_landmarks:  # If hand landmarks are detected
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(
                frame_rgb,  # Draw on the RGB frame
                hand_landmarks,  # Model output
                mp_hands.HAND_CONNECTIONS,  # Hand connections
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_values.append(x)  # Append x-coordinates
                y_values.append(y)  # Append y-coordinates

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                hand_coordinates.append(x - min(x_values))  # Normalize x-coordinates
                hand_coordinates.append(y - min(y_values))  # Normalize y-coordinates

        # Define the bounding box for the hand
        x1 = max(0, int(min(x_values) * W) - 10)
        y1 = max(0, int(min(y_values) * H) - 10)
        x2 = min(W, int(max(x_values) * W) + 10)
        y2 = min(H, int(max(y_values) * H) + 10)

        # Make a prediction using the Random Forest model
        prediction = model.predict([np.asarray(hand_coordinates)])
        predicted_character = labels_dict[int(prediction[0])]  # Get the predicted character

        # Draw a rectangle around the hand and display the predicted character
        cv2.rectangle(frame_rgb, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv2.putText(frame_rgb, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

    # Display the predicted text string on the frame
    cv2.putText(frame_rgb, predicted_text, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3, cv2.LINE_AA)

    # Convert the frame to ImageTk format and update the label
    img = Image.fromarray(frame_rgb)  # Convert RGB frame to Image
    imgtk = ImageTk.PhotoImage(image=img)  # Convert Image to ImageTk
    video_label.imgtk = imgtk  # Update label with the new frame
    video_label.configure(image=imgtk)

    # Schedule the next update after 10 milliseconds
    window.after(10, update_video_feed)

# Function to handle key press events
def on_key_press(event):
    global predicted_text, predicted_character

    if event.char == 'a':  # Press 'a' to add the predicted letter to the text
        predicted_text += predicted_character
    elif event.char == 's':  # Press 's' to delete the entire predicted text
        predicted_text = ""
    elif event.char == 'q':  # Press 'q' to quit the application
        window.quit()

# Bind key press events to the Tkinter window
window.bind('<KeyPress>', on_key_press)

# Initialize video capture from the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video capture.")
else:
    update_video_feed()  # Start the video feed

# Run the Tkinter main loop
window.mainloop()

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
