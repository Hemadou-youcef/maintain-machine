import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 7
        self.name = "Perform Initial Setup and Test the Spindles"
        self.objects = [
            "-Perform Initial Setup\n\n"
            "To perform initial setup, do the following:\n\n"
            "1. Select the Initial Setup button and follow the on-screen steps in the application to perform the Initial Setup.\n\n"
            "Mount the setup spindle to the tester as shown in the following illustration.\n",
            "\img|spindle/07-01-image.png",
            "*The Initial Setup must be completed before testing spindles.\n\n"
            "2. After completing the Initial Setup, the Initial Setup button will display a green check mark as shown in the following illustration. The Test Spindle button is enabled.\n",
            "\img|spindle/07-02-image.png",
            "-Test the Spindles \n\n"
            "To test the spindles, do the following:\n\n"
            "1. Select the Test Spindle button and follow the on-screen steps to test a spindle. After spindle test is completed, the screen will display whether the spindle passed or failed testing.\n\n"
            "2. If the spindle testing failed, a screen similar to the following will display:\n",
            "\img|spindle/07-03-image.png",
            "In many cases, the spindle tester can identify the spindle components that are the likely cause of failure and need to be examined and then potentially cleaned or replaced. If this is the case, then for each failed test, the Error Report screen will report an error code, the corresponding description of the failure in the spindle components, and a recommended repair action. Also, the components in the view on the right will be highlighted. For more in-depth spindle troubleshooting information, refer to the Spindle Troubleshooting section of this document.\n\n"
            "3. When finished reviewing the error report, select OK to display the Test Spindle Results screen.\n",
            "\img|spindle/07-04-image.png",
            "4. Select the Data button to review the test results data.\n",
            "\img|spindle/07-05-image.png",
            "\n\n",
            "\img|spindle/07-06-image.png",
            "5. When finished reviewing the data, enter any desired comments in the Comments section and select OK to proceed.\n\n"
            "• Select the Finish button to save test data.\n\n"
            "• Select the Previous button to return to the test selection screen.\n\n"
            "• Select the Cancel button to return to the main screen without saving test data.\n\n"
            "6. If the spindle passed testing, the following screen will display.\n",
            "\img|spindle/07-07-image.png",
            "• Select the Data button to review the test results.\n\n"
            "• Select the Finish button to save the test data.\n\n"
            "• Select the Previous button to return to the test selection screen.\n\n"
            "• Select Cancel to return to the main screen without saving test data.\n\n"
            "7. Remove the spindle from the Spindle Tester.\n\n"
        ]
    