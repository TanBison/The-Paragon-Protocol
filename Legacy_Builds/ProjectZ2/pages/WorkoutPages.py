import customtkinter as ctk
from pages.widgets import ExerciseRow
from pages.WorkoutStartedPage import  WorkoutStartedPage
from CTkToolTip import CTkToolTip

class WorkoutPagesParent(ctk.CTkFrame):
    def __init__(self, container, app, workout_type):
        super().__init__(container)

        # this is the key for app.py
        self.app = app

        self.workout_type = workout_type

        self.exercise_rows = []

        self.ordered_checked_list = []


        self.configure(fg_color='#010212')

        self.PullingScrollable = ctk.CTkScrollableFrame(master=self, width=600, height=250, fg_color='#00283a',
                                                        border_width=2, border_color='#37f398',
                                                        scrollbar_button_color="#37f398", scrollbar_fg_color='#00283a')
        self.PullingScrollable.place(x=10, y=80)

        self.PullingFrame = ctk.CTkFrame(master=self, width=300, height=25, fg_color='#00283a')
        self.PullingFrame.pack_propagate(False)
        self.PullingFrame.place(x=160, y=50)

        self.PullingText = ctk.CTkLabel(master=self.PullingFrame, text="Pulling Exercises", font=("Arial Bold", 22))
        self.PullingText.pack(padx=10, pady=0, expand=True)

        self.PushingScrollable = ctk.CTkScrollableFrame(master=self, width=600, height=250, fg_color='#00283a',
                                                        border_width=2, border_color='#37f398',
                                                        scrollbar_button_color="#37f398", scrollbar_fg_color='#00283a')
        self.PushingScrollable.place(x=645, y=80)

        self.PushingFrame = ctk.CTkFrame(master=self, width=300, height=25, fg_color='#00283a')
        self.PushingFrame.pack_propagate(False)
        self.PushingFrame.place(x=790, y=50)

        self.PushingText = ctk.CTkLabel(master=self.PushingFrame, text="Pushing Exercises", font=("Arial Bold", 22))
        self.PushingText.pack(padx=10, pady=0, expand=True)

        self.LegsScrollable = ctk.CTkScrollableFrame(master=self, width=600, height=250, fg_color='#00283a',
                                                     border_width=2, border_color='#37f398',
                                                     scrollbar_button_color="#37f398", scrollbar_fg_color='#00283a')
        self.LegsScrollable.place(x=10, y=390)

        self.LegsFrame = ctk.CTkFrame(master=self, width=300, height=25, fg_color='#00283a')
        self.LegsFrame.pack_propagate(False)
        self.LegsFrame.place(x=160, y=360)

        self.LegsText = ctk.CTkLabel(master=self.LegsFrame, text="Legs Exercises", font=("Arial Bold", 22))
        self.LegsText.pack(padx=10, pady=0, expand=True)

        self.AbsScrollable = ctk.CTkScrollableFrame(master=self, width=600, height=250, fg_color='#00283a',
                                                    border_width=2, border_color='#37f398',
                                                    scrollbar_button_color="#37f398", scrollbar_fg_color='#00283a')
        self.AbsScrollable.place(x=645, y=390)

        self.AbsFrame = ctk.CTkFrame(master=self, width=300, height=25, fg_color='#00283a')
        self.AbsFrame.pack_propagate(False)
        self.AbsFrame.place(x=790, y=360)

        self.AbsText = ctk.CTkLabel(master=self.AbsFrame, text="Abs Exercises", font=("Arial Bold", 22))
        self.AbsText.pack(padx=10, pady=0, expand=True)

        self.begin_workoutB = ctk.CTkButton(master=self, text="Begin The Workout",
                                            command= lambda : self.collect_data_and_start_workout(self.workout_type), font=("Arial Bold", 18)
                                            , width=250, height=35, fg_color='#00283a')
        self.begin_workoutB.place(x=515, y=680)

        self.override_here()



    def on_exercise_toggled(self, row_that_was_clicked):
        """This function is called by the ExerciseRow's checkbox."""

        is_checked = row_that_was_clicked.checkbox.get() == 1

        if is_checked:
            # If the box was CHECKED, add the row object to our ordered list
            if row_that_was_clicked not in self.ordered_checked_list:
                self.ordered_checked_list.append(row_that_was_clicked)
        else:
            # If the box was UNCHECKED, remove it from the list
            if row_that_was_clicked in self.ordered_checked_list:
                self.ordered_checked_list.remove(row_that_was_clicked)

        # (Optional) Debug print to see your new list work in real-time
        print("--- Current Workout Order ---")
        for row in self.ordered_checked_list:
            print(f"  -> {row.exercise_name}")

    #so we override the fill_exercise_frames method in the WorkoutType2Page
    def override_here(self):
        self.fill_exercise_frames(WorkoutType=1)



    #this function works immedietly when the page is created it, gets the exercises and saves them in variables then creates objects from the ExercisesRow class
    #to every exercise exists
    #for more info look at the comments in the widgets file

    def fill_exercise_frames(self, WorkoutType):
        pull_exercises = self.app.workout_logic.pulling_exercises
        pull_timed = self.app.workout_logic.pulling_timed

        push_exercises = self.app.workout_logic.pushing_exercises
        push_timed = self.app.workout_logic.pushing_timed

        leg_exercises = self.app.workout_logic.legs_exercises
        leg_timed = self.app.workout_logic.legs_timed

        ab_exercises = self.app.workout_logic.abs_exercises
        ab_timed = self.app.workout_logic.abs_timed

        #every object is saved here (every entry created)
        self.exercise_rows = []

        for exercise in pull_exercises:
            row = ExerciseRow(self.PullingScrollable, exercise, self.app, on_toggle_callback=self.on_exercise_toggled, workout_type = WorkoutType, is_timed=False,)
            row.pack()
            self.exercise_rows.append(row)

        for exercise in pull_timed:
            row = ExerciseRow(self.PullingScrollable, exercise, self.app, on_toggle_callback=self.on_exercise_toggled, workout_type= WorkoutType, is_timed=True)
            row.pack()
            self.exercise_rows.append(row)

        for exercise in push_exercises:
            row =  ExerciseRow(self.PushingScrollable,exercise, self.app, on_toggle_callback=self.on_exercise_toggled, workout_type= WorkoutType, is_timed=False)
            row.pack()
            self.exercise_rows.append(row)

        for exercise in push_timed:
            row =  ExerciseRow(self.PushingScrollable, exercise, self.app, on_toggle_callback=self.on_exercise_toggled, workout_type= WorkoutType, is_timed=True)
            row.pack()
            self.exercise_rows.append(row)

        for exercise in leg_exercises:
            row =  ExerciseRow( self.LegsScrollable, exercise, self.app, on_toggle_callback=self.on_exercise_toggled, workout_type= WorkoutType, is_timed=False)
            row.pack()
            self.exercise_rows.append(row)

        for exercise in leg_timed:
            row =  ExerciseRow(self.LegsScrollable, exercise, self.app, on_toggle_callback=self.on_exercise_toggled, workout_type= WorkoutType, is_timed=True)
            row.pack()
            self.exercise_rows.append(row)

        for exercise in ab_exercises:
            row =  ExerciseRow(self.AbsScrollable, exercise, self.app, on_toggle_callback=self.on_exercise_toggled, workout_type= WorkoutType, is_timed=False)
            row.pack()
            self.exercise_rows.append(row)

        for exercise in ab_timed:
            row =  ExerciseRow(self.AbsScrollable, exercise, self.app, on_toggle_callback=self.on_exercise_toggled, workout_type= WorkoutType, is_timed=True)
            row.pack()
            self.exercise_rows.append(row)

    def collect_data_and_start_workout(self, workout_type):
        #stop the user if no exercises selected
        if not self.ordered_checked_list:
            self.app.show_custom_popup(
                title="Mission Aborted",
                message="Unable to launch.\n\nNo exercises selected.\nPlease select at least one target to begin.",
                button_options=["Understood"],
                icon_type="cancel"
            )
            return

        #mark if a workout is already working
        if self.app.workout_started_flagged:
            response = self.app.show_custom_popup(
                title="Conflict Detected",
                message="A session is already active!\n\nStarting a new one will DISCARD current progress.\n\nOverride system?",
                button_options=["Cancel", "Overwrite"],
                icon_type="warning"
            )

            if response != "Overwrite":
                print("New workout cancelled by user.")
                return
        ##We Make Sure Nothing is left behind (popup message if an entry is left empty)
        # --- 1. Validation Check (NEW) ---
        # We assume valid until proven otherwise
        is_valid = True
        error_message = ""

        # Loop through rows to check for empty fields
        for row in self.ordered_checked_list:
            toolbox = row.get_widget_toolbox()

            # Check if any Rep box is empty (if not timed)
            if not row.is_timed:
                for entry in toolbox['rep_entries']:
                    if not entry.get().strip():  # .strip() removes spaces
                        is_valid = False
                        error_message = f"Missing Reps for {row.exercise_name}"
                        break

            # Check if any Time box is empty (if timed)
            else:
                for entry in toolbox['time_entries']:
                    if not entry.get().strip():
                        is_valid = False
                        error_message = f"Missing Time for {row.exercise_name}"
                        break

            # Check Rest boxes (only for Type 1)
            if workout_type == 1:
                # Check Exercise Rest
                if not toolbox['exercise_rest_entry'].get().strip():
                    is_valid = False
                    error_message = f"Missing Exercise Rest for {row.exercise_name}"
                    break

                # Check Set Rests
                for entry in toolbox['sets_rest_entries']:
                    if not entry.get().strip():
                        is_valid = False
                        error_message = f"Missing Set Rest for {row.exercise_name}"
                        break

            if not is_valid: break

        # If Validation Failed -> Show Popup and STOP
        if not is_valid:
            self.app.show_custom_popup(
                title="Invalid Data",
                message=error_message,
                button_options=["Fix It"],
                icon_type="cancel"
            )
            return
        # --- 1. Get the correct backend dictionary ---
        if workout_type == 1:
            data_dict = self.app.workout_logic.current_workout_type1_plan
            print("Saving data to Workout Type 1 Plan...")
        elif workout_type == 2:
            data_dict = self.app.workout_logic.current_workout_type2_plan
            print("Saving data to Workout Type 2 Plan...")
        else:
            print(f"Error: Unknown workout_type {workout_type}")
            return  # Don't do anything else

        # --- 2. Clear all the old lists in that dictionary ---
        data_dict['exercises'] = []
        data_dict['exercise_reps'] = []
        data_dict['exercise_times'] = []
        data_dict['Type'] = []

        # Clear the specific rest lists for each type
        if workout_type == 1:
            data_dict['exercise_sets'] = []
            data_dict['sets_rest_times'] = []
            data_dict['exercise_rest_times'] = []
        elif workout_type == 2:
            data_dict['rounds_number'] = [] # unified sets
            data_dict['rounds_rest'] = []  # This is the unified rest

        # --- 3. Loop through NEW, ORDERED list ---
        for row in self.ordered_checked_list:

            # Get the "Toolbox" from the worker
            toolbox = row.get_widget_toolbox()

            # --- 4. Get data that is COMMON to both types ---
            data_dict['exercises'].append(toolbox['checkbox'].cget("text"))


            reps_list = [entry.get() for entry in toolbox['rep_entries']]
            times_list = [entry.get() for entry in toolbox['time_entries']]

            # padding
            if not reps_list and row.is_timed:
                reps_list = [""] * len(times_list)
            if not times_list and not row.is_timed:
                times_list = [""] * len(reps_list)

            data_dict['exercise_reps'].append(reps_list)
            data_dict['exercise_times'].append(times_list)
            data_dict['Type'].append("timed" if row.is_timed else "regular")

            # --- 5. Get data that is DIFFERENT for each type ---
            if workout_type == 1:
                set_rests_list = [entry.get() for entry in toolbox['sets_rest_entries']]
                data_dict['exercise_sets'].append(toolbox['sets_entry'].get())
                data_dict['sets_rest_times'].append(set_rests_list)
                data_dict['exercise_rest_times'].append(toolbox['exercise_rest_entry'].get())
        #make the last exercise_rest_time = 0 because no exercises after it, no need for the rest
        if workout_type == 1 and data_dict['exercise_rest_times']:
            data_dict['exercise_rest_times'][-1] = "0"

            # (Note: Type 2 doesn't need to save row-level rests)

        # --- 6. Save the "Page-Level" data (for Type 2) ---
        if workout_type == 2:
            # 'self.RestEntry' is the widget you created in Workout2Page's __init__
            try:
                data_dict['rounds_number'] = self.RoundsEntry.get()
                data_dict['rounds_rest'] = self.RestEntry.get()
            except AttributeError:
                print("Error: Could not find self.RestEntry for Workout 2")
                data_dict['rounds_number'] = ""
                data_dict['rounds_rest'] = ""  # Save empty string as fallback

        if WorkoutStartedPage in self.app.frames:
            target_page = self.app.frames[WorkoutStartedPage]
            if hasattr(target_page, 'cancel_active_timer'):
                print("Stopping previous background timer...")
                target_page.cancel_active_timer()
            if hasattr(target_page, 'ProceedButton'):
                target_page.ProceedButton.place_forget()
                # Show the "Terminate" button again
            if hasattr(target_page, 'TerminateButton'):
                target_page.TerminateButton.place(x=515, y=680)


        # --- 7. Switch the page ---
        print(f"Data saved to backend: {data_dict}")
        if workout_type == 1:
            self.app.workout_started_flagged = False
            self.app.show_page(WorkoutStartedPage)




