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

        submit_button = customtkinter.CTkButton(master=self.master, text="Submit", command=lambda: self.submit())
        submit_button.pack(fill="none", expand=True)

        scrollable_frame = self.createFrame()

        # Insert Questions
        diagnosis_tree = DiagnosisTree()
        questions = diagnosis_tree.getQuestions()
        questionsElement = []
        for i, question in enumerate(questions):
            label = customtkinter.CTkLabel(master=scrollable_frame, text=diagnosis_tree.getQuestion(question))
            label.grid(row=i, column=0, padx=10, pady=10, sticky='w')
            
            # Check the type of the question and decide which widget to use
            if diagnosis_tree.getQuestionType(question) == 'YesNo':
                questionsElement.append(self.createYesNoWidget(i,scrollable_frame))
            elif diagnosis_tree.getQuestionType(question) == 'Input':
                questionsElement.append(self.createInputWidget(i,scrollable_frame))

        

        return [label, scrollable_frame, submit_button]
    
    def submit(self):
        pass
    
    def createFrame(self):
        # Create Scrollable Frame
        CTkScrollableFrame = customtkinter.CTkScrollableFrame(self.master)
        CTkScrollableFrame.pack(fill="both", expand=True)
        CTkScrollableFrame.columnconfigure(0, weight=2)
        CTkScrollableFrame.columnconfigure(1, weight=1)
        return CTkScrollableFrame
    
    def createQuestion(self,frame):
        pass

    def createInputWidget(self,row,frame):
        entry = customtkinter.CTkEntry(frame)
        entry.grid(row=row, column=1, padx=10, pady=10,sticky='ns', columnspan=2)
        return entry
        
    def createYesNoWidget(self,row,frame):
        var = tk.StringVar()
        var.set('No')
        yes = customtkinter.CTkRadioButton(frame, text='Yes', variable=var, value='Yes')
        yes.grid(row=row, column=1, padx=10, pady=10,sticky='e')
        no = customtkinter.CTkRadioButton(frame, text='No', variable=var, value='No')
        no.grid(row=row, column=2, padx=10, pady=10,sticky='e')
        
        return var