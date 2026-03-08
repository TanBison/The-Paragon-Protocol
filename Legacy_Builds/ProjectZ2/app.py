from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.WorkoutStartedPage import WorkoutStartedPage
from pages.HistoryPage import HistoryPage
from pages.WorkoutType1Page import Workout1Page
from pages.WorkoutType2Page import Workout2Page
from pages.WorkoutEvaluationPage import WorkoutEvaluationPage
from pages.AIEvaluationPage import AIEvaluationPage
from backend.workout_logic import WorkoutLogic


import customtkinter as ctk
from CTkToolTip import CTkToolTip
from PIL import Image

class ProjectZ(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.workout_logic = WorkoutLogic(self)
        self.geometry("1280x720")
        self.title("Project Z")
        self.resizable(width=False, height=False)

        # where we are going to show every page
        self.page_container = ctk.CTkFrame(self, fg_color='Black')
        self.page_container.pack(fill="both", expand=True)
        #
        self.workout_started_flagged = False

        self.OptionsFrame = ctk.CTkFrame(self, height=35, width=1260, fg_color='#252531')

        #logout button
        self.LogoutIconPath = Image.open("D:\ProjectPhotos\LogoutIcon.png")
        self.LogoutIcon = ctk.CTkImage(self.LogoutIconPath, size = (24,24))
        self.LogoutB = ctk.CTkButton(master=self.OptionsFrame, text="", image=self.LogoutIcon, command= lambda: self.show_page(LoginPage), fg_color="transparent", hover=False,
                                     corner_radius=0, border_width=0,
                                    width=28, height=28, border_color='Yellow')
        CTkToolTip(self.LogoutB, message = "Logout")
        #home Button
        self.HomeIconPath=Image.open("D:\ProjectPhotos\HomeBIcon2.png")
        self.HomeIcon = ctk.CTkImage(self.HomeIconPath, size = (24,24))
        self.HomeB = ctk.CTkButton(master=self.OptionsFrame, text="", image=self.HomeIcon, command= lambda: self.show_page(HomePage), fg_color="transparent", hover=False,
                                     corner_radius=10, border_width=0,
                                    width=28, height=28, border_color='White')
        CTkToolTip(self.HomeB, message="HomePage")

        #histoy button
        self.HistoryIconPath = Image.open("D:\ProjectPhotos\HistoryBIcon2.png")
        self.HistoryIcon = ctk.CTkImage(self.HistoryIconPath, size = (24,24))
        self.HistoryB = ctk.CTkButton(master=self.OptionsFrame, text="", image=self.HistoryIcon, command= lambda: self.show_page(HistoryPage), fg_color="transparent", hover=False,
                                     corner_radius=10, border_width=0,
                                    width=29, height=29, border_color='White')
        CTkToolTip(self.HistoryB, message="HistoryPage")

        #W1 button
        self.W1IconPath=Image.open("D:\ProjectPhotos\W1Icon.png")
        self.W1smallIcon = ctk.CTkImage(self.W1IconPath, size = (24,24))
        self.W1SmallB = ctk.CTkButton(master=self.OptionsFrame, text="", image=self.W1smallIcon, command= lambda: self.show_page(Workout1Page), fg_color="transparent", hover=False,
                                     corner_radius=10, border_width=0,
                                    width=29, height=29, border_color='White')
        CTkToolTip(self.W1SmallB, message="Workout Type 1")

        #W2 Button
        self.W2IconPath=Image.open("D:\ProjectPhotos\W2Icon.png")
        self.W2smallIcon = ctk.CTkImage(self.W2IconPath, size = (24,24))
        self.W2SmallB = ctk.CTkButton(master=self.OptionsFrame, text="", image=self.W2smallIcon, command= lambda: self.show_page(Workout2Page), fg_color="transparent", hover=False,
                                     corner_radius=10, border_width=0,
                                    width=29, height=29, border_color='White')
        CTkToolTip(self.W2SmallB, message="Workout Type 2")

        #settings button
        self.GearIconPath=Image.open("D:\ProjectPhotos\GearIcon.png")
        self.GearIcon = ctk.CTkImage(self.GearIconPath, size = (24,24))
        self.SettingsButton = ctk.CTkButton(master=self.OptionsFrame, text="", image=self.GearIcon, command= None, fg_color="transparent", hover=False,
                                     corner_radius=10, border_width=0,border_color='Yellow')

        #WorkoutStartedButton
        self.WorkoutSBPath=Image.open("D:\ProjectPhotos\WRunning2.png")
        self.WorkoutRunningIcon=ctk.CTkImage(self.WorkoutSBPath, size=(29,28))
        self.WorkoutRunningB = ctk.CTkButton(master=self.OptionsFrame, text="", image=self.WorkoutRunningIcon, command= lambda: self.show_page(WorkoutStartedPage), fg_color="transparent", hover=False,
                                     corner_radius=10, border_width=1,
                                    width=29, height=29, border_color = 'yellow')
        CTkToolTip(self.WorkoutRunningB, message="Workout Running")

        self.page_button_map = {
            HomePage: self.HomeB,
            HistoryPage: self.HistoryB,
            Workout1Page: self.W1SmallB,
            Workout2Page: self.W2SmallB,
            WorkoutStartedPage: self.WorkoutRunningB
        }
        self.active_page_button = None



        #save all pages (classes) in a dictionary and initialize each page with its master, then it places all of them on top of each other
        self.frames = {}
        for F in (LoginPage, HomePage, Workout1Page, Workout2Page, HistoryPage, WorkoutStartedPage, WorkoutEvaluationPage,  AIEvaluationPage):
            frame = F(container=self.page_container, app=self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)



        print(self.frames)

        self.show_page(HistoryPage)




    # this function is used to make a certain page on top so it appears first
    def show_page(self, page_class):
        if page_class in [LoginPage, AIEvaluationPage]:
            try:
                self.HidePermanentWidgets()
            except:
                None
        else:
            self.PlacePermanentWidgets()

        #wokrout running button
        if page_class == WorkoutStartedPage:
                self.WorkoutRunningB.place(x=1140, y=-1)
        elif page_class == WorkoutEvaluationPage:
            self.workout_started_flagged = False
            self.WorkoutRunningB.place_forget()

        #circle the current page button
        if self.active_page_button is not None:
                self.active_page_button.configure(border_width=0)

        if page_class in self.page_button_map:
            new_button = self.page_button_map[page_class]
            new_button.configure(border_width=2)

            self.active_page_button = new_button
        else:
            self.active_page_button = None

        frame = self.frames[page_class]

        #notice that if u start in the workoutstarted page u wont show the full workout
        if page_class == WorkoutStartedPage:
            if page_class == WorkoutStartedPage:
                if self.workout_started_flagged == False:
                    frame.present_the_current_workout()
                    self.workout_started_flagged = True
        frame.tkraise()

    def terminate_workout(self):
        self.workout_started_flagged = False
        self.WorkoutRunningB.place_forget()
        frame = self.frames[HomePage]

        frame.tkraise()




    # placing the permanent widgest which were initiated before because they are going to be in most of the pages
    def PlacePermanentWidgets(self):
        self.OptionsFrame.place(x=10, y=5)
        self.LogoutB.place(x=5)
        self.HomeB.place(x=105)
        self.HistoryB.place(x=205)
        self.W1SmallB.place(x=305)
        self.W2SmallB.place(x=405)
        self.SettingsButton.place(x=1150)

    #hiding em
    def HidePermanentWidgets(self):
        self.OptionsFrame.place_forget()

    # CUSTOM Message Box
    def show_custom_popup(self, title, message, button_options, icon_type="warning"):
        """
        GLOBAL POPUP: Creates a blocking, dark-themed popup.
        """
        # 1. Create Window
        dialog = ctk.CTkToplevel(self)
        dialog.title(title)
        dialog.geometry("420x240")
        dialog.resizable(False, False)
        dialog.configure(fg_color="#010212")

        # Center the window
        dialog.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - 210
        y = (self.winfo_screenheight() // 2) - 120
        dialog.geometry(f"+{x}+{y}")

        dialog.grab_set()
        dialog.focus_set()

        # 2. Content
        icon_color = "#FF5555" if icon_type == "cancel" else "#FFB74D"
        ctk.CTkLabel(dialog, text=f"⚠ {title.upper()}", font=("Arial Bold", 18), text_color=icon_color).pack(
            pady=(25, 10))
        ctk.CTkLabel(dialog, text=message, font=("Arial", 14), text_color="#dddddd", wraplength=380).pack(pady=(0, 20))

        # 3. Buttons Logic
        user_choice = {"value": None}

        def on_btn_click(choice):
            user_choice["value"] = choice
            dialog.destroy()

        btn_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        btn_frame.pack(fill="x", padx=20, pady=10)

        # Check if we only have ONE button -> Center it
        is_single_button = (len(button_options) == 1)

        for option in button_options:
            if option.lower() in ["cancel", "no", "ok", "understood", "fix it"]:
                fg, hover, txt = "transparent", "#333333", "white"
                border = 1
            else:
                fg, hover, txt = ("#990000", "#FF0000", "white") if icon_type == "cancel" else ("#005577", "#0088AA",
                                                                                                "white")
                border = 0

            btn = ctk.CTkButton(btn_frame, text=option, width=100, height=35,
                                fg_color=fg, hover_color=hover, border_width=border, border_color="gray",
                                text_color=txt,
                                command=lambda opt=option: on_btn_click(opt))

            if is_single_button:
                btn.pack(side="top")  # Centers it because the frame fills X but has no side restrictions
            else:
                # Pack Cancel on Left, Action on Right
                side = "left" if option.lower() in ["cancel", "no"] else "right"
                btn.pack(side=side, padx=10)

        # 4. Wait
        self.wait_window(dialog)
        return user_choice["value"]


