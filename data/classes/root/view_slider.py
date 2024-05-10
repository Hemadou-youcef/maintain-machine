import customtkinter
import data.classes.root.state as state

# views slider class
import data.classes.views.views as views
import data.classes.views.home as home
import data.classes.views.upload as upload
import data.classes.views.questions as questions
import data.classes.views.spindles as spindles


class ViewSlider(customtkinter.CTk):
    def __init__(self, master, title="App", *args, **kwargs):
        super().__init__()
        self.master = master
        self.state_manager = state.StateManager()
        
        # create window and set title
        self.title(title)
        self.state_manager.set_state("title", title)
        
        # check if there is width and height in kwargs
        if "width" in kwargs and "height" in kwargs:
            self.geometry(f"{kwargs['width']}x{kwargs['height']}")
        else:
            self.geometry("800x600")
            
        # set state for load view and refresh view
        self.state_manager.set_state("load_view", self.load_view)
        
            
        # create a frame to hold the views
        self.container = customtkinter.CTkFrame(self)
        self.container.pack(fill="both", expand=True)
        
        # load views dictionary
        self.load_view_dict()
        
        
    def header(self, title):
        # create a frame to hold the header 
        # header contain the title of the view and navigation buttons
        # self.header = tk.Frame(self.container)
        # self.header.pack(fill="x")
        
        # # create a label to hold the title
        # self.title = tk.Label(self.header, text=title)
        # self.title.pack(side="left")
        pass
        
    def add_view(self, view, name):
        self.views[name] = view
        
    def load_view(self, name):
        view = self.views.get(name)
        if view:
            # clear the container and state manager current view children
            self.clear_view()
            
            
            # change the title of the view
            view.load_title(self)
            
            # load the view
            view.load_content()
        else:
            print(f"View {name} not found")
        
    def clear_view(self):
        for child in self.state_manager.get_state("current_view_widget"):
            child.destroy()
            
        self.state_manager.set_state("current_view_widget", [])
            
        # re-render the window
        customtkinter.CTk.update(self)
        
        
    def change_view(self, name):
        self.show_view(name)
        self.views[name].on_show()
        
        
    def load_view_dict(self):
        # create a dictionary to hold the views
        self.views = {
            "upload": upload.View(master=self.container,state_manager=self.state_manager),
            "home": home.View(master=self.container,state_manager=self.state_manager),
            "spindles": spindles.View(master=self.container,state_manager=self.state_manager)
        }
        
        
    def destroy(self):
        self.quit()