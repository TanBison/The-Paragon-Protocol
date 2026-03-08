import customtkinter as ctk

## this class is a frame that appears in the page u call it in and it appears in the master u give for it
class ExerciseRow(ctk.CTkFrame):
    def __init__(self, master, exercise_name, app, on_toggle_callback , workout_type = None, is_timed=False):
        super().__init__(master = master, fg_color="#1a1a1a")
        self.pack(side="top", padx=5, pady=5, fill="x")

        self.app = app

        self.workout_type = workout_type

        self.exercise_name = exercise_name
        self.is_timed = is_timed

        #phone
        self.on_toggle_callback = on_toggle_callback

        # this is where we save the widgets
        self.reps_entries = []

        self.time_entries = []

        self.sets_rest_entries = []


        #when the class frame first appears this is the first thing that appears in it (the checkbox) when u click it, it shows entry_frame that contains sets_entry or
        #sets_entry and rest_time depending on the workout the function that does this is toggle entries down
        self.checkbox = ctk.CTkCheckBox(self, text=self.exercise_name, command=self.toggle_entries, hover_color = 'grey', fg_color='white', checkmark_color= 'black')
        self.checkbox.pack(anchor="w", padx=10)


        self.entry_frame = ctk.CTkFrame(self, fg_color="black")
        #the container that will make reps entries or time entries based on the number entered in the sets entry
        self.reps_time_container = ctk.CTkFrame(master= self.entry_frame, fg_color="#008B8B" )
        self.rest_container = ctk.CTkFrame(master= self.entry_frame, fg_color="#2A3B4D")

        #the sets entry
        if workout_type == 1:
            self.set_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Sets")
            self.set_entry.pack(anchor='w', side='left', padx=5, pady=5)

            self.exercise_rest_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="rest between exercises")
            self.exercise_rest_entry.pack(anchor='w', side='left', padx=5, pady=5)


        #here the number u enter in the sets when ur finger is lift of the keyboard it triggers the show_reps_time function which creates reps or time entries
        if workout_type == 1:
            self.set_entry.bind("<KeyRelease>", self.show_reps_time)




    # the checkbox function
    def toggle_entries(self):
        if self.checkbox.get() == 1 and self.workout_type == 1:
            self.entry_frame.pack(fill="x", padx=10, pady=(0, 5))

        else:
            self.entry_frame.pack_forget()

        self.on_toggle_callback(self)

    # the keyboard release function in sets entry function the .bind
    def show_reps_time(self, event):
        #we save the number of sets to know the number of other entries we create
        sets_text = self.set_entry.get()

        for widget in self.reps_time_container.winfo_children():
            widget.destroy()
        for widget in self.rest_container.winfo_children():
            widget.destroy()
        self.reps_time_container.pack_forget()
        self.rest_container.pack_forget()

        self.reps_entries = []
        self.time_entries = []
        self.sets_rest_entries = []

        try:
            num_sets = int(sets_text)
            num_sets_1 = int(sets_text)-1
        except ValueError:
            num_sets = 0
            num_sets_1 = 0

        if self.is_timed == False:
            for i in range(num_sets):
                reps_label = ctk.CTkLabel(self.reps_time_container, text=f"Set {i + 1} Reps:")
                reps_label.pack(padx=10)

                reps_entry = ctk.CTkEntry(self.reps_time_container, placeholder_text="e.g., 10")
                reps_entry.pack(padx=5, pady=5)

                self.reps_entries.append(reps_entry)

                self.reps_time_container.pack(pady=5, padx=5, side='right')

                # we only show the rest if the workout type is 1
            for i in range(num_sets_1):
                if self.workout_type == 1:
                    sets_rest_label = ctk.CTkLabel(self.rest_container, text=f"Set {i + 1} to {i+2} Rest")
                    sets_rest_label.pack(padx=10)
                    sets_rest_entry = ctk.CTkEntry(self.rest_container, placeholder_text=f"(e.g., 90s)")
                    sets_rest_entry.pack(padx=5, pady=5)

                    self.sets_rest_entries.append(sets_rest_entry)
                    self.rest_container.pack(pady=5, padx=5, side='right')





        elif self.is_timed == True:
            for i in range(num_sets):
                time_label = ctk.CTkLabel(self.reps_time_container, text=f"Set {i + 1} Time:")
                time_label.pack(padx=10)

                time_entry = ctk.CTkEntry(self.reps_time_container, placeholder_text="e.g., 60secs")
                time_entry.pack(padx=5, pady=5)

                self.time_entries.append(time_entry)
                self.reps_time_container.pack(pady=5, padx=5, side='right')

            # we only show the rest if the workout type is 1
            for i in range(num_sets_1):
                if self.workout_type == 1:
                    sets_rest_label = ctk.CTkLabel(self.rest_container, text=f"Set {i + 1} to {i+2} Rest")
                    sets_rest_label.pack(padx=10)
                    sets_rest_entry = ctk.CTkEntry(self.rest_container,
                                                    placeholder_text=f"(e.g., 90s)")
                    sets_rest_entry.pack(padx=5, pady=5)

                    self.sets_rest_entries.append(sets_rest_entry)
                    self.rest_container.pack(pady=5, padx=5, side='right')

                    self.reps_time_container.pack(pady=5, padx=5, side='right')



    #save all the widgets per object called
    def get_widget_toolbox(self):
        # 1. Create the toolbox dictionary
        if self.workout_type == 1:
            saved_widgets = {
                'checkbox': self.checkbox,
                'sets_entry': self.set_entry,
                'exercise_rest_entry': self.exercise_rest_entry,
                'rep_entries': self.reps_entries,
                'time_entries': self.time_entries,
                'sets_rest_entries': self.sets_rest_entries
            }
            return saved_widgets

        elif self.workout_type == 2:
            saved_widgets = {
                'checkbox': self.checkbox,
                'rep_entries': self.reps_entries,
                'time_entries': self.time_entries,
                'rounds_number': None,
                'rounds_rest': None

            }
            return saved_widgets



