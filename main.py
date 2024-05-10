import customtkinter
from data.classes.root.view_slider import ViewSlider

if __name__ == "__main__":
    view = ViewSlider(customtkinter.CTk(), "App", width=800, height=600)
    
    # load the first view
    view.load_view("upload")
    
    view.mainloop()
    
    