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
        views = {
            "feeder": "feeders",
            "nozzle": "nozzles",
            "spindle": "spindles"
        }
        back_button = customtkinter.CTkButton(self.master, text="⬅", command=lambda: self.state_manager.get_state("load_view")(name=views[self.state_manager.get_state("part_inspected_information")['part']]))
        # grid it in the top left corner
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        return [back_button]
    
    def content(self):
        part_information = self.state_manager.get_state("part_inspected_information")


        submit_button = customtkinter.CTkButton(master=self.master, text="Fixed", command=lambda: self.submit(),height=70)

        # create a frame to hold the solutions
        text = [
            f"Inspector - {part_information['part']}",
            f"Part Name: {part_information["information"]["name"]}",
            f"Total Failure: {part_information["information"]["total_failure"]}",
            
        ]
        solutions_frame = self.create_frame(self.master)

        self.diagnosis_tree = DiagnosisTree(part_information['part'])
        if part_information['part'] == "feeder":
            # check the biggest failed section in the feeder
            feeder = self.state_manager.get_state("parts")[0]['data']
            section_position = [6,7,8,9,10,11,12,13]
            # find the biggest failed section by checking each section in the feeder feeder.iloc[part_information['information']['number'] - 1, section_position]
            biggest_failed_section = section_position[0]
            for section in section_position:
                if feeder.iloc[part_information['information']['number'] - 1, section] > feeder.iloc[part_information['information']['number'] - 1, biggest_failed_section]:
                    biggest_failed_section = section

            # get the solution for the biggest failed section
            solutions = self.diagnosis_tree.get_solution(feeder.columns[biggest_failed_section])
            text.append(f"Biggest Failure Type: {feeder.columns[biggest_failed_section]}")

        elif part_information['part'] == "spindle":
            # check the biggest failed section in the spindle
            spindle = self.state_manager.get_state("parts")[1]['data']
            section_position = [4,5,6,7,8]
            # find the biggest failed section by checking each section in the spindle spindle.iloc[part_information['information']['number'] - 1, section_position]
            biggest_failed_section = section_position[0]
            for section in section_position:
                if spindle.iloc[part_information['information']['number'] - 1, section] > spindle.iloc[part_information['information']['number'] - 1, biggest_failed_section]:
                    biggest_failed_section = section

            # get the solution for the biggest failed section
            solutions = self.diagnosis_tree.get_solution(spindle.columns[biggest_failed_section])
            text.append(f"Biggest Failure Type: {spindle.columns[biggest_failed_section]}")

        elif part_information['part'] == "nozzle":
            # check the biggest failed section in the nozzle
            nozzle = self.state_manager.get_state("parts")[2]['data']
            section_position = [4,5,6,7]
            # find the biggest failed section by checking each section in the nozzle nozzle.iloc[part_information['information']['number'] - 1, section_position]
            biggest_failed_section = section_position[0]
            for section in section_position:
                if nozzle.iloc[part_information['information']['number'] - 1, section] > nozzle.iloc[part_information['information']['number'] - 1, biggest_failed_section]:
                    biggest_failed_section = section

            # get the solution for the biggest failed section
            solutions = self.diagnosis_tree.get_solution(nozzle.columns[biggest_failed_section])
            text.append(f"Biggest Failure Type: {nozzle.columns[biggest_failed_section]}")
        

        label = customtkinter.CTkLabel(self.master, text="\n".join(text), font=("Helvetica", 15),justify="left")
        label.grid(row=1, column=0, padx=10, pady=10, sticky=customtkinter.W)

        # create loop of button of each solution
        solution_buttons = [] 
        for i, sol in enumerate(solutions):
            # create a label to show the solution name
            solution_label = customtkinter.CTkLabel(solutions_frame, text=sol.get_name())
            solution_label.grid(row=i, column=0, padx=10, pady=10, sticky='w')


            # create a button to show the solution
            solution_button = customtkinter.CTkButton(master=solutions_frame, text="show", command=lambda sol=sol: self.show_solution(sol))
            solution_button.grid(row=i, column=1, padx=10, pady=10, sticky='w')

            # create a checkbox to show if the solution is applied or not
            is_applied = tk.BooleanVar(master=solutions_frame,value=sol.get_id() in part_information['solutions'])
            
            applied_checkbox = customtkinter.CTkCheckBox(master=solutions_frame, text="", variable=is_applied,state=tk.DISABLED)
            applied_checkbox.grid(row=i, column=2, padx=10, pady=10, sticky='w')
            
            solution_buttons.append(solution_button)

        # show button in center of the bottom that will Submit the inspection
        submit_button.grid(row=3, column=0, padx=10, pady=10,sticky=customtkinter.NSEW,columnspan=4)

        
        return [label, submit_button, solutions_frame, *solution_buttons,is_applied,applied_checkbox]
    

    def show_solution(self, solution):
        self.state_manager.set_state("current_solution", solution)
        self.state_manager.get_state("load_solution")()
        
        # # create sub window using tkinter to show solution
        # sub_window = tk.Toplevel(self.master)
        # sub_window.title(solution.get_name())
        # sub_window.geometry("500x500")
        # # get the solution content
        # solution_content = solution.content(sub_window)
        
        # # create a button to check the sub window
        # check_button = customtkinter.CTkButton(sub_window, text="Check", command=lambda: sub_window.destroy())
        # check_button.pack()
        
        # self.state_manager.set_state("current_solution", [sub_window,*solution_content,check_button])
        
    
    
    def submit(self):
        # submit
        # save the state of the part in the state manager
        parts_data = self.state_manager.get_state("parts")
        inspected_part = self.state_manager.get_state("part_inspected_information")
        part_index = 0
        if inspected_part['part'] == "feeder":
            part_index = 0
        elif inspected_part['part'] == "spindle":
            part_index = 1
        elif inspected_part['part'] == "nozzle":
            part_index = 2
        
        current_parts = parts_data[0]["inspected_data"][inspected_part["information"]["number"] - 1]
        current_parts["solutions"] = inspected_part["solutions"]
        current_parts["state_label"] = "FIXED ✅"
        current_parts["state"] = True
        current_parts["is_inspected"] = True
        # replace parts_data with the new data    
        parts_data[part_index]["inspected_data"][inspected_part["information"]["number"] - 1] = current_parts   
        # save the new data in the state manager
        self.state_manager.set_state("parts", parts_data)
        # navigate to the part view
        views = {
            "feeder": "feeders",
            "nozzle": "nozzles",
            "spindle": "spindles"
        }
        self.state_manager.get_state("load_view")(name=views[inspected_part['part']]) 
        
            
    def create_frame(self,master):
        # Create Scrollable Frame
        CTkScrollableFrame = customtkinter.CTkScrollableFrame(master)
        CTkScrollableFrame.grid(row=2, column=0, padx=10, pady=10, sticky=customtkinter.NSEW,columnspan=10)
        # columnconfigure
        CTkScrollableFrame.columnconfigure(0, weight=1)
        CTkScrollableFrame.columnconfigure(1, weight=1)
        CTkScrollableFrame.columnconfigure(2, weight=1)
        return CTkScrollableFrame
        