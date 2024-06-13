import customtkinter
import data.classes.analyse_data.image as img

class Solution:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.objects = []
        
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def content(self,master):
        # create text with lot of space
        space = " "*50
        # create a label to display the solution name
        solution_name = customtkinter.CTkLabel(master, text=f"{self.name}\n\n",font=("ariel", 23))
        solution_name.pack()
        # loop through the objects and append them to new variable called  
        content_objects = []
        for obj in self.objects:
            if obj.startswith("\img|"):
                # create a label to display the solution image
                # image = self.create_image(master,obj[5:])
                image = img.ImageClass(obj[5:]).create_image(500,300)
                lable_image = customtkinter.CTkLabel(master=master, image=image,text="")
                lable_image.pack()
                content_objects.append(lable_image)
            else:
                # create a label to display the solution description
                
                solution_line = customtkinter.CTkLabel(master, text=f"{obj}",justify="left",wraplength=480,font=("ariel", 20),width=500)
                solution_line.pack()
                content_objects.append(solution_line)
        
        return [solution_name, solution_line, *content_objects]
    
    def create_image(self,master,path):
        image = img.ImageClass(path).create_image(500,300)
        lable_image = customtkinter.CTkLabel(master=master, image=image,text="")
        
        return lable_image