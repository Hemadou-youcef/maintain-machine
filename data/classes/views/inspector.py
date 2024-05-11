import tkinter as tk
from tkinter.messagebox import showinfo
import customtkinter
from data.classes.views.views import ParentView
from data.classes.analyse_data.diagnosisTree import DiagnosisTree

class View(ParentView):
    def __init__(self, master=None, state_manager=None, *args, **kwargs):
        super().__init__(master, state_manager,title="Home", *args, **kwargs)
       
    def content(self):
        current_part = self.state_manager.get_state("part_inspected_information")['part']
        current_question_index = self.state_manager.get_state("part_inspected_information")['current_question_index']


        # Add any widgets or components here
        label = customtkinter.CTkLabel(self.master, text="Inspector - "+current_part)
        label.pack()

        submit_button = customtkinter.CTkButton(master=self.master, text="Submit", command=lambda: self.submit())
        submit_button.pack(fill="none", expand=True)

        scrollable_frame = self.create_frame()

        # Insert Questions
        self.diagnosis_tree = DiagnosisTree(current_part)

        label = customtkinter.CTkLabel(master=scrollable_frame, text=self.diagnosis_tree.getQuestion(current_question_index))
        label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
            
            # Check the type of the question and decide which widget to use
        if self.diagnosis_tree.getQuestionType(current_question_index) == 'YesNo':
            self.questionElement = self.create_yes_no_widget(0,scrollable_frame)
        elif self.diagnosis_tree.getQuestionType(current_question_index) == 'Input':
            self.questionElement = self.create_input_widget(0,scrollable_frame)

        return [label, scrollable_frame, submit_button, self.questionElement]
    
    def submit(self):
        # get the result of the question
        question_answer = self.questionElement.get()
        question_result = self.diagnosis_tree.getResult(self.state_manager.get_state("part_inspected_information")['current_question_index'], question_answer)
        # result of this function is a list of 3 elements
        # the first element is the question answer
        # the second element is the next question index
        # the third element is a boolean to tell that the question loop is stopped or not

        if question_result[2]:
            # if the loop is stopped, then show the answers
            showinfo("Result", question_result[0])
        else:
            # if the loop is not stopped, then save this question information and load the next question
            self.state_manager.get_state("part_inspected_information")['questions'].append({
                "question_index": self.state_manager.get_state("part_inspected_information")['current_question_index'],
                "question_answer": self.questionElement.get(),
                "question_result": question_result
            })

            self.state_manager.set_state("part_inspected_information",question_result[1])
            self.state_manager.get_state("load_view")(name="inspector")



    
    def create_frame(self):
        # Create Scrollable Frame
        CTkScrollableFrame = customtkinter.CTkScrollableFrame(self.master)
        CTkScrollableFrame.pack(fill="both", expand=True)
        CTkScrollableFrame.columnconfigure(0, weight=2)
        CTkScrollableFrame.columnconfigure(1, weight=1)
        return CTkScrollableFrame
    

    def create_input_widget(self,row,frame):
        entry = customtkinter.CTkEntry(frame)
        entry.grid(row=row, column=1, padx=10, pady=10,sticky='ns', columnspan=2)
        return entry
        
    def create_yes_no_widget(self,row,frame):
        var = tk.StringVar()
        var.set('No')
        yes = customtkinter.CTkRadioButton(frame, text='Yes', variable=var, value='Yes')
        yes.grid(row=row, column=1, padx=10, pady=10,sticky='e')
        no = customtkinter.CTkRadioButton(frame, text='No', variable=var, value='No')
        no.grid(row=row, column=2, padx=10, pady=10,sticky='e')
        
        return var