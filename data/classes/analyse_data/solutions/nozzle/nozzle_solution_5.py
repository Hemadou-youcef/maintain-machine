import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 5
        self.name = "Replace damage nozzles"
        self.objects = [
            "One of the most critical steps to a robust SMT process is having clean nozzles. Contaminated nozzles can lead to mis-picks, skewed placements and even missing components.\n\n"
        ]
    