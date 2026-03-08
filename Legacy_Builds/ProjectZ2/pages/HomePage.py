import customtkinter as ctk
from PIL import Image
from pages.WorkoutType1Page import Workout1Page
from pages.WorkoutType2Page import Workout2Page
from pages.AIEvaluationPage import AIEvaluationPage



class HomePage(ctk.CTkFrame):
    def __init__(self, container, app):
        super().__init__(master = container)
        #this is the key for app.py
        self.app = app

        self.configure(fg_color='#010212')

        #workout type 1 buttons
        self.W1IconPath=Image.open("D:\ProjectPhotos\W1Icon.png")
        self.W1smallIcon = ctk.CTkImage(self.W1IconPath, size=(600,510))
        self.W1MainB = ctk.CTkButton(master=self, text="", command= lambda :self.app.show_page(self.app.show_page(Workout1Page)), hover=True, fg_color="silver", hover_color = 'grey',
                                     border_width=0, font = ("Arial Bold", 24),
                                     text_color="Red", image=self.W1smallIcon)

        #workout type 2 buttons
        self.W2IconPath = Image.open("D:\ProjectPhotos\W2Icon.png")
        self.W2smallIcon = ctk.CTkImage(self.W2IconPath, size=(600,510))
        self.W2MainB = ctk.CTkButton(master=self, text="", command= lambda :self.app.show_page(self.app.show_page(Workout2Page)), hover=True, fg_color="silver", hover_color = 'grey',
                                    border_width=0, font = ("Arial Bold", 24),
                                    text_color="Red", image=self.W2smallIcon)

        #new page
        self.AIBImage=Image.open("D:\ProjectPhotos\AI_Button3.png")
        self.AIBB=ctk.CTkImage(self.AIBImage, size=(280,80))
        self.AIEvaluationButton = ctk.CTkButton(master = self, text= '', font=("Arial Bold", 26),
                                                image =self.AIBB,fg_color="transparent", hover = False, command= lambda: self.app.show_page(AIEvaluationPage),
                                                corner_radius=10, border_width=0 )
        self.AIEvaluationButton.place(x= 500, y= 320)




