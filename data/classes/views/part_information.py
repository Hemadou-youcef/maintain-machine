import tkinter as tk
from tkinter.messagebox import showinfo
import customtkinter
from data.classes.views.views import ParentView
from data.classes.analyse_data.diagnosisTree import DiagnosisTree

class View(ParentView):
    def __init__(self, master=None, state_manager=None, *args, **kwargs):
        super().__init__(master, state_manager,title="Home", *args, **kwargs)
    
    def header_content(self):
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=1)
        # create a button to navigate to the upload view
        back_button = customtkinter.CTkButton(self.master, text="⬅", command=lambda: self.state_manager.get_state("load_view")(name=self.state_manager.get_state("part_inspected_information")['part']))
        # grid it in the top left corner
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        return [back_button]
    
    def content(self):
        current_part = self.state_manager.get_state("part_inspected_information")['part']
        questions = self.state_manager.get_state("part_inspected_information")['questions']


        # Add any widgets or components here
        label = customtkinter.CTkLabel(self.master, text="Result - "+current_part)
        label.grid(row=1, column=0, padx=10, pady=10, sticky=customtkinter.W)

        submit_button = customtkinter.CTkButton(master=self.master, text="Save", command=lambda: self.save())
        submit_button.grid(row=2, column=0, padx=10, pady=10, columnspan=4)

        # create scrollable frame
        questions_scrollable_frame = self.create_frame(3)
        
        state_label = ["✅","🛠️","❌"]
        # create label for the questions list
        for i, question in enumerate(questions):
            if question['result'][0]:
                label = customtkinter.CTkLabel(master=questions_scrollable_frame, text=f"{i+1}: {question['label']} - {state_label[0]}")    
            elif question['result'][0] == False and question['result'][3] == False:
                label = customtkinter.CTkLabel(master=questions_scrollable_frame, text=f"{i+1}: {question['label']} - {state_label[1]}")
            else:
                label = customtkinter.CTkLabel(master=questions_scrollable_frame, text=f"{i+1}: {question['label']} - {state_label[2]}")
            label.grid(row=i, column=0, padx=10, pady=10, sticky='w')
            
        # Observation frame
        observation_scrollable_frame = self.create_frame(4)
        
        # add observation label
        observation_label = customtkinter.CTkLabel(master=observation_scrollable_frame, text="Observations:")
        observation_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        # add observation text
        observation_text = "All is good!" if all([question['result'][0] for question in questions]) else questions[-1]['result'][1]
        observation_content = customtkinter.CTkLabel(master=observation_scrollable_frame, text=observation_text)
        observation_content.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        
        return [label, submit_button, questions_scrollable_frame, observation_scrollable_frame, observation_label, observation_content]
    
    def save(self):
        # save the state of the part in the state manager
        current_part = self.state_manager.get_state("part_inspected_information")['part']
        if current_part == "spindles":
            spindle_data = self.state_manager.get_state("spindles_data")
            spindle_index = self.state_manager.get_state("part_inspected_information")['information']['number'] - 1
            # add information the spindle and change state
            spindle_data[spindle_index]['questions'] = self.state_manager.get_state("part_inspected_information")['questions']
            spindle_data[spindle_index]['state_label'] = "DAMAGED ❌" if self.state_manager.get_state("part_inspected_information")['result'] == False else "FIXED ✅"
            spindle_data[spindle_index]['state'] = not self.state_manager.get_state("part_inspected_information")['result']
            spindle_data[spindle_index]['is_inspected'] = True
            # replace the spindle data in the state manager
            self.state_manager.set_state("spindles_data", spindle_data)
            self.state_manager.get_state("load_view")(name="spindles")
        elif current_part == "nozzles":
            nozzles_data = self.state_manager.get_state("nozzles_data")
            nozzles_index = self.state_manager.get_state("part_inspected_information")['information']['number'] - 1
            # add information the nozzles and change state
            nozzles_data[nozzles_index]['questions'] = self.state_manager.get_state("part_inspected_information")['questions']
            nozzles_data[nozzles_index]['state_label'] = "DAMAGED ❌" if self.state_manager.get_state("part_inspected_information")['result'] == False else "FIXED ✅"
            nozzles_data[nozzles_index]['is_failure'] = not self.state_manager.get_state("part_inspected_information")['result']
            # replace the nozzles data in the state manager
            self.state_manager.set_state("nozzles_data", nozzles_data)
            self.state_manager.get_state("load_view")(name="nozzles")
        else:
            self.state_manager.get_state("load_view")(name="home")
        
            
    
    def create_frame(self, row=0):
        # Create Scrollable Frame
        CTkScrollableFrame = customtkinter.CTkScrollableFrame(self.master)
        CTkScrollableFrame.grid(row=row, column=0, padx=10, pady=10, sticky=customtkinter.NSEW,columnspan=10)
        CTkScrollableFrame.columnconfigure(0, weight=2)
        CTkScrollableFrame.columnconfigure(1, weight=1)
        return CTkScrollableFrame