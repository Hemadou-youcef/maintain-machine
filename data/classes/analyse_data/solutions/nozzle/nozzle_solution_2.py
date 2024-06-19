import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 2
        self.name = "Drop off nozzle"
        self.objects = [
            "Drop off nozzles using head changer setup. Do not manually remove nozzles from head:\n\n"
            "Drop off all nozzles as follows: \n\n"
            "a. Select Tools > Setup > Head Nozzle Setup. \n\n"
            "b. Select the FZ30 Head icon. \n\n"
            "c. Select Dropoff All Nozzles. \n\n"
            "d. Select Yes at the confirmation message. Wait for the nozzles to be dropped off. \n\n"
            "e.	Select OK > OK. \n\n"
            "* Verify manually and visual if there is a damaged nozzle\n",
            "\img|nozzle/02-image.png",
        ]
    