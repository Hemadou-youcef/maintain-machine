import customtkinter
from data.classes.views.views import ParentView

class View(ParentView):
    def __init__(self, master=None, state_manager=None, *args, **kwargs):
        super().__init__(master, state_manager,title="Home", *args, **kwargs)
       
        
    def content(self):
        self.analyse_data()
        # Add any widgets or components here
        label = customtkinter.CTkLabel(self.master, text="Home")
        label.pack()
        
        # create four buttons each button navigate to a different view
        spindle_button = customtkinter.CTkButton(self.master,
                                                  text="Spindles"
                                                 , command=lambda: self.state_manager.get_state("load_view")(name="spindles"))
        spindle_button.pack()
        nozzles_button = customtkinter.CTkButton(self.master, text="Nozzles", command=lambda: self.state_manager.get_state("load_view")(name="nozzles"))
        nozzles_button.pack()
        
        return [label, spindle_button, nozzles_button]
        
        
    def analyse_data(self):
        # get the file data from the state manager
        file_data = self.state_manager.get_state("file_data")
        
        # check if the file data is available
        if file_data is not None:
            # perform some analysis on the data
            # start with spindles
            spindles_data = []
            while True:
                try:
                    spindles_data.append({
                        "number": len(spindles_data) + 1,
                        "failures_rate": float(file_data.values[len(spindles_data)][9].replace(",", ".")),
                        "is_failure": int(float(file_data.values[len(spindles_data)][9].replace(",", "."))) > 1,
                        "questions": [],
                        "state": "in process" 
                    })

                except IndexError:
                    break
            # set the data in the state manager
            self.state_manager.set_state("spindles_data", spindles_data)
        else:
            print("No data available")    
    