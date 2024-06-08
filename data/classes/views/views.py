import customtkinter

class ParentView(customtkinter.CTkFrame):
    def __init__(self, master=None,state_manager=None,title="", *args, **kwargs):
        super().__init__(master)
        # Initialize any common attributes or variables here
        self.master = master
        self.state_manager = state_manager
        self.title = title
        self.header = False
        
        # if header argument is passed in kwargs
        if "header" in kwargs:
            self.header(kwargs["header"])
        
    def load_content(self):
        self.state_manager.set_state("current_view_widget", [*self.header_content(),*self.content()])
        
        
    def content(self):
        pass
    
    def header_content(self):
        return []
        
    def get_title(self):
        return self.title
    
    def isHeaderNeeded(self):
        return self.header
    
    def load_title(self,master):
        master.title(self.title)
    
    def change_title(self, title):
        self.title = title
        self.master.header(title)
        
        