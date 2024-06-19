import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 3
        self.name = "Set Regulator Pressure"
        self.objects = [
            "Setting the regulator pressure must be performed in the following circumstances:  \n\n"
            "• After setting the Phi Zero Offset  \n\n"
            "• After replacing/installing the 30-spindle head \n\n"
            "*Note: Vacuum for all spindles for all heads must be turned on prior to setting the head regulators. \n\n"
            "1. Palm down the machine. \n\n"
            "2. Open access covers. \n\n"
            "3. Select the Head Subsystem Control Icon. \n\n"
            "4. In the Head Subsystem Control window, select the Head/Beam. \n",
            "\img|spindle/03-01-image.png",
            "5. Select the Spindle Data tab. Select Spindle All. Select the Vacuum On button. \n\n"
            "6. If Dual Beam Machine, Select Head2/Beam2 and perform step 5. \n\n"
            "7. If Quad Beam Machine, select Mod B and perform steps 3–6. \n\n"
            "8. Set the regulator pressure: \n\n"
            "a. For the advanced 30-spindle head (which has air pressure monitoring), select the Head Data tab, and select the Air Pressure field. Set the pressure to 68 psi. \n\n"
            "b. For any head other than the advanced 30-spindle head, set the regulator to 70 psi. \n\n"
            "9. In the Head Subsystem Control window, select the Head/Beam. \n\n"
            "10. Select the Spindle Data tab. Select Spindle All. Select thVacuum Off button. \n\n"
            "11. If Dual Beam Machine, select Head2/Beam2 and perform step 10. \n\n"
            "12. If Quad Beam Machine, select Mod B and perform steps 9–10. \n\n"
            
        ]
    