import customtkinter
import data.classes.root.state as state

# views slider class
import data.classes.views.views as views
import data.classes.views.home as home
import data.classes.views.upload as upload
import data.classes.views.inspector as inspector
import data.classes.views.part_information as part_information
import data.classes.views.spindles as spindles
import data.classes.views.nozzles as nozzles


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
        self.create_frame()
        
        # load views dictionary
        self.load_view_dict()
    
    def create_frame(self):
        # create a frame to hold the views
        self.container = customtkinter.CTkFrame(self)
        # load frame pack
        self.container.pack(fill="both", expand=True)
        
        
    def add_view(self, view, name):
        self.views[name] = view
        
    def load_view(self, name, clear=True):
        # clear the container and state manager current view children
        if clear:
            self.clear_view()
        view = self.views.get(name)
        if view:
            # change the title of the view
            view.load_title(self)
            
            # load the view
            view.load_content()
        else:
            print(f"View {name} not found")
        
    def clear_view(self):    
        # destroy the container
        self.container.destroy()
        
        # re-create the container
        self.create_frame()
        
        # load the views dictionary
        self.load_view_dict()
        
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
            "inspector": inspector.View(master=self.container,state_manager=self.state_manager),
            "part_information": part_information.View(master=self.container,state_manager=self.state_manager),
            "spindles": spindles.View(master=self.container,state_manager=self.state_manager),
            "nozzles": nozzles.View(master=self.container,state_manager=self.state_manager),
        }
        
        
    def destroy(self):
        self.quit()