import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 1
        self.name = "Verify Vacuum Level"
        self.objects = [
            "Prerequisite: \n\n"
            "• Vacuum Pressure Gauge \n\n"
            "•  Vacuum is turned on for all spindles and all heads\n\n"
            "* Note: Vacuum for all spindles for all heads must be turned on before verifying vacuum level.\n\n"
            "To verify the vacuum level, do the following: \n\n"
            "1. Go to the Operator Interface, and log on as Administrator. \n\n"
            "2. Drop off all nozzles as follows: \n\n"
            "a. Select Tools > Setup > Head Nozzle Setup. \n\n"
            "b. Select the FZ30 Head icon. \n\n"
            "c. Select Dropoff All Nozzles. \n\n"
            "d. Select Yes at the confirmation message. Wait for the nozzles to be dropped off. \n\n"
            "e. Select OK > OK. \n\n"
            "3. Go to the Desktop, and use Manual Control to move the head for accessibility. \n\n"
            "4. Push the Emergency Stop switch to disable the interlocks, and then release the Emergency Stop switch. \n\n"
            "5. Activate vacuum to all spindles as follows: \n\n"
            "a. From the Control Panel, select the Head Subsystem Control  icon. \n\n"
            "b. Select the Spindle Data tab. \n\n"
            "c. Select Spindle All. \n\n"
            "d. Select the Vacuum ON button. \n\n"
            "e. For dual and quad beam machines, repeat these steps to activate vacuum on all spindles for each 30-spindle head. \n",
            "\img|spindle/01-01-image.png",
            "1. Open the access covers. \n\n"
            "2. Attach the vacuum gauge to the spindle. \n\n"
            "3. Verify the vacuum level is 21 in. Hg or greater. \n\n"
            "* (in. HG “Inch of mercury” 1 in.Hg= 0.491154 PSI “Pounds per square inch”) \n\n"
            "*1 PSI = 0.0689476 Bar."
            "4. Perform steps 7 and 8 for each spindle. \n\n"
            "5. Load a product to install the nozzles. \n\n"
            
        ]
    