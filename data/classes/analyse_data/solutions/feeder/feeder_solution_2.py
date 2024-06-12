import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.name = "Component Clean-Out"
        self.text = [
            "* There are two screws located as shown on the feeder. These screws contain magnets that collect components that have fallen inside the unit. For optimum feeder function, remove these screws periodically and clear any accumulated components.",
            "* When replacing the screws, screw them down until they bottom out mechanically. Do not force them beyond snug (approximately 0.4 Nm torque).",
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
        first_image_file = img.ImageClass("feeder/02-01-image.png").create_image(500,300)
        second_image_file = img.ImageClass("feeder/02-02-image.png").create_image(500,300)
        third_image_file = img.ImageClass("feeder/02-03-image.png").create_image(500,300)
        
        first_image = customtkinter.CTkLabel(master=master, image=first_image_file,text="")
        second_image = customtkinter.CTkLabel(master=master, image=second_image_file,text="")
        third_image = customtkinter.CTkLabel(master=master, image=third_image_file,text="")
        
        
        # pack the widgets
        
        first_image.pack()
        second_image.pack()
        third_image.pack()
        
        return [solution_name, solution_line, first_image,second_image,third_image]
        
        
    