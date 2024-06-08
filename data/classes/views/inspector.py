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
        current_question_index = self.state_manager.get_state("part_inspected_information")['current_question_index']


        # Add any widgets or components here
        label = customtkinter.CTkLabel(self.master, text="Inspector - "+current_part )
        label.grid(row=1, column=0, padx=10, pady=10, sticky=customtkinter.W)

        submit_button = customtkinter.CTkButton(master=self.master, text="Submit", command=lambda: self.submit())

        # scrollable_frame = self.create_frame()

        # Insert Questions
        self.diagnosis_tree = DiagnosisTree(current_part)

        label = customtkinter.CTkLabel(master=self.master, text=self.diagnosis_tree.getQuestion(current_question_index))
        label.grid(row=2, column=0, padx=10, pady=10, columnspan=4)
            
            # Check the type of the question and decide which widget to use
        if self.diagnosis_tree.getQuestionType(current_question_index) == 'YesNo':
            self.questionElement = self.create_yes_no_widget(3,self.master)
        elif self.diagnosis_tree.getQuestionType(current_question_index) == 'Input':
            self.questionElement = self.create_input_widget(3,self.master)
            
        submit_button.grid(row=4, column=0, padx=10, pady=10, columnspan=4)
        # create back button to go to the previous question if the current question is not the first question
        if current_question_index > 0:
            back_button = customtkinter.CTkButton(master=self.master, text="Back", command=lambda: self.back_to_previous_question())
            back_button.grid(row=5, column=0, padx=10, pady=10, columnspan=4)
        
        return [label, submit_button, self.questionElement]
    
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
        

    def create_input_widget(self,row,frame):
        entry = customtkinter.CTkEntry(frame)
        entry.grid(row=row, column=1, padx=10, pady=10, sticky='w')
        return entry
        
    def create_yes_no_widget(self,row,frame):
        var = tk.StringVar()
        var.set('Yes')
        yes = customtkinter.CTkRadioButton(frame, text='Yes', variable=var, value='Yes')
        yes.grid(row=row, column=1, padx=10, pady=10, sticky='w')
        no = customtkinter.CTkRadioButton(frame, text='No', variable=var, value='No')
        no.grid(row=row, column=2, padx=10, pady=10, sticky='w')
        
        return var