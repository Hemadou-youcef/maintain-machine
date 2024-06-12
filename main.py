import data.classes.analyse_data.solutions.feeder.feeder_solution_1 as feeder_solution_1
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from data.classes.root.view_slider import ViewSlider

if __name__ == "__main__":
    view = ViewSlider(customtkinter.CTk(), "App", width=800, height=600)
    
    # load the first view``
    view.load_view("upload",clear=False)
    
    view.mainloop()
