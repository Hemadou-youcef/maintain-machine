import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 5
        self.name = "Clean/Lubricate the Spindle Cam"
        self.objects = [
            "-Clean the Spindle Cam \n\n"
            "To clean the spindle cam, do the following: \n\n"
            "1. Use Manual Control to move the beam to the maintenance position. \n\n"
            "2. Push an E-Stop switch. \n\n"
            "3. Push an E-Stop switch. \n\n"
            "4. Remove feeders to get access to the head. \n\n"
            "5. Remove the head cover. \n\n"
            "6. Remove the lower cover. \n\n"
            "7. Apply isopropyl alcohol to a folded 1/2 in. square piece of clean, lint-free cloth. \n\n"
            "8. Pull out the spindle to the immediate right of the Z-Drive Assembly and place the cloth between the spindle cam and the spindle cap. \n",
            "\img|spindle/05-01-image.png",
            "9. Rotate the VRM Turret Assembly counterclockwise until the spindle reaches the immediate left of the Z-Drive Assembly.\n",
            "\img|spindle/05-02-image.png",
            "10. Remove the piece of cloth. If there is a significant amount of lubricant on the cloth, repeat steps 4-6 until the cloth comes out clean. \n\n"
            "-Lubricate the Spindle Cam \n\n"
            "1. Pull out every other spindle in the accessible region of the head shown below, and apply a small amount of Kluber Isoflex Topas NB5051 grease to each spindle cap using a clean, lint-free swab. \n",
            "\img|spindle/05-03-image.png",
            "\n\n",
            "\img|spindle/05-04-image.png",
            "2. Rotate the VRM Turret Assembly counterclockwise to distribute the grease. \n\n"
            "3. Repeat steps 1 and 2 until the entire spindle cam has been lubricated. \n\n"
            "4. Reinstall the lower cover. \n\n"
            "5. Reinstall the head cover. \n\n"
            "6. Reinstall feeders, close the access door(s), and release the Emergency Stop switch. \n\n"
            "7. Repeat procedure for each 30-spindle head. \n\n"
        ]
    