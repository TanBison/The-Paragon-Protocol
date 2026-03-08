import customtkinter as ctk
from PIL import Image
from pages.WorkoutEvaluationPage import WorkoutEvaluationPage
from CTkToolTip import CTkToolTip
import time


class WorkoutStartedPage(ctk.CTkFrame):
    def __init__(self, container, app):
        super().__init__(master=container)
        self.app = app
        self.configure(fg_color='#010212')

        # --- TRACKERS ---
        self.current_ex_index = 0
        self.current_set_index = 0

        # --- ROBUST TIMER VARIABLES ---
        self.timer_running = False
        self.end_time = 0  # The timestamp when the timer should finish
        self.paused_time_left = 0  # Snapshot of time left when paused
        self.timer_loop = None  # To cancel the .after event cleanly

        # --- FRAMES ---
        self.WorkoutFrame = ctk.CTkScrollableFrame(master=self, width=580, height=290, fg_color='#00283a')
        self.WorkoutFrame.place(x=10, y=50)

        self.VideoFrame = ctk.CTkFrame(master=self, width=650, height=620, fg_color='#00283a')
        self.VideoFrame.place(x=620, y=50)

        self.RestFrame = ctk.CTkFrame(master=self, width=600, height=180, fg_color='#00283a')
        self.RestFrame.place(x=10, y=360)
        self.RestFrame.pack_propagate(False)

        # --- START BUTTON ---
        self.begin_the_work = ctk.CTkButton(master=self, fg_color='transparent', width=200, height=45,
                                            text="Begin Workout", corner_radius=50, border_width=3,
                                            border_color="#1F2937", command=self.start_workout,
                                            font=("Arial Bold", 24), hover_color="#191970")

        self.TerminateButton = ctk.CTkButton(master=self, width=250, height=35, fg_color='red', border_width=0,
                                           command=lambda: self.confirm_termination(),
                                           text="Terminate Workout", font=("Arial Bold", 18))
        self.TerminateButton.place(x=515, y=680)

        self.ProceedButton = ctk.CTkButton(master=self, width=250, height=35, fg_color='#00283a', border_width=0,
                                           command=lambda: self.app.show_page(WorkoutEvaluationPage),
                                           text="Proceed To Evaluation", font=("Arial Bold", 18))


        self.RestTimeLabel = ctk.CTkLabel(master=self.RestFrame, text="00:00", text_color='white',
                                          font=('Arial Bold', 30))
        self.RestTimeLabel.pack(padx=5, pady=20, anchor='center')

        # Resume (Initially Hidden)
        self.ResumeButtonPath = Image.open(r"D:\ProjectPhotos\Resume.png")
        self.ResumeButtonImage = ctk.CTkImage(self.ResumeButtonPath, size=(40, 40))
        self.ResumeButton = ctk.CTkButton(master=self.RestFrame, border_width=0, hover=False,
                                          image=self.ResumeButtonImage,
                                          text="", fg_color='transparent', width=40, height=40,
                                          command=self.resume_timer)
        CTkToolTip(self.ResumeButton, message='Resume')

        # Pause (Initially Visible)
        self.PauseButtonPath = Image.open(r"D:\ProjectPhotos\Pause.png")
        self.PauseButtonImage = ctk.CTkImage(self.PauseButtonPath, size=(40, 40))
        self.PauseButton = ctk.CTkButton(master=self.RestFrame, border_width=0, hover=False,
                                         image=self.PauseButtonImage,
                                         text="", fg_color='transparent', width=40, height=40, command=self.pause_timer)
        CTkToolTip(self.PauseButton, message='Pause')
        self.PauseButton.place(x=250, y=80)

        # Skip
        self.SkipTimePath = Image.open(r"D:\ProjectPhotos\Skip2.png")
        self.SkipTimeImage = ctk.CTkImage(self.SkipTimePath, size=(40, 40))
        self.SkipTimeB = ctk.CTkButton(master=self.RestFrame, border_width=0, hover=False, image=self.SkipTimeImage,
                                       text="", fg_color='transparent', width=40, height=40, command=self.skip_timer)
        CTkToolTip(self.SkipTimeB, message='Skip Rest')
        self.SkipTimeB.place(x=310, y=80)

        # Add Time
        self.AddTimePath = Image.open(r"D:\ProjectPhotos\AddTime.png")
        self.AddTimeImage = ctk.CTkImage(self.AddTimePath, size=(40, 40))
        self.AddTimeB = ctk.CTkButton(master=self.RestFrame, border_width=0, hover=False, image=self.AddTimeImage,
                                      text="", fg_color='transparent', width=40, height=40,
                                      command=lambda: self.modify_time(5))
        CTkToolTip(self.AddTimeB, message='Add 5 secs')
        self.AddTimeB.place(x=380, y=80)

        # Take Time
        self.TakeTimePath = Image.open(r"D:\ProjectPhotos\TakeTime.png")
        self.TakeTimeImage = ctk.CTkImage(self.TakeTimePath, size=(40, 40))
        self.TakeTimeB = ctk.CTkButton(master=self.RestFrame, border_width=0, hover=False, image=self.TakeTimeImage,
                                       text="", fg_color='transparent', width=40, height=40,
                                       command=lambda: self.modify_time(-5))
        CTkToolTip(self.TakeTimeB, message='Remove 5 secs')
        self.TakeTimeB.place(x=180, y=80)


    def start_new_timer(self, seconds):
        """Starts a new timer based on System Clock"""
        # If timer is already running, do nothing (prevents reset bug)
        if self.timer_running:
            return

        self.actual_rest_start_time = time.time()

        # 1. Calculate the exact time this timer should finish
        self.end_time = time.time() + int(seconds)
        self.timer_running = True

        # 2. Reset UI State
        self.ResumeButton.place_forget()
        self.PauseButton.place(x=250, y=80)

        # 3. Start the loop
        self.update_timer_loop()

    def update_timer_loop(self):
        """Checks the system clock every 100ms"""
        if not self.timer_running:
            return

        # Calculate remaining time (Goal Time - Current Time)
        remaining = self.end_time - time.time()

        if remaining <= 0:
            # --- TIMER FINISHED ---
            self.timer_running = False
            self.RestTimeLabel.configure(text="Loading next...", text_color="#00FF00", font=('Arial Bold', 24))
            self.after(500, self.next_set)
        else:
            # --- UPDATE DISPLAY ---
            # We convert to int just for display, but keep float for precision
            self.update_display(int(remaining))

            # --- CANCEL OLD LOOP & START NEW ONE ---
            # This 'after_cancel' prevents the "double speed" bug
            if self.timer_loop:
                self.after_cancel(self.timer_loop)

            # Run again in 100ms (0.1s). This makes it responsive but not heavy.
            self.timer_loop = self.after(100, self.update_timer_loop)

    def cancel_active_timer(self):
        """Forcefully stops any running timer and resets display."""
        self.timer_running = False
        self.paused_time_left = 0

        # --- [NEW] Reset the visual label immediately ---
        self.RestTimeLabel.configure(text="00:00", text_color='white', font=('Arial Bold', 30))
        # ------------------------------------------------

        # Cancel the scheduled 'after' task
        if self.timer_loop is not None:
            try:
                self.after_cancel(self.timer_loop)
                self.timer_loop = None
            except ValueError:
                pass  # Handle cases where the loop ID is already invalid
    def update_display(self, seconds_left):
        minutes = seconds_left // 60
        seconds = seconds_left % 60
        # +1 hack is sometimes used to make it feel natural, but raw int is accurate
        self.RestTimeLabel.configure(text=f"{minutes:02d}:{seconds:02d}", text_color="white", font=('Arial Bold', 30))

    def pause_timer(self):
        if not self.timer_running: return  # Can't pause if not running

        self.timer_running = False

        # Cancel the loop immediately so it stops ticking
        if self.timer_loop:
            self.after_cancel(self.timer_loop)

        # Snapshot: Save how much time was left at the moment of pause
        self.paused_time_left = self.end_time - time.time()

        # UI Swap
        self.PauseButton.place_forget()
        self.ResumeButton.place(x=250, y=80)

    def resume_timer(self):
        if self.timer_running or self.paused_time_left <= 0: return

        # Recalculate End Time: Current Time + The time we had left
        self.end_time = time.time() + self.paused_time_left
        self.timer_running = True

        # UI Swap
        self.ResumeButton.place_forget()
        self.PauseButton.place(x=250, y=80)

        self.update_timer_loop()

    def skip_timer(self):
        # Allow skipping only if we are actually in a rest period
        # We check paused_time_left in case they paused then skipped
        current_rem = self.end_time - time.time()
        if self.timer_running or (not self.timer_running and self.paused_time_left > 0):
            self.timer_running = False
            if self.timer_loop:
                self.after_cancel(self.timer_loop)

            self.RestTimeLabel.configure(text="Skipping...", text_color="#00FF00", font=('Arial Bold', 24))
            self.after(500, self.next_set)

    def modify_time(self, seconds):
        """Adds/Removes time by pushing the End Time forward/back"""
        # Logic: We simply move the finish line

        # Case 1: Timer is running
        if self.timer_running:
            self.end_time += seconds
            # Update display instantly so they see the button worked
            rem = int(self.end_time - time.time())
            if rem < 0: rem = 0  # Don't go negative
            self.update_display(rem)

        # Case 2: Timer is Paused
        elif not self.timer_running and self.paused_time_left > 0:
            self.paused_time_left += seconds
            if self.paused_time_left < 0: self.paused_time_left = 0
            self.update_display(int(self.paused_time_left))

