import customtkinter as ctk
from pages.WorkoutPages import WorkoutPagesParent


class Workout2Page(WorkoutPagesParent):
    def __init__(self, container, app):
        super().__init__(container, app, workout_type = 2)

        self.PullingScrollable.configure(width = 600, height = 200)
        self.PushingScrollable.configure(width = 600, height = 200)

        self.LegsScrollable.configure(width = 600, height = 200)
        self.AbsScrollable.configure(width = 600, height = 200)

        self.LegsScrollable.place(x= 10, y = 340)
        self.AbsScrollable.place(x=645, y=340)

        self.LegsFrame.place(x=160, y=310)
        self.AbsFrame.place(x=790, y=310)

        #comingsoon
        self.begin_workoutB.configure(text = "Coming Soon", fg_color = 'red', hover_color = '#DC143C')

        #the new addition (the only difference xd)
        self.RoundsFrame = ctk.CTkFrame(master=self, width=570, height=100, fg_color='#00283a')
        self.RoundsFrame.place(x=355, y = 570)
        self.RoundsFrame.pack_propagate(False)

        self.RoundsLabel = ctk.CTkLabel(master = self.RoundsFrame, text="NO. rounds and the rest time between (Unified for all exercises)", font=("Arial Bold", 18))
        self.RoundsLabel.pack(padx=10, pady=10)

        self.entry_container = ctk.CTkFrame(self.RoundsFrame, fg_color="transparent")
        self.entry_container.pack(pady=5)

        self.RestEntry = ctk.CTkEntry(master=self.entry_container, placeholder_text="Rest")
        self.RestEntry.pack(side="left", padx=10)

        self.RoundsEntry = ctk.CTkEntry(master=self.entry_container, placeholder_text="Rounds")
        self.RoundsEntry.pack(side="left", padx=10)



    def override_here(self):
        self.fill_exercise_frames(WorkoutType=2)





