import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 6
        self.name = "Spindle Replacement Calibration"
        self.objects = [
            "Description  \n\n"
            "This procedure applies to 30-Spindle heads only. \n\n"
            "Spindle Replacement Calibration calibrates a spindle after it has been replaced. The calibration process identifies the location of the center of rotation for one spindle. The center of rotation is the basis for the mathematical pick and place model and is unique for every spindle assembly. \n\n"
            "Procedures  \n\n"
            "To perform spindle replacement calibration, do the following: \n\n"
            "1. From the Control Panel, select the Machine Setup icon  The Setup Task invoker dialog box displays. \n\n"
            "2. Select Spindle Replacement Calibration > Invoke. \n\n"
            "3. Select the desired head location. \n\n"
            "4. Select the desired spindle to calibrate. \n\n"
            "5. Select Activate. The Platform machine zeros the axes. \n\n"
            "6. Push START to begin the process. \n\n"
            "7. Calibration processing begins. When completed successfully, the calibration nozzle is placed back in the changer. \n\n"
        ]
    