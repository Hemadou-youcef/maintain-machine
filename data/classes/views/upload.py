import customtkinter
from tkinter import filedialog
from tkinter.messagebox import showinfo

import pandas as pd


from data.classes.views.views import ParentView

class View(ParentView):
    def __init__(self, master=None, state_manager=None, *args, **kwargs):
        super().__init__(master, state_manager,title="App", *args, **kwargs)
       
        
    def content(self):
        # create upload button
        upload_button_ = customtkinter.CTkButton(self.master, text="Upload", command=self.upload_file)
        upload_button_.pack(fill="none", expand=True)
        return [upload_button_]
    
        
    def upload_file(self):
        filepath = filedialog.askopenfilename()
        if filepath == "":
            return
        elif self.check_file_exists(filepath):
            # VALIDATE THE FILE
            self.file_data = pd.read_csv(filepath,header=0,sep="\t")
            self.state_manager.set_state("file_data", self.file_data)
            self.state_manager.set_state("do_analysis", True)
            self.state_manager.get_state("load_view")(name="home")
        else:
            showinfo('Error', 'File not found')
            
    def check_file_exists(self,filepath):
        try:
            with open(filepath, 'r') as file:
                return True
        except FileNotFoundError:
            return False