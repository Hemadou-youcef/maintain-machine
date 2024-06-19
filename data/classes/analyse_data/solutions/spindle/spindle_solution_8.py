import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 8
        self.name = "Do the maintenance preventive for the Spindle:"
        self.objects = [
            "1- Clean: Spindle Shaft, valve GP, Guided Cap Assembly, Upper Housing Assembly, Spindle Assembly Venturi, Lower Housing Assembly.\n",
            "\img|spindle/08-image.png",
            "2- lubricate the valve joints GP grease OZ G.450 Ref: 40833825.\n\n",
            "3- Reassemble the spindle +Teste OFFLINE using SPINDLE TESTER.\n\n",
        ]
    