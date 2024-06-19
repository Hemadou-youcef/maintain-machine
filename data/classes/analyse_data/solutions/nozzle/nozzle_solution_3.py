import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 3
        self.name = "Do preventive measures for nozzles"
        self.objects = [
            "Do preventive measures for nozzles that have clogging or contamination problems:\n\n"
            "-Wash the Nozzles\n\n"
            "1- Remove UIC nozzles from platform machine with a nozzle removal tool. \n\n"
            "2- Put the Nozzle Removal Tools on the Ultrasonic Cleaner Hanger Tools and into the Ultrasonic Cleaner as shown. \n",
            "\img|nozzle/03-01-image.png",
            "3- UIC Nozzle Clean is sold in concentrated form. Before using, make a solution of 1 part UIC Nozzle Clean and 9 parts deionized (DI) water. \n\n"
            "4- Add the UIC Nozzle Clean/DI water solution into the Ultrasonic Cleaner so that the fluid level is half way up the Nozzle Removal Tools as shown below. \n",
            "\img|nozzle/03-02-image.png",
            "5- Put the cover on the Ultrasonic Cleaner."
            "* Caution: To prevent damage to compliant nozzles, Universal Instruments recommends to not use the heating function of the Ultrasonic Cleaner.\n\n"
            "* Do not leave nozzles in cleaner for extended periods of time. Excessive exposure to the cleaning solution may affect nozzle markings. To prevent spillage, always put on the cover before operating the Ultrasonic Cleaner.\n\n"
            "6- Set the timer to the desired number of minutes. The Ultrasonic Cleaner will stop automatically when the set time ends. \n\n"
            "Estimated cleaning time is 3-15 minutes in Ultrasonic Cleaner. Cleaning time related to the nozzle size and the amount of contamination. In most cases, 3-5 minutes will be sufficient. \n\n"
            "7- Remove the nozzles from the cleaning solution as soon as contamination is no longer present. \n\n"
            "8- If nozzles are not completely clean, use the matching size cleaning wire to gently loosen and remove contamination. \n\n"
            "Return the nozzles into the solution and run the Ultrasonic Cleaner for another short cycle to complete the cleaning process. \n\n"
            "-Rinse the Nozzles: \n\n"
            "With the nozzles still attached to the removal tool, rinse with clean, room temperature DI water. \n\n"
            "Universal Instruments recommends using a container wide and deep enough to completely submerge the nozzles and removal tool in the DI water. \n\n"
            "-Dry the Nozzles: \n\n"
            "With the nozzles still attached to the removal tool, dry the nozzles using clean, compressed air. \n\n"
            "When the nozzles are completely dry, install the nozzles back into machine. \n\n",
            "-Scheduled Cleaning: \n\n"
            "1- If experiencing repeated pick errors, inspect the affected nozzle and clean if needed. \n\n"
            "2- Cleaning cycle is related to the specific customer application. \n\n"
            "3- Nozzle configuration and component mix will determine proper cleaning schedule. \n\n"
            "4- Monitor the condition of nozzles and clean as required to remove contaminates. \n\n"
            "** Before and After Following Best Practices: \n\n"
            "1- Before: \n",
            "\img|nozzle/03-03-image.png",
            "2- After: \n",
            "\img|nozzle/03-04-image.png",
        ]
    