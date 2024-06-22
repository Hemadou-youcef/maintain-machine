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
        label = customtkinter.CTkLabel(self.master, text=f"Nozzles List 🛠️")
        label.grid(row=1, column=0, padx=10, pady=10, sticky=customtkinter.W)
        
        # show list of Nozzles
        scrollable_frame = self.create_frame()

        Nozzles = self.state_manager.get_state("parts")[2]
        inspected_Nozzles = Nozzles['inspected_data']
        
        NozzlesElement = []
        for i, nozzle in enumerate(inspected_Nozzles):
            label = customtkinter.CTkLabel(master=scrollable_frame, text=f"{nozzle['name']}")
            label.grid(row=i, column=0, padx=10, pady=10, sticky='w')
            
            # Check the type of the question and decide which widget to use
            if nozzle['is_failure'] and not nozzle['is_inspected']:
                # create a button to navigate to the inspector view
                nozzle_button = customtkinter.CTkButton(master=scrollable_frame, text="Inspect 🛠️", command= lambda nozzle=nozzle: self.inspect_nozzle(nozzle))
                nozzle_button.grid(row=i, column=1, padx=10, pady=10, sticky='w')
                NozzlesElement.append(nozzle_button)
            else:
                # create a label to show the state of the Nozzles
                state_label = customtkinter.CTkLabel(master=scrollable_frame, text=nozzle['state_label'])
                state_label.grid(row=i, column=1, padx=10, pady=10, sticky='w')
                NozzlesElement.append(state_label)
                

        return [label, scrollable_frame, *NozzlesElement]

    def create_frame(self):
        # Create Scrollable Frame
        CTkScrollableFrame = customtkinter.CTkScrollableFrame(self.master)
        CTkScrollableFrame.grid(row=2, column=0, padx=10, pady=10, sticky=customtkinter.NSEW,columnspan=10)
        CTkScrollableFrame.columnconfigure(0, weight=2)
        CTkScrollableFrame.columnconfigure(1, weight=1)
        return CTkScrollableFrame
    
    def inspect_nozzle(self,Nozzles):
        self.state_manager.set_state("part_inspected_information",{
            "part": "nozzle",
            "information": Nozzles,
            "solutions": []
        })
        self.state_manager.get_state("load_view")(name="inspector")