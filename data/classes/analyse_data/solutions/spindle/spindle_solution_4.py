import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 4
        self.name = "Remove/Replace a Spindle Assembly"
        self.objects = [
            "1. Move the beams for access to the head \n\n"
            "2. Purge parts from Spindles. \n\n"
            "3. Power down machine. \n\n"
            "*Warning: The machine must be powered down and your site's Lockout/Tagout procedure executed during this procedure to ensure personal safety. \n\n"
            "*CAUTION:  Do not remove Spindle Assembly with power on Spindle Interface Board as this might cause damage to Spindle Board and/or Spindle Interface Board. \n\n"
            "4. Turn the pneumatic input valve clockwise to turn off air to the machine. The Air Input Assembly is located on the lower left side of the machine. \n\n"
            "5. Open access covers. \n\n"
            "6. Remove 3 screws to remove the lower cover, if present, from the 30-spindle head. \n",
            "\img|spindle/04-image.png",
            "7. Manually rotate Phi axis for access to the faulty Spindle. Faulty Spindle should be located at the 4 o'clock position. \n\n"
            "8. For best access to the Spindle retaining screws, rotate the spindle to the orientation shown below. \n",
            "9. Loosen 2 retaining screws on Spindle Assembly using the 2mm hex driver from tool kit. \n\n"
            "10. Remove Spindle Assembly. \n\n"
            "11. Loosen 2 retaining screws on Spindle Assembly using the 2mm hex driver from tool kit. \n\n"
            "12. Remove Spindle Assembly. \n\n"
        ]
    