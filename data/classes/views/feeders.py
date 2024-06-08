import tkinter as tk
import customtkinter
from data.classes.views.views import ParentView
from data.classes.analyse_data.diagnosisTree import DiagnosisTree

class View(ParentView):
    def __init__(self, master=None, state_manager=None, *args, **kwargs):
        super().__init__(master, state_manager,title="Home", *args, **kwargs)
       
    def header_content(self):
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=3)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=20)
        # create a button to navigate to the upload view
        back_button = customtkinter.CTkButton(self.master, text="⬅", command=lambda: self.state_manager.get_state("load_view")(name="home"))
        # grid it in the top left corner
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        return [back_button]
    
    def content(self):
        # Add any widgets or components here
        label = customtkinter.CTkLabel(self.master, text=f"Feeders List 🛠️")
        label.grid(row=1, column=0, padx=10, pady=10, sticky=customtkinter.W)
        
        # show list of Feeders
        scrollable_frame = self.create_frame()

        feeders = self.state_manager.get_state("parts")[0]
        inspected_feeders = feeders['inspected_data']
        
        feedersElement = []
        for i, feeder in enumerate(inspected_feeders):
            label = customtkinter.CTkLabel(master=scrollable_frame, text=f"Feeders {feeder['number']}")
            label.grid(row=i, column=0, padx=10, pady=10, sticky='w')
            
            # Check the type of the question and decide which widget to use
            if feeder['is_failure'] and not feeder['is_inspected']:
                # create a button to navigate to the inspector view
                feeder_button = customtkinter.CTkButton(master=scrollable_frame, text="Inspect 🛠️", command= lambda: self.inspect_feeder(feeder))
                feeder_button.grid(row=i, column=1, padx=10, pady=10, sticky='w')
                feedersElement.append(feeder_button)
            else:
                # create a label to show the state of the feeders
                state_label = customtkinter.CTkLabel(master=scrollable_frame, text=feeder['state_label'])
                state_label.grid(row=i, column=1, padx=10, pady=10, sticky='w')
                feedersElement.append(state_label)
                

        return [label, scrollable_frame, *feedersElement]

    def create_frame(self):
        # Create Scrollable Frame
        CTkScrollableFrame = customtkinter.CTkScrollableFrame(self.master)
        CTkScrollableFrame.grid(row=2, column=0, padx=10, pady=10, sticky=customtkinter.NSEW,columnspan=10)
        CTkScrollableFrame.columnconfigure(0, weight=2)
        CTkScrollableFrame.columnconfigure(1, weight=1)
        return CTkScrollableFrame
    
    def inspect_feeder(self,feeders):
        self.state_manager.set_state("part_inspected_information",{
            "part": "feeder",
            "information": feeders,
            "solution": []
        })
        self.state_manager.get_state("load_view")(name="inspector")