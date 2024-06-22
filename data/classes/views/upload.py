import customtkinter
from tkinter import filedialog
from tkinter.messagebox import showinfo

import pandas as pd


from data.classes.views.views import ParentView

class View(ParentView):
    def __init__(self, master=None, state_manager=None, *args, **kwargs):
        super().__init__(master, state_manager,title="App", *args, **kwargs)
       
        
    def content(self):
        # CREATE 
        # create upload button
        upload_button_ = customtkinter.CTkButton(self.master, text="SELECT DATA FILE", command=self.upload_file,corner_radius=0,bg_color="#161d3d",width=200, height=50)
        upload_button_.pack(fill="none", expand=True)
        return [upload_button_]
    
        
    def upload_file(self):
        filepath = filedialog.askopenfilename()
        if filepath == "":
            return
        elif self.check_file_exists(filepath):
            # VALIDATE THE FILE AND READ THE XLSX FILE
            self.file_data = pd.ExcelFile(filepath)
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