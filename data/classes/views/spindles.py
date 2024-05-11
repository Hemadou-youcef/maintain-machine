import tkinter as tk
import customtkinter
from data.classes.views.views import ParentView
from data.classes.analyse_data.diagnosisTree import DiagnosisTree

class View(ParentView):
    def __init__(self, master=None, state_manager=None, *args, **kwargs):
        super().__init__(master, state_manager,title="Home", *args, **kwargs)
       
    def content(self):
        # Add any widgets or components here
        label = customtkinter.CTkLabel(self.master, text="Spindles")
        label.pack()
        
        # show list of spindles
        scrollable_frame = self.create_frame()

        # Insert Spindles from self.state_manager.get_state("spindles_data")
        spindles = self.state_manager.get_state("spindles_data")
        spindlesElement = []
        for i, spindle in enumerate(spindles):
            label = customtkinter.CTkLabel(master=scrollable_frame, text=f"Spindle {spindle['number']}")
            label.grid(row=i, column=0, padx=10, pady=10, sticky='w')
            
            # Check the type of the question and decide which widget to use
            if spindle['is_failure']:
                # create a button to navigate to the inspector view
                spindle_button = customtkinter.CTkButton(master=scrollable_frame, text="Inspect 🛠️", command= lambda: self.inspect_spindle(spindle))
                spindle_button.grid(row=i, column=1, padx=10, pady=10, sticky='w')
                spindlesElement.append(spindle_button)
            else:
                # create a label to show the state of the spindle
                state_label = customtkinter.CTkLabel(master=scrollable_frame, text=spindle['state'])
                state_label.grid(row=i, column=1, padx=10, pady=10, sticky='w')
                spindlesElement.append(state_label)

        return [label, scrollable_frame, *spindlesElement]

    def create_frame(self):
        # Create Scrollable Frame
        CTkScrollableFrame = customtkinter.CTkScrollableFrame(self.master)
        CTkScrollableFrame.pack(fill="both", expand=True)
        CTkScrollableFrame.columnconfigure(0, weight=2)
        CTkScrollableFrame.columnconfigure(1, weight=1)
        return CTkScrollableFrame
    
    def inspect_spindle(self,spindle):
        self.state_manager.set_state("part_inspected_information",{
            "part": "spindle",
            "information": spindle,
            "questions": [],
            "current_question_index": 0,
        })
        self.state_manager.get_state("load_view")(name="inspector")