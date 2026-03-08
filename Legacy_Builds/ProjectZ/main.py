from PIL import Image
import customtkinter as ctk
from CTkToolTip import CTkToolTip
from WorkoutVids import ViewVid


class ProjectZ(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.resizable(False, False)
        self.configure(fg_color="black")
        self.login_createAccount()
        self.BackArrowPath = Image.open("D:\ImagesFProjeccts\ChatGPT Image Jul 4, 2025, 08_45_26 PM.png")
        self.BackArrow = ctk.CTkImage(self.BackArrowPath)
        self.GearIconPath= Image.open("D:\ProjectPhotos\GearIcon.png")
        self.GearIcon = ctk.CTkImage(self.GearIconPath)
        self.LogoutIconPath= Image.open("D:\ProjectPhotos\LogoutIcon.png")
        self.LogoutIcon = ctk.CTkImage(self.LogoutIconPath)
        self.current_page = None
        self.FlagOfRetrieval = 0
        self.FirstTime = 0
        self.current_exercise_index = 0
        self.checkboxes_order=[]
        self.saved_selection_order=[]
        self.saved_type_order=[]
        self.RetrievalIndex=0
        self.SavingIndex=0
        self.MainPageFlag=0
        self.IsSaving=False
        self.reps_index=0
        self.times_index=0
        self.rest_timer_id = None
        self.remaining_seconds = 0
        self.timer_paused = False
        self.reps_done=[]
        self.time_done=[]
        self.setNOindex=0
        self.setNOflag=False
        self.current_exercise_index_flag= False
        self.junk_flag=False
        self.current_timed_exercise_index=0
        self.iterationstimesflag=0
        self.iterationstimesflag2=0
        self.current_exercise_index2=0
        self.VidsList=[]


        self.saved_data = {
            'pulling': { 'exercises':[],
                'exercise_sets': [], 'exercise_reps': [[]], 'exercise_times':[[]], 'exercise_rest_times': [], 'exercise_checkbox_states': [],
                         'Type': []
            },
            'pushing': { 'exercises':[],
                'exercise_sets': [], 'exercise_reps': [[]], 'exercise_times': [[]], 'exercise_rest_times': [], 'exercise_checkbox_states': [],
                         'Type': []
            },
            'legs': { 'exercises':[],
                'exercise_sets': [], 'exercise_reps': [[]], 'exercise_times': [[]], 'exercise_rest_times': [], 'exercise_checkbox_states': [],
                      'Type': []
            },
            'abs': { 'exercises':[],
                'exercise_sets': [], 'exercise_reps': [[]], 'exercise_times': [[]], 'exercise_rest_times': [], 'exercise_checkbox_states': [],
                     'Type': []
            }
        }


    def login_createAccount(self):
        self.main_frame = ctk.CTkFrame(self, fg_color="black")
        self.main_frame.pack(fill="both", expand=True)
        self.login_frame = ctk.CTkFrame(master=self.main_frame, width=400, height=250, fg_color='#2B2B2B',
                                        corner_radius=15)
        def login_command():
            for widget in self.login_frame.winfo_children():
                widget.destroy()
            self.login_butt.destroy()
            self.create_account_but.destroy()

            self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
            self.label1 = ctk.CTkLabel(self.login_frame, text="Email", text_color="#E1E1E1", width=100, height=30,
                                       font=("Arial Bold", 16))
            self.label1.place(x=22, y=83)
            self.label2 = ctk.CTkLabel(self.login_frame, text="Password", text_color="#E1E1E1", width=100, height=30,
                                       font=("Arial Bold", 16))
            self.label2.place(x=11, y=121)
            self.email_entry = ctk.CTkEntry(self.login_frame, width=200, height=30,text_color="#2B2B2B")
            self.email_entry.place(relx=0.5, rely=0.4, anchor="center")
            self.passwd_entry = ctk.CTkEntry(self.login_frame, width=200, height=30,text_color="#2B2B2B")
            self.passwd_entry.place(relx=0.5, rely=0.55, anchor="center")
            self.login_key = ctk.CTkButton(master=self.login_frame, width=200, height=40, text="Continue",
                                           font=("Arial Bold", 24),command=self.MainPage,text_color="#2B2B2B",fg_color="#E1E1E1", hover_color="#CCCCCC")
            self.login_key.place(relx=0.5, rely=0.8, anchor="center")
            self.create_account_but = ctk.CTkButton(master=self.login_frame, width=190, height=40,
                                                    text="Create Account", font=("Arial Bold", 24),
                                                    command=CreateAccount_command, fg_color="#E1E1E1",
                                                    text_color="#2B2B2B", hover_color="#CCCCCC")
            self.create_account_but.place(x=5, y=5)
            self.login_butt = ctk.CTkButton(master=self.login_frame, width=190, height=40, text="Login",
                                            font=("Arial Bold", 24), command=login_command, fg_color="#E1E1E1",
                                            text_color="#2B2B2B", hover_color="#CCCCCC")
            self.login_butt.place(x=205, y=5)

        def CreateAccount_command():

            for widget in self.login_frame.winfo_children():
                widget.destroy()
            self.login_butt.destroy()
            self.create_account_but.destroy()

            self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
            self.label1 = ctk.CTkLabel(self.login_frame, text="Email", text_color="#E1E1E1", width=100, height=30,
                                       font=("Arial Bold", 16))
            self.label1.place(x=22, y=57)
            self.label2 = ctk.CTkLabel(self.login_frame, text="Password", text_color="#E1E1E1", width=100, height=30,
                                       font=("Arial", 16))
            self.label2.place(x=11, y=96)
            self.label3=ctk.CTkLabel(self.login_frame, text="Confirm Password", text_color="#E1E1E1", width=100, height=30,font=("Arial Bold", 14))
            self.label3.place(x=7, y=133)
            self.email_entry = ctk.CTkEntry(self.login_frame, width=200, height=30)
            self.email_entry.place(relx=0.5, rely=0.3, anchor="center")
            self.passwd_entry = ctk.CTkEntry(self.login_frame, width=200, height=30)
            self.passwd_entry.place(relx=0.5, rely=0.45, anchor="center")
            self.reenter_password=ctk.CTkEntry(master=self.login_frame, width=200, height=30)
            self.reenter_password.place(relx=0.6, rely=0.6, anchor="center")

            self.login_key = ctk.CTkButton(master=self.login_frame, width=200, height=40, text="Continue",
                                           font=("Arial Bold", 24),command=self.MainPage,text_color="#2B2B2B",fg_color="#E1E1E1", hover_color="#CCCCCC")
            self.login_key.place(relx=0.5, rely=0.8, anchor="center")
            self.create_account_but = ctk.CTkButton(master=self.login_frame, width=190, height=40,
                                                    text="Create Account", font=("Arial Bold", 24),
                                                    command=CreateAccount_command, fg_color="#E1E1E1",
                                                    text_color="#2B2B2B", hover_color="#CCCCCC")
            self.create_account_but.place(x=5, y=5)
            self.login_butt = ctk.CTkButton(master=self.login_frame, width=190, height=40, text="Login",
                                            font=("Arial Bold", 24), command=login_command, fg_color="#E1E1E1",
                                            text_color="#2B2B2B", hover_color="#CCCCCC")
            self.login_butt.place(x=205, y=5)

        self.create_account_but = ctk.CTkButton(master=self, width=190, height=40,
                                                text="Create Account", font=("Arial Bold", 24),command=CreateAccount_command, fg_color="#E1E1E1",text_color="#2B2B2B", hover_color="#CCCCCC")
        self.create_account_but.place(x=545, y=340)
        self.login_butt = ctk.CTkButton(master=self, width=193, height=40, text="Login",
                                        font=("Arial Bold", 24),command=login_command,fg_color="#E1E1E1",text_color="#2B2B2B", hover_color="#CCCCCC")
        self.login_butt.place(x=545, y=385)


    def MainPage(self):
        self.MainPageFlag=1
        self.saved_selection_order = []
        self.saved_type_order = []
        self.checkboxes_order = []
        self.current_exercise_index = 0
        if self.MainPageFlag == 1:
            self.saved_data = {
                'pulling': {'exercises': [],
                            'exercise_sets': [], 'exercise_reps': [[]], 'exercise_times': [[]], 'exercise_rest_times': [],
                            'exercise_checkbox_states': [],
                            'Type': []
                            },
                'pushing': {'exercises': [],
                            'exercise_sets': [], 'exercise_reps': [[]], 'exercise_times': [[]], 'exercise_rest_times': [],
                            'exercise_checkbox_states': [],
                            'Type': []
                            },
                'legs': {'exercises': [],
                         'exercise_sets': [], 'exercise_reps': [[]], 'exercise_times': [[]], 'exercise_rest_times': [],
                         'exercise_checkbox_states': [],
                         'Type': []
                         },
                'abs': {'exercises': [],
                        'exercise_sets': [], 'exercise_reps': [[]], 'exercise_times': [[]], 'exercise_rest_times': [],
                        'exercise_checkbox_states': [],
                        'Type': []
                        }
            }

        for winfo in self.winfo_children():
            winfo.destroy()

        def MakeSureWindow():
            self.SmallWindow=ctk.CTkToplevel(self.MainPage(), height=400, width=400)
            self.SmallWindow.resizable(False, False)
            MakeSureLabel=ctk.CTkLabel(self.SmallWindow, text="Are you sure to logout?", font=("Arial Bold", 22))
            MakeSureLabel.place(x=30, rely=0.4)

            def Cancelfunction():
                 for winfo in self.SmallWindow.winfo_children():
                     winfo.destroy()
                 self.SmallWindow.destroy()
            def Yesfunction():
                 for winfo in self.SmallWindow.winfo_children():
                     winfo.destroy()
                 self.SmallWindow.destroy()
                 self.login_createAccount()

            YesB=ctk.CTkButton(master=self.SmallWindow, command=Yesfunction, text="Yes", font=("Arial Bold", 22))
            YesB.place(x=10, y=250)
            CancelB=ctk.CTkButton(master=self.SmallWindow, command=Cancelfunction, text="Cancel", font=("Arial Bold", 22))
            CancelB.place(x=170, y=250)

        self.OptionsFrame= ctk.CTkFrame(self, height=30, width=1260)
        self.OptionsFrame.place(x=10, y=10)
        self.LogoutB= ctk.CTkButton(master=self.OptionsFrame, text="", image=self.LogoutIcon, command=MakeSureWindow, fg_color="transparent", hover=False, corner_radius=0, border_width=0,
                                    width=28, height=28)
        self.LogoutB.place(x=5)
        CTkToolTip(self.LogoutB, message="Logout", delay= 0.3)
        self.PullingB = ctk.CTkButton(self, height=325, width=625, command=self.PullingPage, text="Pulling", font=("Arial Bold", 24), fg_color="#E1E1E1", text_color="#2B2B2B", hover_color="#CCCCCC")
        self.PullingB.place(x=10, y=50)
        self.PushingB = ctk.CTkButton(self, height=325, width=625, command=self.PushingPage, text="Pushing", font=("Arial Bold", 24), fg_color="#E1E1E1", text_color="#2B2B2B", hover_color="#CCCCCC")
        self.PushingB.place(x=645, y=50)
        self.LegsB = ctk.CTkButton(self, height=325, width=625, command=self.LegsPage, text="Legs", font=("Arial Bold", 24), fg_color="#E1E1E1", text_color="#2B2B2B", hover_color="#CCCCCC")
        self.LegsB.place(x=10, y=385)
        self.AbsB = ctk.CTkButton(self, height=325, width=625, command=self.AbsPage, text="Abs", font=("Arial Bold", 24), fg_color="#E1E1E1", text_color="#2B2B2B", hover_color="#CCCCCC")
        self.AbsB.place(x=645, y=385)

    def PullingPage(self):
        self.MainPageFlag = 0
        self.current_page = self.PullingPage
        self.current_page_name = 'pulling'
        self.ClearPage()
        self.ReturnBack(self.MainPage)

        Exercises = ["Pull Ups",
                     "Chin Ups",
                     "Rows",
                     "Archer Pullups",
                     "Weighted Pullups",
                     "OneArm Pullups",
                     ]
        TimedExercises = ["Dead Hangs"]

        self.CreateExercisesPages(Exercises, TimedExercises)
        self.StartWorkout(self.ExercisesFrame1)

    def PushingPage(self):
        self.MainPageFlag = 0
        self.current_page = self.PushingPage
        self.current_page_name = 'pushing'
        self.ClearPage()
        self.ReturnBack(self.MainPage)

        Exercises = ["Push ups",
                     "Diamond Pushups",
                     "Inclined Pushups",
                     "Declined Pushups",
                     "Weighted Pushups",
                     "OneArm Pushups",
                     "Pike Pushups",
                     "Advanced Pike Pushups",
                     "HandStand Pushups",
                     "Archer Pushups"
                     ]
        TimedExercises = ["Handstand Hold",
                          "StraightArm Plank Hold",
                          "Pike Position Hold"]

        self.CreateExercisesPages(Exercises, TimedExercises)
        self.StartWorkout(self.ExercisesFrame1)

    def LegsPage(self):
        self.MainPageFlag = 0
        self.current_page = self.LegsPage
        self.current_page_name = 'legs'
        self.ClearPage()
        self.ReturnBack(self.MainPage)
        Exercises = ["BW Squats",
                     "BW Lunges",
                     "Weighted Squats",
                     "Weighted Lunges",
                     "Pistol Squats"
                     ]

        self.CreateExercisesPages(Exercises, [])
        self.StartWorkout(self.ExercisesFrame1)

    def AbsPage(self):
        self.MainPageFlag = 0
        self.current_page = self.AbsPage
        self.current_page_name = 'abs'
        self.ClearPage()
        self.ReturnBack(self.MainPage)
        Exercises = ["Hanging Knee Raises",
                     "Sit Ups",
                     "Toes To Bar",
                     ]
        TimedExercises = ["L-Sit",
                          "Plank",
                          "Flutter Kicks",
                          "Bicycle Kicks",
                          "Dragon Flag"]
        self.CreateExercisesPages(Exercises, TimedExercises)
        self.StartWorkout(self.ExercisesFrame1)

    def ReturnBack(self, page):
        self.current_exercise_index=0
        self.setNOindex=0
        self.current_timed_exercise_index=0
        self.current_exercise_index2=0
        self.VidsList = []
        self.setNOflag= False
        self.junk_flag=False
        self.ReturnArrow = ctk.CTkButton(self, width=0, height=0, image=self.BackArrow, fg_color="transparent", text="",
                                         hover_color="black"
                                         , border_width=0, command=page)

        self.ReturnArrow.place(x=5, y=5)

        if self.FlagOfRetrieval == 1:
            self.FlagOfRetrieval = 0

    def ExercisePages(self, exercises):
        self.MainPageFlag = 0
        ExercisesFrame1 = ctk.CTkFrame(self, width=1200, height=680)
        ExercisesFrame1.place(x=40, y=20)
        ScrollableFrame1 = ctk.CTkScrollableFrame(ExercisesFrame1, width=1150, height=655)
        ScrollableFrame1.place(x=30, y=15)

    def ClearPage(self):
        for widget in self.winfo_children():
            widget.destroy()

    def CreateExercisesPages(self, Exercises, TimedExercises):
        ###page Layout
        self.ExercisesFrame1 = ctk.CTkFrame(self, width=1200, height=680)
        self.ExercisesFrame1.place(x=40, y=20)
        ScrollableFrame1 = ctk.CTkScrollableFrame(self.ExercisesFrame1, width=1140, height=580)
        ScrollableFrame1.place(x=20, y=50)
        TextFrame1 = ctk.CTkFrame(self.ExercisesFrame1)
        TextFrame1.place(x=490, y=7)
        Label1 = ctk.CTkLabel(TextFrame1, text="Available Exercises", font=("Arial", 22))
        Label1.pack(padx=5, pady=5)

        self.Exercises = {"Names": Exercises+TimedExercises, "Type":[], "CheckBoxes": [], "Frames": [],
                          "RepsLabel": [], "RepsEntry": [], "SetsLabel": [], "SetsEntry": [], "TimeLabel": [],
                          "TimeEntry": [], "RestLabel": [], "RestEntry": [],
                          "Sets": [], "Reps": [[]],"Rest":[], "Time": [[]], "CheckBox_Status": [], "NewCheckBoxes": [], "ConfirmSetsButton":[]}
        self.ConfirmedSets=[]

        for exercise in Exercises:
            self.Exercises["Type"].append("regular")
        for exercise in TimedExercises:
            self.Exercises["Type"].append("timed")



        ###Create Frames and CheckBoxes inside the frame for all exercises.
        for name in self.Exercises["Names"]:
            frames = ctk.CTkFrame(ScrollableFrame1)
            frames.pack(padx=5, pady=5, anchor="w")
            options = ctk.CTkCheckBox(frames, text=name, font=("Arial", 22), command= self.ShowOnSelect())
            options.pack(padx=5, pady=5, anchor="w")
            self.Exercises["CheckBoxes"].append(options)
            self.Exercises["Frames"].append(frames)


        ###Create labels and entries in each frame
        for i, widget in enumerate(self.Exercises["Frames"]):
            self.setlabel = ctk.CTkLabel(widget, text="Sets", font=("Arial", 18))
            self.setentry = ctk.CTkEntry(widget)
            self.ConfirmSetsB= ctk.CTkButton(widget, text="Confirm Sets", font=("Arial", 18))
            self.restlabel = ctk.CTkLabel(widget, text="Rest", font=("Arial", 18))
            self.restsentry = ctk.CTkEntry(widget)

            ###create and dont show yet reps labels and entries not timed ones. Goal:- create labels and entries based on the number of sets
            ### the code used to be here
            ###save other widgets
            self.Exercises["SetsLabel"].append(self.setlabel)
            self.Exercises["SetsEntry"].append(self.setentry)
            self.Exercises["RestLabel"].append(self.restlabel)
            self.Exercises["RestEntry"].append(self.restsentry)
            self.Exercises["ConfirmSetsButton"].append(self.ConfirmSetsB)

        """self.RetrieveEntries()"""


    def ShowOnSelect(self):

        ##save the order of selection and type of exercises in order
        for i, checkbox in enumerate(self.Exercises["CheckBoxes"]):
            if checkbox.get() == 1:
                if checkbox.cget("text") not in self.saved_selection_order:
                    self.saved_selection_order.append(checkbox.cget("text"))
                    self.saved_type_order.append(self.Exercises["Type"][i])


            else:
                if checkbox.cget("text") in self.saved_selection_order:
                    self.saved_selection_order.remove(checkbox.cget("text"))
                    self.saved_type_order.remove(self.Exercises["Type"][i])

        #loadwidgets
        for i, widget in enumerate(self.Exercises["CheckBoxes"]):
            setlabel = self.Exercises["SetsLabel"][i]
            setentry = self.Exercises["SetsEntry"][i]

            restlabel = self.Exercises["RestLabel"][i]
            restentry = self.Exercises["RestEntry"][i]
            confirmsets = self.Exercises["ConfirmSetsButton"][i]
            ###show when checked

            if widget.get() == 1 and self.Exercises["Type"][i] == "regular":
                setlabel.pack(padx=5, pady=5, anchor="w", side="left")
                setentry.pack(padx=1, pady=5, anchor="w", side="left")

                confirmsets.pack(padx=5, pady=5, anchor="w", side="left")

                restlabel.pack(padx=5, pady=5, anchor="w", side="left")
                restentry.pack(padx=1, pady=5, anchor="w", side="left")

            elif widget.get() == 1 and self.Exercises["Type"][i] == "timed":
                setlabel.pack(padx=5, pady=5, anchor="w", side="left")
                setentry.pack(padx=1, pady=5, anchor="w", side="left")

                confirmsets.pack(padx=5, pady=5, anchor="w", side="left")

                restlabel.pack(padx=5, pady=5, anchor="w", side="left")
                restentry.pack(padx=1, pady=5, anchor="w", side="left")

    def ShowBasedWidgets(self):
        for i, status in enumerate(self.Exercises["CheckBox_Status"]):
            if self.Exercises["CheckBox_Status"][i] == 1:
                self.ConfirmedSets.append(self.Exercises["SetsEntry"][i].cget("text"))
                if self.Exercises["Type"][i] == "regular":
                    self.repslabel = ctk.CTkLabel(self.Exercises["Frames"][i], text="Reps", font=("Arial", 18))
                    self.repsentry = ctk.CTkEntry(self.Exercises["Frames"][i])
                    self.timelabel = None
                    self.timeentry = None
                    self.Exercises["RepsLabel"].append(self.repslabel)
                    self.Exercises["RepsEntry"].append(self.repsentry)


                else:
                    self.timelabel = ctk.CTkLabel(self.Exercises["Frames"][i], text="Exercise Time", font=("Arial", 18))
                    self.timeentry = ctk.CTkEntry(self.Exercises["Frames"][i])
                    self.repslabel = None
                    self.repsentry = None
                    self.Exercises["TimeLabel"].append(self.timelabel)
                    self.Exercises["TimeEntry"].append(self.timeentry)


    def StartWorkout(self, frame):
        StartWorkout_Button = ctk.CTkButton(frame, width=200, height=30, text="Start Workout", fg_color="green",
                                            command= None)
        StartWorkout_Button.place(x=500, y=645)

    def WorkoutStartedPage(self):
        self.ConfirmedSets.clear()
        self.reps_done.clear()
        self.time_done.clear()
        current_data = self.saved_data[self.current_page_name]
        self.MainPageFlag = 0
        self.SaveEntries()
        self.FlagOfRetrieval = 1
        self.ClearPage()
        self.ReturnBack(self.current_page)
        setNO = [[] for i in current_data['exercises']]

        WorkoutFrame = ctk.CTkFrame(master=self, width=600, height=300)
        WorkoutFrame.place(x=10, y=30)
        WorkoutFrame.pack_propagate(False)

        VideoFrame = ctk.CTkFrame(master=self, width=650, height=640)
        VideoFrame.place(x=620, y=30)

        RestFrame = ctk.CTkFrame(master=self, width=600, height=180)
        RestFrame.place(x=10, y=340)
        RestFrame.pack_propagate(False)
        current_data = self.saved_data[self.current_page_name]


        def UpdateBelowButton():
            print("current exercise index: ", self.current_exercise_index)
            print("setNOindex : ", self.setNOindex)
            if hasattr(self, 'ProceedButton'):
                self.ProceedButton.destroy()
            if hasattr(self, 'TerminateButton'):
                self.TerminateButton.destroy()

            if self.current_exercise_index == len(current_data['exercises']) and self.setNOindex  == 0:
                self.ProceedButton = ctk.CTkButton(master=self, width=250, height=35, fg_color="green",
                                              text="Proceed To Evaluation",
                                              font=("Arial", 18))
                self.ProceedButton.place(x=515, y=680)
            else:
                self.TerminateButton = ctk.CTkButton(master=self, width=250, height=35, fg_color="red",
                                                text="Terminate Early",
                                                font=("Arial", 18))
                self.TerminateButton.place(x=515, y=680)

        def UpdateRestFrame():
            if self.current_exercise_index < len(current_data['exercises']):
                rest_time = int(current_data['exercise_rest_times'][self.current_exercise_index])
                formatted_time = format_time(rest_time)
                time_label.configure(text=formatted_time)

        def format_time(seconds):
            minutes = seconds // 60
            remaining_seconds = seconds % 60
            return f"{minutes:02d}:{remaining_seconds:02d}"

        def InitializeRestFrame():
            for widget in RestFrame.winfo_children():
                widget.destroy()
            if len(current_data['exercises']) > 0:
                global new_frame1
                new_frame1 = ctk.CTkFrame(master=RestFrame)
                new_frame1.pack(padx=5, pady=5, fill='both', expand='yes')
                new_label = ctk.CTkLabel(master=new_frame1, font=("Arial", 24), text="Timer")
                new_label.pack(padx=(0, 5), pady=5, side='top', anchor='center')
                rest_time = int(current_data['exercise_rest_times'][0])
                global time_label
                formatted_time = format_time(rest_time)
                time_label = ctk.CTkLabel(master=new_frame1, font=("Arial", 24), text=formatted_time)
                time_label.pack(padx=5, anchor="center")

        InitializeRestFrame()

        def IterateOverExercises():
            if self.current_exercise_index < len(current_data['exercises']) - 1:
                self.current_exercise_index += 1
                self.display_current_exercise(WorkoutFrame, current_data)
                UpdateRestFrame()

        def ReturnOverExercises():
            if self.current_exercise_index > 0:
                self.current_exercise_index -= 1
                self.display_current_exercise(WorkoutFrame, current_data)
                UpdateRestFrame()

        self.current_exercise_index = 0
        self.display_current_exercise(WorkoutFrame, current_data)

        self.next_exercise = ctk.CTkButton(master=WorkoutFrame, fg_color="green", text="Next Exercise",
                                           font=("Arial", 18),
                                           command=IterateOverExercises, width=200, height=25)
        self.prev_exercise = ctk.CTkButton(master=WorkoutFrame, fg_color="green", text="Prev Exercise",
                                           font=("Arial", 18),
                                           command=ReturnOverExercises, width=200, height=25)
        self.prev_exercise.pack(padx=5, pady=5, anchor="center", side="bottom")
        self.next_exercise.pack(padx=5, pady=5, anchor="center", side="bottom")

        def BeginTheWork():
            if self.junk_flag==False:
                self.current_exercise_index = 0
                self.junk_flag = True

            UpdateBelowButton()
            current_data = self.saved_data[self.current_page_name]

            for winfo in WorkoutFrame.winfo_children():
                winfo.destroy()
                if hasattr(self, 'theseframes'):
                    self.theseframes.destroy()
                    delattr(self, 'theseframes')
                if hasattr(self, 'finishedlabel'):
                    self.finishedlabel.destroy()
                    delattr(self, 'finishedlabel')
            WorkoutFrame.update()


            if self.current_exercise_index >= len(current_data['exercises']):
                new_frame = ctk.CTkFrame(master=WorkoutFrame)
                new_frame.pack(padx=5, pady=5, fill='both', expand='yes')
                DoneLabel = ctk.CTkLabel(master=new_frame, font=("Arial", 26),
                                         text="Workout Done, Proceed to save workout if you wish.")
                DoneLabel.pack(padx=5, pady=5, anchor="w")
                if self.current_exercise_index == len(current_data['exercises']) and self.setNOindex == len(
                        setNO[self.current_exercise_index]):
                    ProceedButton = ctk.CTkButton(master=self, width=250, height=35, fg_color="green",
                                                  text="Proceed To Evaluation",
                                                  font=("Arial", 18))
                    ProceedButton.place(x=515, y=680)
                else:
                    TerminateButton = ctk.CTkButton(master=self, width=250, height=35, fg_color="red",
                                                    text="Terminate Early",
                                                    font=("Arial", 18))
                    TerminateButton.place(x=515, y=680)
                return

            if self.current_exercise_index < len(current_data['exercises']):
                new_frame = ctk.CTkFrame(master=WorkoutFrame)
                new_frame.pack(padx=5, pady=5, fill='both', expand='yes')

                if self.current_exercise_index < len(setNO):
                    if not setNO[self.current_exercise_index]:
                        for i in range(1, int(''.join(
                                c for c in str(current_data['exercise_sets'][self.current_exercise_index] or '0') if
                                c.isdigit())) + 1):
                            setNO[self.current_exercise_index].append(i)

                print("setNO :-  ", setNO)

                if self.setNOindex < len(setNO[self.current_exercise_index]):
                    SetNumber = ctk.CTkLabel(master=new_frame,
                                             text=f"Set Number: {setNO[self.current_exercise_index][self.setNOindex]}",
                                             font=("Arial", 24))
                    exercise = (current_data['exercises'][self.current_exercise_index])
                    new_label = ctk.CTkLabel(master=new_frame, font=("Arial", 24), text=exercise)
                    new_label.pack(padx=5, pady=5, anchor="w")

                    SetNumber.pack(padx=5, pady=5, anchor="w")
                    self.setNOindex += 1
                    UpdateBelowButton()
                elif self.setNOindex >= len(setNO[self.current_exercise_index]):
                    self.setNOindex = 0
                    if self.setNOindex == 0:
                        self.current_exercise_index += 1
                    UpdateBelowButton()

                    if self.current_exercise_index >= len(current_data['exercises']):
                        DoneLabel = ctk.CTkLabel(master=new_frame, font=("Arial", 26),
                                                 text="Workout Done, Proceed to save workout if you wish.")
                        DoneLabel.pack(padx=5, pady=5, anchor="w")
                        return

                    if self.current_exercise_index < len(setNO):
                        if not setNO[self.current_exercise_index]:
                            for i in range(1, int(''.join(
                                    c for c in str(current_data['exercise_sets'][self.current_exercise_index] or '0') if
                                    c.isdigit())) + 1):
                                setNO[self.current_exercise_index].append(i)

                    if (self.current_exercise_index < len(setNO) and
                            self.setNOindex < len(setNO[self.current_exercise_index])):
                        SetNumber = ctk.CTkLabel(master=new_frame,
                                                 text=f"Set Number: {setNO[self.current_exercise_index][self.setNOindex]}",
                                                 font=("Arial", 24))
                        exercise = (current_data['exercises'][self.current_exercise_index])
                        new_label = ctk.CTkLabel(master=new_frame, font=("Arial", 24), text=exercise)
                        new_label.pack(padx=5, pady=5, anchor="w")

                        SetNumber.pack(padx=5, pady=5, anchor="w")
                        self.setNOindex += 1
                        UpdateBelowButton()

                if self.current_exercise_index < len(current_data['exercises']):
                    exercise_type = self.saved_type_order[self.current_exercise_index]
                    if exercise_type == "regular":
                        self.iterationstimesflag2 += 1
                        if self.iterationstimesflag > int(current_data['exercise_sets'][self.current_exercise_index]):
                            self.current_exercise_index2 += 1
                            self.iterationstimesflag2=0
                        self.TargetReps = ctk.CTkLabel(master=new_frame,
                                                       text=f"Target Reps: {current_data['exercise_reps'][self.current_exercise_index2]}",
                                                       font=("Arial", 24))
                        self.TargetReps.pack(padx=5, pady=5, anchor="w")

                        self.TargetRest = ctk.CTkLabel(master=new_frame,
                                                       text=f"Target Rest: {current_data['exercise_rest_times'][self.current_exercise_index]}",
                                                       font=("Arial", 24))
                        self.TargetRest.pack(padx=5, pady=5, anchor="w")

                        self.RepsLabel = ctk.CTkLabel(master=new_frame, text="Repetitions Done:", font=("Arial", 24))
                        self.RepsLabel.pack(side="left", padx=(0, 5), pady=5)

                        self.RepsDoneE = ctk.CTkEntry(master=new_frame, placeholder_text="Number", font=("Arial", 18))
                        self.RepsDoneE.pack(side="left")
                    elif exercise_type == "timed":
                        self.iterationstimesflag += 1
                        if self.iterationstimesflag > int(current_data['exercise_sets'][self.current_exercise_index]):
                            self.current_timed_exercise_index += 1
                            self.iterationstimesflag=0
                        TargetTime = ctk.CTkLabel(master=new_frame,
                                                  text=f"Target Time: {current_data['exercise_times'][self.current_timed_exercise_index]}",
                                                  font=("Arial", 24))
                        TargetTime.pack(padx=5, pady=5, anchor="w")


                        self.TargetRest = ctk.CTkLabel(master=new_frame,
                                                       text=f"Target Rest: {current_data['exercise_rest_times'][self.current_exercise_index]}",
                                                       font=("Arial", 24))
                        self.TargetRest.pack(padx=5, pady=5, anchor="w")

                        self.TimeLabel = ctk.CTkLabel(master=new_frame, text="Time Done:", font=("Arial", 24))
                        self.TimeLabel.pack(side="left", padx=(0, 5), pady=5)

                        self.TimeDoneE = ctk.CTkEntry(master=new_frame, placeholder_text="Number", font=("Arial", 18))
                        self.TimeDoneE.pack(side="left")


                def BeginTheRest():
                    if self.current_exercise_index < len(current_data['exercises']):
                        exercise_type = self.saved_type_order[self.current_exercise_index]
                        if exercise_type == "regular":
                            reps_done = self.RepsDoneE.get()
                            self.reps_done.append(reps_done)
                            self.time_done.append('')
                        elif exercise_type == "timed":
                            time_done = self.TimeDoneE.get()
                            self.time_done.append(time_done)
                            self.reps_done.append('')

                        global new_frame1
                        global resume_button
                        global pause_button
                        global reset_button

                        for widget in new_frame1.winfo_children():
                            if isinstance(widget, ctk.CTkFrame) and widget.cget('fg_color') == 'transparent':
                                widget.destroy()

                        rest_time = int(current_data['exercise_rest_times'][self.current_exercise_index])
                        start_rest_timer(rest_time)
                        pause_image = ctk.CTkImage(
                            Image.open("D:\ImagesFProjeccts\ChatGPT Image Aug 5, 2025, 02_52_52 PM.png"), size=(30, 30))
                        resume_image = ctk.CTkImage(
                            Image.open("D:\ImagesFProjeccts\ChatGPT Image Aug 5, 2025, 02_53_42 PM.png"), size=(30, 30))
                        reset_image = ctk.CTkImage(
                            Image.open("D:\ImagesFProjeccts\ChatGPT Image Aug 5, 2025, 02_53_52 PM.png"), size=(30, 30))

                        button_container = ctk.CTkFrame(master=new_frame1, fg_color='transparent')
                        button_container.pack(padx=5, anchor="center", pady=5)

                        pause_button = ctk.CTkButton(master=button_container, image=pause_image, text="",
                                                     fg_color='transparent', border_width=0, hover_color='grey',
                                                     width=30, height=30, command=pause_time)
                        pause_button.pack(padx=5, side='left')

                        resume_button = ctk.CTkButton(master=button_container, image=resume_image, text="",
                                                      fg_color='transparent', border_width=0, hover_color='grey',
                                                      width=30, height=30, command=resume_time)

                        reset_button = ctk.CTkButton(master=button_container, image=reset_image, text="",
                                                     fg_color='transparent', border_width=0, hover_color='grey',
                                                     width=30, height=30, command=reset_time)
                        reset_button.pack(padx=5, side='left')

                        skip_rest = ctk.CTkButton(master=button_container, text="Skip Rest -->", command=skip_time)
                        skip_rest.pack(pady=5, padx=5)

                        self.StartRest.pack_forget()
                        if exercise_type == "regular":
                            self.RepsLabel.pack_forget()
                            self.RepsDoneE.pack_forget()
                        elif exercise_type == "timed":
                            self.TimeLabel.pack_forget()
                            self.TimeDoneE.pack_forget()

                        print("Reps Done: ", self.reps_done)
                        print("Time Done: ", self.time_done)

                def start_rest_timer(seconds):
                    self.remaining_seconds = seconds
                    self.timer_paused = False
                    count_down()

                def count_down():
                    if self.remaining_seconds > -1 and not self.timer_paused:
                        formatted_time = format_time(self.remaining_seconds)
                        time_label.configure(text=formatted_time)
                        self.remaining_seconds -= 1
                        self.rest_timer_id = RestFrame.after(1000, count_down)
                    elif self.remaining_seconds <= 0:
                        BeginTheWork()

                def pause_time():
                    self.timer_paused = True
                    if self.rest_timer_id:
                        RestFrame.after_cancel(self.rest_timer_id)
                        self.rest_timer_id = None
                    global resume_button
                    global pause_button
                    global reset_button
                    reset_button.pack_forget()
                    pause_button.pack_forget()
                    resume_button.pack(padx=5, side='left')
                    reset_button.pack(padx=5, side='left')

                def resume_time():
                    self.timer_paused = False
                    count_down()
                    global resume_button
                    global pause_button
                    global reset_button
                    reset_button.pack_forget()
                    resume_button.pack_forget()
                    pause_button.pack(padx=5, side='left')
                    reset_button.pack(padx=5, side='left')

                def reset_time():
                    if self.rest_timer_id:
                        RestFrame.after_cancel(self.rest_timer_id)
                        self.rest_timer_id = None

                    self.timer_paused = False
                    if self.current_exercise_index < len(current_data['exercises']):
                        self.remaining_seconds = int(current_data['exercise_rest_times'][self.current_exercise_index])
                        formatted_time = format_time(self.remaining_seconds)
                        time_label.configure(text=formatted_time)
                    global resume_button
                    global pause_button
                    global reset_button
                    pause_button.pack_forget()
                    reset_button.pack_forget()
                    resume_button.pack(padx=5, side='left')
                    reset_button.pack(padx=5, side='left')
                if self.current_exercise_index < len(current_data['exercises']):
                    self.StartRest = ctk.CTkButton(master=new_frame, text="Start Rest", font=("Arial", 24),
                                                   command=BeginTheRest)
                    self.StartRest.pack(padx=5, pady=5, anchor="s", side="bottom")

                def skip_time():
                    self.remaining_seconds=0




        def StartWorkoutWrapper():
            if self.current_exercise_index < len(current_data['exercises']):
                if hasattr(self, 'next_exercise'):
                    self.next_exercise.pack_forget()
                if hasattr(self, 'prev_exercise'):
                    self.prev_exercise.pack_forget()
                BeginTheWork()

        self.StartTheWorkoutB = ctk.CTkButton(master=WorkoutFrame, fg_color="green", text="Start The Workout",
                                              font=("Arial", 18),
                                              command=StartWorkoutWrapper)
        self.StartTheWorkoutB.pack(padx=5, pady=5, anchor="w", side="bottom")

    def display_current_exercise(self, WorkoutFrame, current_data):
        if hasattr(self, 'theseframes'):
            self.theseframes.destroy()

        if hasattr(self, 'finishedlabel'):
            self.finishedlabel.destroy()

        if self.current_exercise_index < len(current_data['exercises']):
            exercise = current_data['exercises'][self.current_exercise_index]
            self.theseframes = ctk.CTkFrame(master=WorkoutFrame)
            self.theseframes.pack(padx=5, pady=5, fill="both", expand="yes")

            self.theseexercise_label = ctk.CTkLabel(master=self.theseframes, text=exercise, font=("Arial", 24))
            self.theseexercise_label.pack(padx=5, pady=5, anchor="w")

            self.theseSets_label = ctk.CTkLabel(master=self.theseframes,
                                                text=f"Intended Sets : {current_data['exercise_sets'][self.current_exercise_index]}",
                                                font=("Arial", 18))
            self.theseSets_label.pack(padx=10, pady=0, anchor="w")
            print(current_data['exercises'][self.current_exercise_index])
            ViewVid(current_data['exercises'][self.current_exercise_index])


            reps_count = 0
            times_count = 0
            for i in range(self.current_exercise_index):
                if self.saved_type_order[i] == "regular":
                    reps_count += 1
                else:
                    times_count += 1

            exercise_type = self.saved_type_order[self.current_exercise_index]
            if exercise_type == "regular":
                self.theseConditional_label = ctk.CTkLabel(master=self.theseframes,
                                                           text=f"Intended Reps : {current_data['exercise_reps'][reps_count]}",
                                                           font=("Arial", 18))
            else:
                self.theseConditional_label = ctk.CTkLabel(master=self.theseframes,
                                                           text=f"Intended Time : {current_data['exercise_times'][times_count]}",
                                                           font=("Arial", 18))

            self.theseConditional_label.pack(padx=10, pady=0, anchor="w")

            self.theseTime_label = ctk.CTkLabel(master=self.theseframes,
                                                text=f"Intended Rest : {current_data['exercise_rest_times'][self.current_exercise_index]}",
                                                font=("Arial", 18))
            self.theseTime_label.pack(padx=10, pady=0, anchor="w")
        else:
            self.finishedlabel = ctk.CTkLabel(master=WorkoutFrame, text="Workout Completed", font=("Arial", 18))
            self.finishedlabel.pack(padx=5, pady=5, anchor="w")

    def SaveEntries(self):
        current_data = self.saved_data[self.current_page_name]

        current_data['exercises'].clear()
        current_data['exercise_sets'].clear()
        current_data['exercise_reps'].clear()
        current_data['exercise_times'].clear()
        current_data['exercise_rest_times'].clear()
        current_data['exercise_checkbox_states'].clear()
        current_data['Type'].clear()

        self.ShowOnSelect()

        for exercise_name in self.saved_selection_order:
            current_data['exercises'].append(exercise_name)
            if exercise_name not in self.VidsList:
                self.VidsList.append(exercise_name)


        for i, checkbox in enumerate(self.Exercises["CheckBoxes"]):
            current_data['exercise_checkbox_states'].append(checkbox.get())

        for exercise_name in current_data['exercises']:
            for i, checkbox in enumerate(self.Exercises["CheckBoxes"]):
                if checkbox.cget("text") == exercise_name and checkbox.get()==1:
                    current_data['exercise_sets'].append(self.Exercises['SetsEntry'][i].get())
                    break

        for exercise_name in current_data['exercises']:
            for i, checkbox in enumerate(self.Exercises["CheckBoxes"]):
                if checkbox.cget("text") == exercise_name and checkbox.get()==1:
                    if self.Exercises["RepsEntry"][i] is not None:
                        reps_value = self.Exercises["RepsEntry"][i].get()
                        current_data['exercise_reps'].append(reps_value if reps_value != "" else "")
                        break

        for exercise_name in current_data['exercises']:
            for i, checkbox in enumerate(self.Exercises["CheckBoxes"]):
                if checkbox.cget("text") == exercise_name and checkbox.get()==1:
                    if self.Exercises["TimeEntry"][i] is not None:
                        time_value = self.Exercises["TimeEntry"][i].get()
                        current_data['exercise_times'].append(time_value if time_value != "" else "")
                        break

        for exercise_name in current_data['exercises']:
            for i, checkbox in enumerate(self.Exercises["CheckBoxes"]):
                if checkbox.cget("text") == exercise_name and checkbox.get() == 1:
                    current_data['exercise_rest_times'].append(self.Exercises["RestEntry"][i].get())
                    break

        for exercise_name in current_data['exercises']:
            for i, checkbox in enumerate(self.Exercises["CheckBoxes"]):
                if checkbox.cget("text") == exercise_name:
                    current_data["Type"].append(self.Exercises["Type"][i])
                    break


        self.SavingIndex=0
        print(self.saved_data)
        print(self.VidsList)



    def RetrieveEntries(self):
        current_data = self.saved_data[self.current_page_name]

        for i, checkbox in enumerate(self.Exercises["CheckBoxes"]):
            if i < len(current_data['exercise_checkbox_states']):
                if current_data['exercise_checkbox_states'][i] == 1:
                    checkbox.select()
                else:
                    checkbox.deselect()

        for i, checkbox in enumerate(self.Exercises["CheckBoxes"]):
            if checkbox.get() == 1:
                setlabel = self.Exercises["SetsLabel"][i]
                setentry = self.Exercises["SetsEntry"][i]
                repslabel = self.Exercises["RepsLabel"][i]
                repsentry = self.Exercises["RepsEntry"][i]
                timelabel = self.Exercises["TimeLabel"][i]
                timeentry = self.Exercises["TimeEntry"][i]
                restlabel = self.Exercises["RestLabel"][i]
                restentry = self.Exercises["RestEntry"][i]

                setlabel.pack(padx=5, pady=5, anchor="w", side="left")
                setentry.pack(padx=1, pady=5, anchor="w", side="left")
                if repslabel is not None:
                    repslabel.pack(padx=5, pady=5, anchor="w", side="left")
                if repsentry is not None:
                    repsentry.pack(padx=1, pady=5, anchor="w", side="left")
                if timelabel is not None:
                    timelabel.pack(padx=5, pady=5, anchor="w", side="left")
                if timeentry is not None:
                    timeentry.pack(padx=1, pady=5, anchor="w", side="left")

                restlabel.pack(padx=5, pady=5, anchor="w", side="left")
                restentry.pack(padx=1, pady=5, anchor="w", side="left")

        for idx, exercise_name in enumerate(current_data['exercises']):
            for i, checkbox in enumerate(self.Exercises["CheckBoxes"]):
                if checkbox.cget("text") == exercise_name and checkbox.get() == 1:
                    if idx < len(current_data['exercise_sets']):
                        self.Exercises["SetsEntry"][i].insert(0, current_data['exercise_sets'][idx])
                    break
        self.RetrievalIndex =0

        reps_index = 0
        for exercise_name in current_data['exercises']:
            for i, checkbox in enumerate(self.Exercises["CheckBoxes"]):
                if checkbox.cget("text") == exercise_name and checkbox.get() == 1:
                    if self.Exercises["RepsEntry"][i] is not None and reps_index < len(current_data['exercise_reps']):
                        self.Exercises["RepsEntry"][i].insert(0, current_data['exercise_reps'][reps_index])
                        reps_index += 1
                    break
        self.RetrievalIndex = 0

        time_index = 0
        for exercise_name in current_data['exercises']:
            for i, checkbox in enumerate(self.Exercises["CheckBoxes"]):
                if checkbox.cget("text") == exercise_name and checkbox.get() == 1:
                    if self.Exercises["TimeEntry"][i] is not None and time_index < len(current_data['exercise_times']):
                        self.Exercises["TimeEntry"][i].insert(0, current_data['exercise_times'][time_index])
                        time_index += 1
                    break
        self.RetrievalIndex = 0

        for idx, exercise_name in enumerate(current_data['exercises']):
            for i, checkbox in enumerate(self.Exercises["CheckBoxes"]):
                if checkbox.cget("text") == exercise_name and checkbox.get() == 1:ل
                    if idx < len(current_data['exercise_rest_times']):
                        self.Exercises["RestEntry"][i].insert(0, current_data['exercise_rest_times'][idx])
                    break
        self.RetrievalIndex = 0
        
