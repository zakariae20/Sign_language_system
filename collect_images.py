import os
import cv2

#Set up a directory to save collected images for different classes.
COLLECTION_DIRECTORY = './Our_Data'  # Define the directory to store collected images.
if not os.path.exists(COLLECTION_DIRECTORY):
    os.makedirs(COLLECTION_DIRECTORY)  # Create the directory if it doesn't exist.

#Define parameters for the data collection process.
TOTAL_CLASSES = 1  # Number of classes for which images will be collected.
IMAGES_PER_CLASS = 100  # Number of images to capture for each class.
CAMERA_PORT = 0  # Camera port to use for video capture.

#Set up the video capture using the specified camera port.
video_capture = cv2.VideoCapture(CAMERA_PORT)  # Initialize video capture.

# Check if the camera was successfully accessed.
if not video_capture.isOpened():
    print(f"Error: Unable to access camera at port {CAMERA_PORT}")  # Display error if camera can't be accessed.
    exit()

#Loop through each class and capture the specified number of images.
for class_num in range(TOTAL_CLASSES):
    # Create a folder for each class if it doesn't already exist.
    class_folder = os.path.join(COLLECTION_DIRECTORY, str(class_num))
    if not os.path.exists(class_folder):
        os.makedirs(class_folder)  # Create the class folder.

    print('Starting data collection for class {}'.format(class_num))  # Notify start of data collection.

    #Wait for user input to begin data collection for the current class.
    while True:
        success, frame = video_capture.read()  # Capture a frame from the camera.
        if not success:
            print("Error: Failed to capture frame from camera")  # Display error if frame capture fails.
            break

        # Display instruction text on the frame.
        cv2.putText(frame, 'Press "Q" to begin data collection for class {}'.format(class_num),
                    (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('frame', frame)  # Show the frame in a window.

        # Wait for the user to press 'Q' to start collecting images.
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break  # Exit the loop when 'Q' is pressed.

    #Capture and save the specified number of images for the current class.
    image_count = 0  # Initialize the image count.
    while image_count < IMAGES_PER_CLASS:
        success, frame = video_capture.read()  # Capture a frame from the camera.
        if not success:
            print("Error: Failed to capture frame from camera")  # Display error if frame capture fails.
            break

        cv2.imshow('frame', frame)  # Show the captured frame.
        cv2.waitKey(25)  # Wait for 25ms before capturing the next frame.

        # Save the captured frame as an image file in the class folder.
        frame_path = os.path.join(class_folder, '{}.jpg'.format(image_count))
        cv2.imwrite(frame_path, frame)  # Write the frame to a file.

        image_count += 1  # Increment the image count.

#Release the video capture object and close all OpenCV windows.
video_capture.release()  # Release the video capture object.
cv2.destroyAllWindows()  # Close all OpenCV windows.
