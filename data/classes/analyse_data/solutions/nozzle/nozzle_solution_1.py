import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 1
        self.name = "Check If Nozzle is Clean"
        self.objects = [
            "One of the most critical steps to a robust SMT process is c.\n\n"
            "Contaminated nozzles can lead to mis-picks, skewed placements and even missing components.\n\n"
            "1- Verify that there is no contamination present using the Vision window.\n",
            "\img|nozzle/01-01-image.png",
            "\n\n",
            '\img|nozzle/01-02-image.png',
        ]
    