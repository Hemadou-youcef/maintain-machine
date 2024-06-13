import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 3
        self.name = "Preparing Cover Tape"
        self.objects = [
            "* Make sure loose components do not fall into the feeder, which may cause it to jam and fail.\n\n"
            "* If the carrier tape does not have enough leader to load into the exit chute, the front of the carrier tape must be cut into a point. Load the tape so that the leading edge is at least past the tape sprocket.\n",
            "\img|feeder/03-image.png",
        ]
        