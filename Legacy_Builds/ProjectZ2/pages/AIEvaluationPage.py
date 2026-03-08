from PIL import Image
import customtkinter as ctk

class AIEvaluationPage(ctk.CTkFrame):
    def __init__(self, container, app):
        super().__init__(master=container)
        self.app = app
        self.configure(fg_color='black')

        self.arrow_image = Image.open(r'D:\ProjectPhotos\Back_Button.png')
        self.back_buttoni = ctk.CTkImage(self.arrow_image, size=(25, 25))

        self.return_button = ctk.CTkButton(
            master=self,
            text='',
            image=self.back_buttoni,
            fg_color="transparent",
            hover=False,
            command=self.go_back_home,
            width=25,
        )

        self.return_button.place(x=10, y=10)

    def go_back_home(self):
        from pages.HomePage import HomePage
        self.app.show_page(HomePage)

