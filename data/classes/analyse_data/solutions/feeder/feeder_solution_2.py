import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 2
        self.name = "Component Clean-Out"
        self.objects = [
            "* There are two screws located as shown on the feeder. These screws contain magnets that collect components that have fallen inside the unit. For optimum feeder function, remove these screws periodically and clear any accumulated components.\n\n"
            "* When replacing the screws, screw them down until they bottom out mechanically. Do not force them beyond snug (approximately 0.4 Nm torque).\n",
            "\img|feeder/06-01-image.png",
            "\n\n",
            "\img|feeder/06-02-image.png",
            "\n\n",
            "\img|feeder/06-03-image.png",
        ]
