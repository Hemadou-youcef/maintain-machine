import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.name = "Preparing Cover Tape"
        self.text = [
            "* Make sure loose components do not fall into the feeder, which may cause it to jam and fail.",
            "* If the carrier tape does not have enough leader to load into the exit chute, the front of the carrier tape must be cut into a point. Load the tape so that the leading edge is at least past the tape sprocket."
        ]
        self.id = 1

    def content(self,master):
        
        # create a label to display the solution name
        solution_name = customtkinter.CTkLabel(master, text=f"{self.name}\n\n",font=("ariel", 23))
        solution_name.pack()
        # create a label to display the solution description
        solution_line = customtkinter.CTkLabel(master, text=f"{"\n\n".join(self.text)}\n\n",justify="left",wraplength=480,font=("ariel", 20))
        solution_line.pack()
            
        # create a label to display the solution image
        first_image_file = img.ImageClass("feeder/03-image.png").create_image(500,300)
        
        first_image = customtkinter.CTkLabel(master=master, image=first_image_file,text="")
        
        # pack the widgets
        first_image.pack()
        
        return [solution_name, solution_line, first_image]
        
        
    