import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.name = "do the preventive maintenance"
        self.text = [
            "For optimum performance perform the following before loading the feeder:",
            "* Check the pogo pin interface for damage.",
            "* Keep the reel holder (tail section) free of labels or adhesive thatcould interfere with the component reel/",
            "* Before loading, check the feeder for loose components or debris.",
            "* Keep the cover, tensioner, and idler free of adhesives and debris.",
            "* Empty the component collection area(s). Clean the magnets and make sure there are no components or debris present."
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
        first_image_file = img.ImageClass("feeder/04-01-image.png").create_image(500,300)
        second_image_file = img.ImageClass("feeder/04-02-image.png").create_image(500,300)
        third_image_file = img.ImageClass("feeder/04-03-image.png").create_image(500,300)
        
        first_image = customtkinter.CTkLabel(master=master, image=first_image_file,text="")
        second_image = customtkinter.CTkLabel(master=master, image=second_image_file,text="")
        third_image = customtkinter.CTkLabel(master=master, image=third_image_file,text="")
        
        # pack the widgets
        first_image.pack()
        
        return [solution_name, solution_line, first_image,second_image,third_image]
        
        
    