#############################################################
#############################################################

    def present_the_current_workout(self):

        for widget in self.WorkoutFrame.winfo_children():
            widget.destroy()

        if hasattr(self, 'WorkoutFrame') and self.WorkoutFrame.winfo_exists():
            self.WorkoutFrame.destroy()

        self.WorkoutFrame = ctk.CTkScrollableFrame(master=self, width=580, height=290, fg_color='#00283a')
        self.WorkoutFrame.place(x=10, y=50)


        # Shorten variable name for readability
        data = self.app.workout_logic.current_workout_type1_plan
        print("this is the data after starting", data)

        # --- FONT SETTINGS ---
        header_font = ("Arial", 26, "bold")
        info_font = ("Arial", 22)

        # 1. OUTER LOOP: Iterate through the exercises
        for ex_i, exercise_name in enumerate(data['exercises']):

            # Get how many sets exist for this exercise
            num_sets = int(data['exercise_sets'][ex_i])

            # 2. INNER LOOP: Iterate through the sets for THIS exercise
            for set_i in range(num_sets):

                # --- DISPLAY EXERCISE NAME ---
                current_exercise = ctk.CTkLabel(
                    master=self.WorkoutFrame,
                    text=f"Exercise: {exercise_name} (Set {set_i + 1}/{num_sets})",
                    font=header_font,
                    text_color="white",
                    anchor="w"  # Aligns text inside the label to the left
                )
                # anchor="w" pushes the widget to the left side of the frame
                # padx=20 gives it a nice margin from the edge
                current_exercise.pack(padx=20, pady=(15, 2), anchor="w", fill="x")

                # --- DISPLAY REPS OR TIME ---
                if data['Type'][ex_i] == 'regular':
                    reps_value = data['exercise_reps'][ex_i][set_i]
                    # Handle empty values
                    display_val = reps_value if reps_value != "" else "-"

                    current_reps = ctk.CTkLabel(
                        master=self.WorkoutFrame,
                        text=f"Reps: {display_val}",
                        font=info_font,
                        anchor="w"
                    )
                    current_reps.pack(padx=20, pady=2, anchor="w")
                else:
                    time_value = data['exercise_times'][ex_i][set_i]
                    display_val = time_value if time_value != "" else "-"

                    current_work_time = ctk.CTkLabel(
                        master=self.WorkoutFrame,
                        text=f"Work Time: {display_val}",
                        font=info_font,
                        anchor="w"
                    )
                    current_work_time.pack(padx=20, pady=2, anchor="w")

                # --- REST TIME LOGIC ---
                if set_i == num_sets - 1:
                    # Last set for this exercise
                    rest_val = data['exercise_rest_times'][ex_i]
                    label_text = "Exercise Rest"
                    text_color = "#FF5555"  # Red for big rest
                else:
                    # Normal set rest
                    rest_val = data['sets_rest_times'][ex_i][set_i]
                    label_text = "Set Rest"
                    text_color = "yellow"  # Yellow for short rest

                rest_val = rest_val if rest_val != "" else "0"

                upcoming_rest = ctk.CTkLabel(
                    master=self.WorkoutFrame,
                    text=f"{label_text}: {rest_val}s",
                    font=info_font,
                    text_color=text_color,
                    anchor="w"
                )
                upcoming_rest.pack(padx=20, pady=(2, 20), anchor="w")
                self.begin_the_work.place(x=200, y=550)

    def start_workout(self):
        #start workout timer
        self.start_timestamp = time.time()
        # 1. KILL THE OLD TIMER FIRST
        self.cancel_active_timer()

        logic = self.app.workout_logic
        plan = logic.current_workout_type1_plan

        # Reset the "Done" dictionary to be empty but ready
        logic.workout_done = {
            'exercises': plan['exercises'][:],  # Copy names
            'Type': plan['Type'][:],  # Copy types
            'exercise_sets': plan['exercise_sets'][:],
            'exercise_reps': [],  # We will fill these loops below
            'exercise_times': [],
            'sets_rest_times': [],
            'exercise_rest_times': [""] * len(plan['exercises'])  # One slot per exercise
        }

        # Create the empty lists based on the plan's size
        # If the plan says 3 sets, we make a list like ['', '', '']
        for i, sets_count_str in enumerate(plan['exercise_sets']):
            count = int(sets_count_str)

            # Create slots for Reps and Time
            logic.workout_done['exercise_reps'].append([""] * count)
            logic.workout_done['exercise_times'].append([""] * count)

            # Create slots for Set Rests (matching the plan's list length to be safe)
            # Usually plan['sets_rest_times'][i] is a list of strings
            sets_rest_len = len(plan['sets_rest_times'][i])
            logic.workout_done['sets_rest_times'].append([""] * sets_rest_len)
        print("the workout_done skeleton : ", logic.workout_done)
        # Initialize the variable to track actual rest duration later
        self.actual_rest_start_time = 0

        # 2. Reset indices
        self.current_ex_index = 0
        self.current_set_index = 0

        # 3. Build the UI
        self.present_active_set()

    def present_active_set(self):
        if hasattr(self, 'WorkoutFrame') and self.WorkoutFrame.winfo_exists():
            self.WorkoutFrame.destroy()

        self.WorkoutFrame = ctk.CTkScrollableFrame(master=self, width=580, height=290, fg_color='#00283a')
        self.WorkoutFrame.place(x=10, y=50)

        data = self.app.workout_logic.current_workout_type1_plan
        if not data or not data.get('exercises'): return

        ex_i = self.current_ex_index
        set_i = self.current_set_index

        if ex_i >= len(data['exercises']):
            self.current_ex_index = 0
            self.current_set_index = 0
            ex_i = 0

        exercise_name = data['exercises'][ex_i]
        num_sets = int(data['exercise_sets'][ex_i])

        header_font = ("Arial", 30, "bold")
        info_font = ("Arial", 24)

        current_exercise = ctk.CTkLabel(master=self.WorkoutFrame, text=f"Current: {exercise_name}", font=header_font,
                                        text_color="white", anchor="w")
        current_exercise.pack(padx=20, pady=(20, 5), anchor="w", fill="x")

        set_info = ctk.CTkLabel(master=self.WorkoutFrame, text=f"Set {set_i + 1} of {num_sets}", font=("Arial", 18),
                                text_color="gray", anchor="w")
        set_info.pack(padx=20, pady=(0, 20), anchor="w")

        if data['Type'][ex_i] == 'regular':
            val = data['exercise_reps'][ex_i][set_i]
            text_val = f"Target Reps: {val if val else '-'}"
            input_label_text = "Reps Done:"
        else:
            val = data['exercise_times'][ex_i][set_i]
            text_val = f"Target Time: {val if val else '-'}"
            input_label_text = "Time Done:"

        main_metric = ctk.CTkLabel(master=self.WorkoutFrame, text=text_val, font=info_font, anchor="w")
        main_metric.pack(padx=20, pady=10, anchor="w")

        # Input
        input_container = ctk.CTkFrame(self.WorkoutFrame, fg_color="transparent")
        input_container.pack(padx=20, pady=10, anchor="w", fill="x")

        self.done_label = ctk.CTkLabel(input_container, text=input_label_text, font=("Arial", 20), text_color="#A0A0A0")
        self.done_label.pack(side="left", padx=(0, 10))

        self.done_entry = ctk.CTkEntry(input_container, width=80, font=("Arial", 20), fg_color="#001822",
                                       border_color="#1F2937")
        self.done_entry.pack(side="left")

        # Calculate Rest
        is_last_set = (set_i == num_sets - 1)
        if is_last_set:
            rest_seconds = data['exercise_rest_times'][ex_i]
            rest_label_text = "Upcoming: Big Rest"
            rest_color = "#FF5555"
        else:
            rest_seconds = data['sets_rest_times'][ex_i][set_i]
            rest_label_text = "Upcoming: Set Rest"
            rest_color = "yellow"

        try:
            current_rest_val = int(rest_seconds)
        except ValueError:
            current_rest_val = 0

        minutes = current_rest_val // 60
        seconds = current_rest_val % 60
        formatted_time = f"{minutes:02d}:{seconds:02d}"

        # Set the label to show the upcoming rest (e.g., "01:30") instead of "00:00"
        self.RestTimeLabel.configure(text=formatted_time, text_color="white", font=('Arial Bold', 30))

        # Start Rest Button
        self.start_timer_btn = ctk.CTkButton(
            self.WorkoutFrame,
            text="Start Rest Timer",
            command=lambda: self.start_new_timer(current_rest_val),
            font=("Arial Bold", 16),
            height=30,
            width=150,
            fg_color="#E59400",
            hover_color="#B37400",
            text_color="white"
        )
        self.start_timer_btn.pack(padx=20, pady=(5, 10), anchor="w")

        # Rest Preview
        rest_display = ctk.CTkLabel(master=self.WorkoutFrame, text=f"{rest_label_text}: {current_rest_val}s",
                                    font=info_font, text_color=rest_color, anchor="w")
        rest_display.pack(padx=20, pady=20, anchor="w")

        self.begin_the_work.place_forget()

    def next_set(self):
        logic = self.app.workout_logic

        # Get what the user typed
        user_input = self.done_entry.get()

        ex_i = self.current_ex_index
        set_i = self.current_set_index

        # Save it to the backend
        if logic.current_workout_type1_plan['Type'][ex_i] == 'regular':
            logic.workout_done['exercise_reps'][ex_i][set_i] = user_input
        else:
            logic.workout_done['exercise_times'][ex_i][set_i] = user_input
        #save the time of the current set based on if it was exercise rest or set rest
        if self.actual_rest_start_time > 0:

            # 1. Calculate Duration
            actual_duration = int(time.time() - self.actual_rest_start_time)

            # 2. Decide WHERE to save it
            # We need to know if this was the Last Set or a Middle Set
            total_sets_for_this_exercise = int(logic.current_workout_type1_plan['exercise_sets'][ex_i])
            is_last_set = (set_i == total_sets_for_this_exercise - 1)

            if is_last_set:
                # It was an Exercise Rest (Big Rest)
                logic.workout_done['exercise_rest_times'][ex_i] = str(actual_duration)
                print(f"Saved Exercise Rest: {actual_duration}s")
            else:
                # It was a Set Rest (Small Rest)
                # usage: sets_rest_times[exercise_index][set_index]
                logic.workout_done['sets_rest_times'][ex_i][set_i] = str(actual_duration)
                print(f"Saved Set Rest: {actual_duration}s")
        print("Workout_done after each set : ", logic.workout_done)

        # Reset the start time for the next round
        self.actual_rest_start_time = 0

        # Reset display
        self.RestTimeLabel.configure(text="00:00", text_color="white", font=('Arial Bold', 30))
        self.paused_time_left = 0  # Clear pause cache

        data = self.app.workout_logic.current_workout_type1_plan
        current_ex_sets = int(data['exercise_sets'][self.current_ex_index])

        if self.current_set_index < current_ex_sets - 1:
            self.current_set_index += 1
            self.present_active_set()

        elif self.current_ex_index < len(data['exercises']) - 1:
            self.current_ex_index += 1
            self.current_set_index = 0
            self.present_active_set()

        else:
            self.current_ex_index = 0
            self.current_set_index = 0
            self.paused_time_left = 0
            self.timer_running = False

            for widget in self.WorkoutFrame.winfo_children():
                widget.destroy()
            finish_label = ctk.CTkLabel(self.WorkoutFrame, text="WORKOUT COMPLETE!", font=("Arial", 30, "bold"),
                                        text_color="#00FF00")
            finish_label.place(relx=0.5, rely=0.5, anchor="center")
            self.TerminateButton.place_forget()
            self.ProceedButton.place(x=515, y=680)
            end_timestamp = time.time()
            total_duration_seconds = int(end_timestamp - self.start_timestamp)
            print(f"Total Workout Time: {total_duration_seconds} seconds")

            self.app.workout_duration = total_duration_seconds

    def confirm_termination(self):
        # 1. Pause Timer (So time doesn't tick while they decide)
        was_running = self.timer_running
        if was_running:
            self.pause_timer()

        # 2. Call the App Brain for the Popup
        response = self.app.show_custom_popup(
            title="Terminate Workout?",
            message="Are you sure you want to abort this session?\nAll progress will be lost.",
            button_options=["Cancel", "Terminate"],
            icon_type="cancel"  # Makes it Red
        )

        # 3. Handle the Answer
        if response == "Terminate":
            # User said YES -> Kill it
            print("User confirmed termination.")
            self.app.terminate_workout()
        else:
            # User said NO -> Resume timer if it was running
            print("Termination cancelled.")
            if was_running:
                self.resume_timer()
