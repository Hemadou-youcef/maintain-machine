import tkinter as tk
from PIL import Image, ImageTk

# Function to load the image and create the button
def create_button_with_image_and_multiline_text(root, image_path, button_text):
    # Load the image using Pillow
    image = Image.open(image_path)
    
    # Resize the image to 100x100 pixels
    resized_image = image.resize((100, 100), Image.LANCZOS)
    
    # Convert the resized image to a format that Tkinter can use
    photo = ImageTk.PhotoImage(resized_image)
    
    # Create the button with both image and text
    button = tk.Button(root, text=button_text, image=photo, compound='top')
    button.image = photo  # Keep a reference to avoid garbage collection
    button.pack(pady=20)

root = tk.Tk()
root.title("Button with Image and Multi-line Text Example")
root.geometry("300x300")

# Path to your image
image_path = "images\logo.png"  # Replace with your image path
button_text = "Click Me\nThis is a multi-line\nbutton text"

# Create the button
create_button_with_image_and_multiline_text(root, image_path, button_text)

root.mainloop()
