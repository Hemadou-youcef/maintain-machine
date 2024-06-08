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
        part_information = self.state_manager.get_state("part_inspected_information")


        # Add any widgets or components here
        label = customtkinter.CTkLabel(self.master, text="Inspector - " + part_information['part'])
        label.grid(row=1, column=0, padx=10, pady=10, sticky=customtkinter.W)

        submit_button = customtkinter.CTkButton(master=self.master, text="Fixed", command=lambda: self.submit())

        # create a frame to hold the solutions
        solutions_frame = self.create_frame()

        self.diagnosis_tree = DiagnosisTree(part_information['part'])
        if part_information['part'] == "feeder":
            # check the biggest failed section in the feeder
            feeder = self.state_manager.get_state("parts")[0]['data']
            section_position = [5,6,7,8,9,10,11,12]
            # find the biggest failed section by checking each section in the feeder feeder.iloc[part_information['information']['number'] - 1, section_position]
            biggest_failed_section = section_position[0]
            for section in section_position:
                if feeder.iloc[part_information['information']['number'] - 1, section] > feeder.iloc[part_information['information']['number'] - 1, biggest_failed_section]:
                    biggest_failed_section = section

            # get the solution for the biggest failed section
            solution = self.diagnosis_tree.get_solution(feeder.columns[biggest_failed_section])

            
            solution_buttons = []
            # create loop of button of each solution
            for i, sol in enumerate(solution):
                solution_button = customtkinter.CTkButton(master=solutions_frame, text=sol["name"], command=lambda sol=sol: self.show_solution(sol))
                solution_button.grid(row=0, column=i, padx=10, pady=10, sticky='w')
                solution_buttons.append(solution_button)

        
        return [label, submit_button, solutions_frame, *solution_buttons]
    

    def show_solution(self, solution):
        # save the solution in the state manager
        self.state_manager.set_state("current_solution", solution)
        # load the solution detail view
        self.state_manager.get_state("load_view")(name="solution_detail")
    
    
    def submit(self):
        # get the result of the question
        question_answer = self.questionElement.get()
        question_result = self.diagnosis_tree.getResult(self.state_manager.get_state("part_inspected_information")['current_question_index'], question_answer)
        # result of this function is a list of 3 elements
        # the first element is the question answer
        # the second element is the next question index
        # the third element is a boolean to tell that the question loop is stopped or not

        self.state_manager.set_state("part_inspected_information",{
                "part": self.state_manager.get_state("part_inspected_information")['part'],
                "information": self.state_manager.get_state("part_inspected_information")['information'],
                "questions": self.state_manager.get_state("part_inspected_information")['questions'] + [{
                    "label": self.diagnosis_tree.getQuestion(self.state_manager.get_state("part_inspected_information")['current_question_index']),
                    "index": self.state_manager.get_state("part_inspected_information")['current_question_index'],
                    "answer": self.questionElement.get(),
                    "result": question_result
                }],
                "current_question_index": question_result[2],
                "result": question_result[3]
            })
        
        if question_result[3]:
            # if the answer is True then all is good
            if question_result[1] == None:
                showinfo("Inspection Complete", "All is good")
                self.state_manager.get_state("load_view")(name="part_information")
            else:
                showinfo("Inspection Complete", question_result[1])
                self.state_manager.get_state("load_view")(name="part_information")
        else:
            # if the loop is not stopped, then save this question information and load the next question
            # self.state_manager.get_state("part_inspected_information")['questions'].append({
            #     "question_index": self.state_manager.get_state("part_inspected_information")['current_question_index'],
            #     "question_answer": self.questionElement.get(),
            #     "question_result": question_result
            # })
            self.state_manager.get_state("load_view")(name="inspector")

    def back_to_previous_question(self):
        # remove the last question from the questions list
        self.state_manager.set_state("part_inspected_information",{
            "part": self.state_manager.get_state("part_inspected_information")['part'],
            "information": self.state_manager.get_state("part_inspected_information")['information'],
            "questions": self.state_manager.get_state("part_inspected_information")['questions'][:-1],
            "current_question_index": self.state_manager.get_state("part_inspected_information")["questions"][-1]["index"],
        })
        # load the previous question
        self.state_manager.get_state("load_view")(name="inspector")

    def create_frame(self):
        # Create Scrollable Frame
        CTkScrollableFrame = customtkinter.CTkScrollableFrame(self.master)
        CTkScrollableFrame.grid(row=2, column=0, padx=10, pady=10, sticky=customtkinter.NSEW,columnspan=10)
        return CTkScrollableFrame
        