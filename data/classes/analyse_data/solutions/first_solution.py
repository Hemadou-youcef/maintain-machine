import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.name = "THIS IS SOLUTION"
        self.id = 1

    def content(self,master):
        
        # create a label to display the solution name
        solution_name = customtkinter.CTkLabel(master, text=self.name)
        # create a label to display the solution description
        solution_description = customtkinter.CTkLabel(master, text="This is a solution description")
        # create a label to display the solution image
        first_image_file = img.ImageClass("image1.png").create_image(500,300)
        first_image = customtkinter.CTkLabel(master=master, image=first_image_file,text="")
        
        # pack the widgets
        solution_name.pack()
        solution_description.pack()
        first_image.pack()
        
        return [solution_name, solution_description, first_image]
        