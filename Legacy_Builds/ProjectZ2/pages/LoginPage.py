import customtkinter as ctk
from PIL import Image
from pages.HomePage import HomePage


class LoginPage(ctk.CTkFrame):
    def __init__(self, container, app):
        super().__init__(master = container)
        #this is the key for app.py
        self.app = app


        self.configure(fg_color='Black')
        #first scene
        self.create_account_but = ctk.CTkButton(master=self, width=190, height=40,
                                                text="Create Account", font=("Arial Bold", 24),command= self.create_account_view,
                                                fg_color="#E1E1E1",text_color="#2B2B2B", hover_color="#CCCCCC")
        self.create_account_but.place(x=545, y=340)
        self.login_butt = ctk.CTkButton(master=self, width=193, height=40, text="Login",
                                        font=("Arial Bold", 24),command= self.login_view,fg_color="#E1E1E1",text_color="#2B2B2B", hover_color="#CCCCCC")
        self.login_butt.place(x=545, y=385)

        #login and create account widgets
        self.login_frame = ctk.CTkFrame(master=self, width=400, height=250, fg_color='#2B2B2B',
                                        corner_radius=15)
        self.label1 = ctk.CTkLabel(self.login_frame, text="Email", text_color="#E1E1E1", width=100, height=30,
                                   font=("Arial Bold", 16))
        self.label2 = ctk.CTkLabel(self.login_frame, text="Password", text_color="#E1E1E1", width=100, height=30,
                                   font=("Arial Bold", 16))
        self.email_entry = ctk.CTkEntry(self.login_frame, width=200, height=30, text_color="#2B2B2B")
        self.passwd_entry = ctk.CTkEntry(self.login_frame, width=200, height=30, text_color="#2B2B2B")
        self.login_key = ctk.CTkButton(master=self.login_frame, width=200, height=40, text="Continue",
                                       font=("Arial Bold", 24), command= lambda : self.app.show_page(HomePage), text_color="#2B2B2B",
                                       fg_color="#E1E1E1", hover_color="#CCCCCC")
        self.create_account_but2 = ctk.CTkButton(master=self.login_frame, width=190, height=40,
                                                text="Create Account", font=("Arial Bold", 24),
                                                command=self.create_account_view, fg_color="#E1E1E1",
                                                text_color="#2B2B2B", hover_color="#CCCCCC")
        self.login_butt2 = ctk.CTkButton(master=self.login_frame, width=190, height=40, text="Login",
                                        font=("Arial Bold", 24), command=self.login_view, fg_color="#E1E1E1",
                                        text_color="#2B2B2B", hover_color="#CCCCCC")
        #createaccount specific widgets

        self.label3 = ctk.CTkLabel(self.login_frame, text="Confirm Password", text_color="#E1E1E1", width=100,
                                   height=30, font=("Arial Bold", 14))
        self.reenter_password = ctk.CTkEntry(master=self.login_frame, width=200, height=30)

    def common_factors(self):
        self.login_butt.place_forget()
        self.create_account_but.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.label1.place_forget()
        self.label2.place_forget()
        self.label3.place_forget()
        self.passwd_entry.place_forget()
        self.login_key.place_forget()
        self.create_account_but2.place_forget()
        self.login_butt2.place_forget()
        self.reenter_password.place_forget()


    def login_view(self):
        self.common_factors()
        self.email_entry.place(relx=0.5, rely=0.4, anchor="center")
        self.label1.place(x=22, y=83)
        self.label2.place(x=11, y=121)
        self.passwd_entry.place(relx=0.5, rely=0.55, anchor="center")
        self.login_key.place(relx=0.5, rely=0.8, anchor="center")
        self.create_account_but2.place(x=5, y=5)
        self.login_butt2.place(x=205, y=5)


    def create_account_view(self):
        self.common_factors()
        self.email_entry.place(relx=0.5, rely=0.3, anchor="center")
        self.label1.place(x=22, y=57)
        self.label2.place(x=11, y=96)
        self.passwd_entry.place(relx=0.5, rely=0.45, anchor="center")
        self.login_key.place(relx=0.5, rely=0.8, anchor="center")
        self.create_account_but2.place(x=5, y=5)
        self.login_butt2.place(x=205, y=5)
        self.label3.place(x=7, y=133)
        self.reenter_password.place(relx=0.6, rely=0.6, anchor="center")
