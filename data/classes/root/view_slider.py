import customtkinter
import data.classes.root.state as state
import os

from PIL import Image, ImageTk
import data.classes.analyse_data.image as img


# views slider class
import data.classes.views.views as views
import data.classes.views.home as home
import data.classes.views.upload as upload
import data.classes.views.inspector as inspector
import data.classes.views.part_information as part_information
import data.classes.views.feeders as feeders
import data.classes.views.spindles as spindles
import data.classes.views.nozzles as nozzles
import data.classes.views.solution_detail as solution_detail


class ViewSlider(customtkinter.CTk):
    def __init__(self, master, title="App",width=800,height=600, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        self.state_manager.set_state("load_solution", self.show_solution)
        self.create_frame()
        
        # load views dictionary
        self.load_view_dict()
    
    
    def create_frame(self):
        # create a frame to hold the views
        self.container = customtkinter.CTkFrame(self)
        # load frame pack
        self.container.pack(fill="both", expand=True)
        return self.container
        
        
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
            "feeders": feeders.View(master=self.container,state_manager=self.state_manager),
            "spindles": spindles.View(master=self.container,state_manager=self.state_manager),
            "nozzles": nozzles.View(master=self.container,state_manager=self.state_manager),
            "solution_detail": solution_detail.View(master=self.container,state_manager=self.state_manager)
        }
        
    def destroy(self):
        self.quit()
        
    def show_solution(self):
        solution = self.state_manager.get_state("current_solution")
        # create sub window using tkinter to show solution
        sub_window = customtkinter.CTkToplevel()
        sub_window.title(solution.get_name())
        sub_window.geometry("700x500")
        # get the solution content
        
        self.solution_content_frame = customtkinter.CTkScrollableFrame(master=sub_window)
        self.solution_content_frame.pack(fill="both", expand=True)
        
        solution_content = solution.content(self.solution_content_frame)
        
        # create a button to check the sub window
        check_button = customtkinter.CTkButton(self.solution_content_frame, text="Check", command=lambda: self.solution_check(sub_window,solution))
        check_button.pack(pady=20)

    def solution_check(self,sub_window,solution):
        # Get the part information
        part_information = self.state_manager.get_state("part_inspected_information")
        # Apply the solution and check if the solution is not already applied
        if solution not in part_information["solutions"]:
            part_information["solutions"].append(solution)
            self.state_manager.set_state("part_inspected_information", {
                "part": part_information["part"],
                "information": part_information["information"],
                "solutions": part_information["solutions"] + [solution.get_id()],
            })

        self.state_manager.get_state("load_view")(name="inspector")
        sub_window.destroy()

        