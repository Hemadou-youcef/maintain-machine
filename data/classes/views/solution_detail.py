import customtkinter
import tkinter as tk
from PIL import Image, ImageTk
import os

from data.classes.views.views import ParentView

class View(ParentView):
    def __init__(self, master=None, state_manager=None, *args, **kwargs):
        super().__init__(master, state_manager, title="App", *args, **kwargs)
        self.image_refs = {}  # Dictionary to keep references to images

    def header_content(self):
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=1)

        # Create a button to navigate to the upload view
        back_button = customtkinter.CTkButton(self.master, text="⬅", command=lambda: self.state_manager.get_state("load_view")(name="inspector"))
        # Grid it in the top left corner
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        return [back_button]

    def content(self):
        # Show image of the solution with the solution name and description
        solution = self.state_manager.get_state("current_solution")

        # Create a label to display the solution name
        solution_name = customtkinter.CTkLabel(self.master, text=solution["name"])

        # Create a label to display the solution description
        solution_description = customtkinter.CTkLabel(self.master, text=solution["description"])

        # Create a label to display the solution image
        current_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_path, f"../../{solution['image']}")

        # Check if the image file exists
        if os.path.exists(image_path):
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            # self.solution_image = customtkinter.CTkImage(light_image=self.image, size=(30, 30))
            # solution_image_label = customtkinter.CTkLabel(self.master, text="", image=self.solution_image)
            solution_image_label = tk.Button(self.master, text="", image=photo, compound='top')
            self.image_refs['solution_image'] = photo
        else:
            # Create a label indicating the image could not be found
            solution_image_label = customtkinter.CTkLabel(self.master, text="Image not found")

        # Create submit button for applying the solution
        submit_button = customtkinter.CTkButton(master=self.master, text="Apply Solution", command=lambda: self.submit())

        # Grid the solution name label
        solution_name.grid(row=0, column=0, padx=10, pady=10)
        # Grid the solution description label
        solution_description.grid(row=1, column=0, padx=10, pady=10)
        # Grid the solution image label
        solution_image_label.grid(row=2, column=0, padx=10, pady=10)
        # Grid the submit button
        submit_button.grid(row=3, column=0, padx=10, pady=10)

        return [solution_name, solution_description, solution_image_label, submit_button]

    def submit(self):
        # Get the part information
        part_information = self.state_manager.get_state("part_inspected_information")
        # Get the solution
        solution = self.state_manager.get_state("current_solution")
        # Apply the solution and check if the solution is not already applied
        if solution not in part_information["solution"]:
            part_information["solution"].append(solution)
            self.state_manager.set_state("part_inspected_information", {
                "part": part_information["part"],
                "information": part_information["information"],
                "solution": part_information["solution"] + [solution]
            })

        # Navigate to the inspector view
        self.state_manager.get_state("load_view")(name="inspector")
