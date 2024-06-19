import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 6
        self.name = "All or most of the nozzles are contaminated "
        self.objects = [
            "if you see that all or most of the nozzles are contaminated so do the following instructions (do immediately preventive for all the nozzles for 04 heads of the machine).\n\n"
            "- Inspect/Clean Nozzles \n\n"
            "All nozzles used on the 30-spindle head assembly should be inspected and cleaned according to the frequency specified by the maintenance concept. If a nozzle has evidence of physical damage or wear that might affect picking and placement, it should be replaced. \n\n"
            "- Prerequisites \n\n"
            "Make sure that the following items are available before beginning the procedure: \n\n"
            "• Compressed air \n\n"
            "• Lint-free cloth \n\n"
            "• Nozzle Cleaning Wire Kit \n\n"
            "• UIC Nozzle Clean solution \n\n"
            "• Ultrasonic cleaner (optional) \n\n"
            "To inspect or clean a nozzle, use the following procedure. \n\n"
            "1- Go to the Operator Interface, and log on as Administrator. \n\n"
            "2- Drop off all nozzles as follows: \n\n"
            "a. Select Tools > Setup > Head Nozzle Setup. \n\n"
            "b. Select the FZ30 Head icon. \n\n"
            "c. Select Dropoff All Nozzles. \n\n"
            "d. Select Yes at the confirmation message. Wait for the nozzles to be dropped off. \n\n"
            "e. Select OK > OK. \n\n"
            "3- Open the access cover. \n\n"
            "4- Remove nozzles from the Nozzle Changer. \n\n"
            "5- Inspect the nozzles for damage. \n\n"
            "If physical damage or wear on a nozzle tip is evident that might affect picking and placement of components, discard the nozzle. \n\n"
            "6- Inspect the nozzles for contamination, such as solder paste buildup. If contamination is present, do the following: \n",
            "\img|nozzle/06-image.png",
            "7- To install a nozzle after inspection or cleaning, do the following: \n\n"
            "a. Install the original nozzle if acceptable. \n\n"
            "b. If the original nozzle was discarded, install a new identical nozzle. \n\n"
            "8- Repeat this procedure until all nozzles in the Nozzle Changers are inspected. \n\n"
            "9- If more than one nozzle was removed at a time, verify that the nozzle configuration is correct. \n\n"
        ]
    