import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 2
        self.name = "Verify Airkiss Pressure"
        self.objects = [
            "Required Tools : \n\n"
            "• Vacuum Pressure Gauge \n\n"
            "To verify the airkiss pressure, do the following: \n\n"
            "1. Go to the Operator Interface, and log on as Administrator. \n\n"
            "2. Drop off all nozzles as follows: \n\n"
            "a. Select Tools > Setup > Head Nozzle Setup. \n\n"
            "b. Select the FZ30 Head icon. \n\n"
            "c. Select Dropoff All Nozzles. \n\n"
            "d. Select Yes at the confirmation message. Wait for the nozzles to be dropped off. \n\n"
            "e. Select OK > OK. \n\n"
            "3. Activate airkiss to all spindles as follows: \n\n"
            "a. From the Control Panel, select the Head Subsystem Control  icon. \n\n"
            "b. Select the Spindle Data tab. \n\n"
            "c. Select Spindle All. \n\n"
            "d. Select the Airkiss ON button. \n",
            "\img|spindle/02-01-image.png",
            "1. Attach vacuum gauge to spindle. \n\n"
            "2. Verify the airkiss pressure level is between 3 to 6.5 psi. \n\n"
            "3. Perform steps 5 and 6 for each spindle. \n\n"
            "4. Load a product to install nozzles. \n\n"
            "5. Repeat procedure for each 30-spindle head. \n\n"
        ]
    