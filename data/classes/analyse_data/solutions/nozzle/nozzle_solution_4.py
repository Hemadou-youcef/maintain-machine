import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 4
        self.name = "Inspect nozzle tip"
        self.objects = [
            "Inspect nozzle tip for damage and check if the reference on the nozzle is existed. Use microscope for smaller nozzles.\n\n"
        ]
    