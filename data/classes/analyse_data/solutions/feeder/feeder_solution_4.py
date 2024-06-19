import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 4
        self.name = "do the preventive maintenance"
        self.objects = [
            "For optimum performance perform the following before loading the feeder:\n\n"
            "* Check the pogo pin interface for damage.\n\n"
            "* Keep the reel holder (tail section) free of labels or adhesive thatcould interfere with the component reel/\n\n"
            "* Before loading, check the feeder for loose components or debris.\n\n"
            "* Keep the cover, tensioner, and idler free of adhesives and debris.\n\n"
            "* Empty the component collection area(s). Clean the magnets and make sure there are no components or debris present.\n",
            "\img|feeder/04-01-image.png",
            "\n\n",
            "\img|feeder/04-02-image.png",
            "\n\n",
            "\img|feeder/04-03-image.png",
            
        ]