import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.name = "Tape & Reel Handling Protocol"
        self.text = [
            "* Damaged component tapes and reels can negatively affect overall system performance.",
            "* Damaged tapes can prevent smooth movement off the reel and through the feeder. For best performance, ensure that component tapes are flat: not bent, warped or twisted.",
            "* Damaged reels can prevent smooth release of tape from the reel and prevent the reel from rotating smoothly. For best performance, ensure that all reels inside and outside surfaces are smooth: not burred, bent, dented, or twisted. Ensure that corrugated paper reels are not torn or delaminated.",
            "* always use undamaged component tapes and reels to ensure the best performance of ion Feeders, Feeder Baskets, Basket Dividers, Reel Dividers, and Reel Holders."
        ]
        self.id = 1

    def content(self,master):
        
        # create a label to display the solution name
        solution_name = customtkinter.CTkLabel(master, text=f"{self.name}\n\n",font=("ariel", 23))
        solution_name.pack()
        # create a label to display the solution description
        solution_line = customtkinter.CTkLabel(master, text=f"{"\n\n".join(self.text)}\n\n",justify="left",wraplength=480,font=("ariel", 20))
        solution_line.pack()
        
        # solution_text_labels = []
        # for line in self.text:
        #     # create label for each line of the solution and make it in the left and make it wrap as much as window size
        #     solution_line = customtkinter.CTkLabel(master, text=line,justify="left",wraplength=520,width=500)
        #     solution_line.pack()
        #     solution_text_labels.append(solution_line)
            
        # create a label to display the solution image
        first_image_file = img.ImageClass("feeder/01-image.png").create_image(500,300)
        first_image = customtkinter.CTkLabel(master=master, image=first_image_file,text="")
        
        # pack the widgets
        first_image.pack()
        
        return [solution_name, solution_line, first_image]
        
        
    