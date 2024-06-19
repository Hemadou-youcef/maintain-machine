import customtkinter
from PIL import Image, ImageTk
import os

class ImageClass:
    def __init__(self, filename):
        current_path = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(current_path, f"../../assets/images/{filename}")
        
    def create_image(self,width,height=0):
        # Load the image using Pillow
        image_data = Image.open(self.filename)
        
        # Resize the image
        if height == 0:
            # resize the image with the width and keep the aspect ratio
            height = int(image_data.height * (width / image_data.width))
            resized_image = image_data.resize((width, height))
        else:
            # resize the image with the width and height
            resized_image = image_data.resize((width, height))
        
        # Convert the resized image to a format that Tkinter can use
        # self.final_image = ImageTk.PhotoImage(resized_image)  # Store the final_image as an attribute
        self.final_image = customtkinter.CTkImage(light_image=resized_image, size=(width,height))
        
        return self.final_image
