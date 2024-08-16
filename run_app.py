from pathlib import Path
import os
from tkinter import Tk, Canvas, Button, PhotoImage

# Define the paths for the output and assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Desktop\Sign_language_system\build\assets\frame1")

# Function to generate a path relative to the assets folder
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Function to open the main GUI application
def open_gui_principale():
    gui_principale = r"C:\Users\HP\Desktop\Sign_language_system\tk_app.py"
    os.system("python " + gui_principale)  # Runs the main application script

# Initialize the Tkinter window
window = Tk()

# Set the window size and background color
window.geometry("1280x720")
window.configure(bg="#FFFFFF")

# Create a canvas to hold the UI elements
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

# Create a blue rectangle on the left side of the window
canvas.create_rectangle(
    0.0,
    3.0,
    623.0,
    720.0,
    fill="#074173",
    outline="")

# Create a button using an image and place it on the canvas
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui_principale,  # Opens the main GUI when clicked
    relief="flat"
)
button_1.place(x=62.0, y=418.0, width=174.0, height=49.0)

# Add text to the canvas for the title and description of the system
canvas.create_text(
    62.0,
    141.0,
    anchor="nw",
    text="REAL-TIME SIGN LANGUAGE ",
    fill="#FFFFFF",
    font=("Poppins ExtraBold", 32 * -1)
)

canvas.create_text(
    62.0,
    188.0,
    anchor="nw",
    text="TRANSLATION SYSTEM",
    fill="#FFFFFF",
    font=("Poppins ExtraBold", 32 * -1)
)

# Add text for the description of the system
canvas.create_text(
    62.0,
    262.0,
    anchor="nw",
    text="Unlock seamless communication with our",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 24 * -1)
)

canvas.create_text(
    62.0,
    293.0,
    anchor="nw",
    text="cutting-edge sign language translator.",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 24 * -1)
)

canvas.create_text(
    62.0,
    324.0,
    anchor="nw",
    text="Experience the future of inclusive",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 24 * -1)
)

canvas.create_text(
    62.0,
    355.0,
    anchor="nw",
    text="interaction, intuitive, and powerful.",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 24 * -1)
)

# Load and display images on the right side of the canvas
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(1167.0, 35.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(953.0, 355.0, image=image_image_2)

# Prevent the window from being resized
window.resizable(False, False)

# Start the Tkinter event loop
window.mainloop()
