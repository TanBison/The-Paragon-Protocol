import customtkinter as ctk
from PIL import Image
from backend.LocalManager import LocalManager


class WorkoutEvaluationPage(ctk.CTkFrame):
    def __init__(self, container, app):
        super().__init__(master = container)
        #this is the key for app.py
        self.app = app

        self.configure(fg_color='#010212')

        self.OverViewFrame= ctk.CTkFrame(master = self, fg_color='#252531', width=1260, height=290)
        self.OverViewFrame.place(x=10, y=50)
        self.OverViewFrame.pack_propagate(False)

        self.WorkoutFrame = ctk.CTkScrollableFrame(master=self, fg_color='#252531', width= 630, height=345 )
        self.WorkoutFrame.place(x=10, y = 350)

        #RatingsLoading
        self.RatingAPath = Image.open("D:\ProjectPhotos\RatingA.png")
        self.RatingBPath = Image.open("D:\ProjectPhotos\RatingB.png")
        self.RatingCPath = Image.open("D:\ProjectPhotos\RatingC.png")
        self.RatingDPath = Image.open("D:\ProjectPhotos\RatingD.png")

        self.RatingAImage = ctk.CTkImage(self.RatingAPath, size=(270,270))
        self.RatingBImage = ctk.CTkImage(self.RatingBPath, size=(270,270))
        self.RatingCImage = ctk.CTkImage(self.RatingCPath, size=(270,270))
        self.RatingDImage = ctk.CTkImage(self.RatingDPath, size=(270,270))

        self.RankLabel = ctk.CTkLabel(master=self.OverViewFrame, fg_color='transparent', text="")
        self.RankLabel.pack(side='right', padx=20, pady=5)

        self.OverViewLabel = ctk.CTkLabel(self.OverViewFrame, text= "Workout Overview", font=('Arial Bold', 40), text_color='#66ddaa')
        self.OverViewLabel.place(x=30, y=15)

        self.DurationRingPath= Image.open("D:\ProjectPhotos\DurationRing.png")
        self.DurationRing = ctk.CTkImage(self.DurationRingPath, size=(210,210))

        self.WorkoutDuration = ctk.CTkLabel(self.OverViewFrame, text = '00:00', image=self.DurationRing, text_color='White', font=('Arial Bold', 36))
        self.WorkoutDuration.place(x=110,y=70)

        self.ScoreLabel = ctk.CTkLabel(self.OverViewFrame, text="0.0%",
                                       font=("Arial", 70, "bold"), text_color="white")
        self.ScoreLabel.place(relx=0.5, rely=0.45, anchor="center")

        self.ScoreSubtitle = ctk.CTkLabel(self.OverViewFrame, text="Performance Score",
                                          font=("Arial", 18), text_color="gray", )
        self.ScoreSubtitle.place(relx=0.5, rely=0.65, anchor="center")

        self.exit_dont_save = ctk.CTkButton(self, text= 'Exit Without Saving', fg_color = 'transparent', corner_radius = 20, width = 560 , height = 50, hover_color = '#330000',
                                            border_width = 3, border_color = '#FF0000', font=('Arial Bold', 18), text_color = "#FF0000", command = lambda: self.on_exit_click())
        self.exit_dont_save.place(x= 685, y= 550)
        self.exit_save_locally = ctk.CTkButton(self, text='Exit And Save Locally', fg_color='transparent', corner_radius = 20, width = 560 , height = 50, hover_color = '#332200',
                                            border_width = 3, border_color = '#FF6103', font=('Arial Bold', 18), text_color = "#FF6103", command = lambda: self.on_save_local_click())
        self.exit_save_locally.place(x=685, y=605)
        self.exit_save_cloud = ctk.CTkButton(
            self,
            text='Exit And Save To Cloud',
            font=('Arial Bold', 18),
            fg_color='#66ddaa',
            text_color='#010212',
            hover_color='#55cc99',
            corner_radius=20, width=560, height=50,
            command = lambda: self.on_save_cloud_click()
        )
        self.exit_save_cloud.place(x=685, y=660)

        self.StatsFrame = ctk.CTkFrame(master=self, fg_color="transparent", width=560, height=190)
        self.StatsFrame.place(x=685, y=350)
        self.StatsFrame.pack_propagate(False)

        # --- Box 1: Total Reps (Top Left) ---
        self.Box1 = ctk.CTkFrame(self.StatsFrame, fg_color="#1F2937", corner_radius=10,
                                 width=270, height=85, border_width=1, border_color="#3A3A4A")
        self.Box1.place(x=0, y=0)

        ctk.CTkLabel(self.Box1, text="Total Reps", font=("Arial", 14), text_color="gray").place(relx=0.5, rely=0.3,
                                                                                                anchor="center")
        self.StatRepsLabel = ctk.CTkLabel(self.Box1, text="0", font=("Arial Bold", 24), text_color="white")
        self.StatRepsLabel.place(relx=0.5, rely=0.7, anchor="center")

        # --- Box 2: Sets Completed (Top Right) ---
        self.Box2 = ctk.CTkFrame(self.StatsFrame, fg_color="#1F2937", corner_radius=10,
                                 width=270, height=85, border_width=1, border_color="#3A3A4A")
        self.Box2.place(x=290, y=0)

        ctk.CTkLabel(self.Box2, text="Sets Completed", font=("Arial", 14), text_color="gray").place(relx=0.5, rely=0.3,
                                                                                                    anchor="center")
        self.StatSetsLabel = ctk.CTkLabel(self.Box2, text="0", font=("Arial Bold", 24), text_color="white")
        self.StatSetsLabel.place(relx=0.5, rely=0.7, anchor="center")

        # --- Box 3: Est. Volume (Bottom Left) ---
        self.Box3 = ctk.CTkFrame(self.StatsFrame, fg_color="#1F2937", corner_radius=10,
                                 width=270, height=85, border_width=1, border_color="#3A3A4A")
        self.Box3.place(x=0, y=105)

        ctk.CTkLabel(self.Box3, text="Est. Volume", font=("Arial", 14), text_color="gray").place(relx=0.5, rely=0.3,
                                                                                                 anchor="center")
        self.StatVolumeLabel = ctk.CTkLabel(self.Box3, text="---", font=("Arial Bold", 24), text_color="white")
        self.StatVolumeLabel.place(relx=0.5, rely=0.7, anchor="center")

        # --- Box 4: Est. Calories (Bottom Right) ---
        self.Box4 = ctk.CTkFrame(self.StatsFrame, fg_color="#1F2937", corner_radius=10,
                                 width=270, height=85, border_width=1, border_color="#3A3A4A")
        self.Box4.place(x=290, y=105)

        ctk.CTkLabel(self.Box4, text="Est. Calories", font=("Arial", 14), text_color="gray").place(relx=0.5, rely=0.3,
                                                                                                   anchor="center")
        self.StatCalsLabel = ctk.CTkLabel(self.Box4, text="---", font=("Arial Bold", 24), text_color="white")
        self.StatCalsLabel.place(relx=0.5, rely=0.7, anchor="center")



    def tkraise(self, *args, **kwargs):
        """Automatically runs every time the page is shown."""
        super().tkraise(*args, **kwargs)
        self.evaluate_performance()

    def evaluate_performance(self):
        """Calculates score based on Reps/Time completion %"""

        # 1. UPDATE DURATION DISPLAY
        total_seconds = getattr(self.app, 'workout_duration', 0)
        mins = total_seconds // 60
        secs = total_seconds % 60
        self.WorkoutDuration.configure(text=f"{mins:02d}:{secs:02d}")

        # 2. GET DATA
        plan = self.app.workout_logic.current_workout_type1_plan
        done = self.app.workout_logic.workout_done

        total_set_scores = 0
        total_sets_count = 0
        total_reps_count = 0  # <--- New variable
        completed_sets_count = 0  # <--- New variable

        # --- LOOP THROUGH THE PLAN ---
        num_exercises = len(plan['exercises'])

        for ex_i in range(num_exercises):
            is_timed = (plan['Type'][ex_i] == 'timed')

            if is_timed:
                targets = plan['exercise_times'][ex_i]
                actuals = done['exercise_times'][ex_i]
            else:
                targets = plan['exercise_reps'][ex_i]
                actuals = done['exercise_reps'][ex_i]

            for set_i in range(len(targets)):
                total_sets_count += 1
                try:
                    target_val = float(targets[set_i])
                except ValueError:
                    target_val = 0

                try:
                    done_val = float(actuals[set_i])
                except ValueError:
                    done_val = 0.0

                # [NEW] Track Stats Logic
                if done_val > 0:
                    completed_sets_count += 1
                    if not is_timed:
                        total_reps_count += int(done_val)

                # [EXISTING] Score Logic
                if target_val > 0:
                    set_score = done_val / target_val
                else:
                    set_score = 0

                if set_score > 1.0: set_score = 1.0
                total_set_scores += set_score
        # 3. CALCULATE FINAL AVERAGE
        if total_sets_count > 0:
            final_percentage = (total_set_scores / total_sets_count) * 100
        else:
            final_percentage = 0

        self.ScoreLabel.configure(text=f"{final_percentage:.1f}%")

        # Store this in 'self' so the Save button can grab it easily
        self.final_score_percent = final_percentage

        print(f"Final Score: {final_percentage:.1f}% (Avg of {total_sets_count} sets)")

        # 4. UPDATE RANK IMAGE
        if final_percentage >= 90:
            self.RankLabel.configure(image=self.RatingAImage)
        elif final_percentage >= 75:
            self.RankLabel.configure(image=self.RatingBImage)
        elif final_percentage >= 50:
            self.RankLabel.configure(image=self.RatingCImage)
        else:
            self.RankLabel.configure(image=self.RatingDImage)

        self.StatRepsLabel.configure(text=str(int(total_reps_count)))
        self.StatSetsLabel.configure(text=f"{completed_sets_count} / {total_sets_count}")

        # Placeholders for future features
        self.StatVolumeLabel.configure(text="---")
        self.StatCalsLabel.configure(text="---")

        # 5. SHOW SUMMARY LIST
        self.display_workout_summary()

    def display_workout_summary(self):
        """Populates the scrollable frame with Reps/Time AND Rest details."""

        # 1. CLEAR OLD WIDGETS
        for widget in self.WorkoutFrame.winfo_children():
            widget.destroy()

        # 2. GET DATA
        logic = self.app.workout_logic
        plan = logic.current_workout_type1_plan
        done = logic.workout_done

        header_font = ("Arial", 20, "bold")
        detail_font = ("Arial", 16)

        # 3. LOOP THROUGH EXERCISES
        num_exercises = len(plan['exercises'])

        for ex_i in range(num_exercises):
            ex_name = plan['exercises'][ex_i]
            is_timed = (plan['Type'][ex_i] == 'timed')

            # --- A. Header ---
            block_frame = ctk.CTkFrame(self.WorkoutFrame, fg_color="transparent")
            block_frame.pack(fill="x", pady=(10, 20), padx=10)

            name_label = ctk.CTkLabel(block_frame, text=ex_name, font=header_font,
                                      text_color="#66ddaa", anchor="w")
            name_label.pack(fill="x", anchor="w")

            # --- B. Get Data Lists ---
            if is_timed:
                targets = plan['exercise_times'][ex_i]
                actuals = done['exercise_times'][ex_i]
                unit = "s"
            else:
                targets = plan['exercise_reps'][ex_i]
                actuals = done['exercise_reps'][ex_i]
                unit = ""

            # Lists for rest times
            set_rests = done['sets_rest_times'][ex_i]  # Gaps between sets
            ex_rest = done['exercise_rest_times'][ex_i]  # Rest after last set

            # --- C. Create Set Rows ---
            sets_text_list = []

            for set_i in range(len(targets)):
                target_val = targets[set_i]

                # 1. Get Actual Work
                try:
                    actual_val = actuals[set_i]
                    if actual_val == "": actual_val = "0"
                except IndexError:
                    actual_val = "0"

                # 2. Get Rest Data
                # If it's the LAST set, look at Exercise Rest. Otherwise, look at Set Rest.
                if set_i == len(targets) - 1:
                    rest_val = ex_rest
                    rest_label = "Ex.Rest"  # Optional indicator
                else:
                    try:
                        rest_val = set_rests[set_i]
                    except IndexError:
                        rest_val = "0"
                    rest_label = "Rest"

                if rest_val == "": rest_val = "0"

                # 3. Format: "Set 1: 12/12 (Rest: 60s)"
                # We use a distinct color or format for rest to make it readable
                row_str = f"Set {set_i + 1}: {actual_val}/{target_val}{unit}  (Rest: {rest_val}s)"
                sets_text_list.append(row_str)

            # Join with a vertical separator or new lines?
            # Given we added rest info, it might be long. Let's try " | " first.
            full_sets_str = "   |   ".join(sets_text_list)

            # If the text is too long, CustomTkinter labels wrap automatically if we don't set a width,
            # but sometimes "   \n   " is cleaner than "   |   " if you have many sets.
            # Let's stick to " | " for now.

            sets_label = ctk.CTkLabel(block_frame, text=full_sets_str, font=detail_font,
                                      text_color="white", anchor="w", justify="left", wraplength=580)
            sets_label.pack(fill="x", anchor="w", padx=(10, 0), pady=(5, 0))

            if ex_i < num_exercises - 1:
                divider = ctk.CTkFrame(self.WorkoutFrame, height=2, fg_color="#3A3A4A")
                divider.pack(fill="x", padx=20, pady=5)

    def _get_workout_stats(self):
        """Collects all the data needed for saving, INCLUDING TARGETS."""
        logic = self.app.workout_logic

        # 1. Get the raw dictionary (The complex data - What you DID)
        data = logic.workout_done

        # --- [NEW] BUNDLE THE TARGETS ---
        # We grab the plan (What you AIMED for) while it's still in memory
        plan = logic.current_workout_type1_plan

        # We inject the targets into the data dictionary
        # This way, the LocalManager saves them automatically inside the JSON
        data['exercise_targets'] = plan['exercise_reps']
        data['exercise_target_times'] = plan['exercise_times']
        # --------------------------------

        # 2. Get Duration (from App state)
        duration = getattr(self.app, 'workout_duration', 0)

        # 3. Get Score (saved in self during evaluation)
        score = getattr(self, 'final_score_percent', 0.0)

        # 4. Get Total Reps (Read from the UI label)
        try:
            total_reps = int(self.StatRepsLabel.cget("text"))
        except:
            total_reps = 0

        return data, duration, score, total_reps
    # --- HELPER: RESET & NAVIGATE ---
    def _reset_and_go_home(self):
        """Clears all workout data and returns to Home Page."""
        print("--- RESETTING APP STATE ---")

        # 1. Wipe the Logic Dictionary
        self.app.workout_logic.workout_done = {
            'exercises': [], 'exercise_sets': [], 'exercise_reps': [],
            'exercise_times': [], 'sets_rest_times': [], 'exercise_rest_times': [], 'Type': []
        }

        # 2. Reset Flags
        self.app.workout_started_flagged = False
        self.app.workout_duration = 0

        # 3. Go Home
        from pages.HomePage import HomePage
        self.app.show_page(HomePage)

    # --- BUTTON ACTIONS ---

    def action_exit_no_save(self):
        print("User clicked: Exit Without Saving")
        self._reset_and_go_home()

    def action_save_local(self):
        print("User clicked: Save Locally")

        # 1. Get the data
        data, dur, score, reps = self._get_workout_stats()

        # 2. Save to SQLite
        manager = LocalManager()
        manager.save_workout(data, dur, score, reps)

        # 3. Reset and Exit
        self._reset_and_go_home()

    def on_exit_click(self):
        """Warns the user that data will be lost."""
        response = self.app.show_custom_popup(
            title="Discard Mission?",
            message="Warning: If you exit now, this workout data will be purged from memory forever.\n\nAre you sure you want to discard it?",
            button_options=["Cancel", "Discard"],
            icon_type="cancel"  # Red Title
        )

        if response == "Discard":
            # Go back to Home (or wherever your exit logic goes)
            from pages.HomePage import HomePage
            self.app.show_page(HomePage)

    def on_save_local_click(self):
        """Warns about the risks of local storage."""
        response = self.app.show_custom_popup(
            title="Local Storage Protocol",
            message="Data will be saved to a local file within the app directory.\n\nRISK WARNING: If this file is deleted or the app is uninstalled without a backup, your history will be lost.\n\nProceed?",
            button_options=["Cancel", "Save"],
            icon_type="warning"  # Orange Title
        )

        if response == "Save":
            # Call your ACTUAL save function here
            self.action_save_local()

    def on_save_cloud_click(self):
        """Explains Cloud safety and AI usage."""
        response = self.app.show_custom_popup(
            title="Cloud Upload Protocol",
            message="This is the safest option. Your data is backed up remotely and never lost.\n\nNOTICE: Anonymous workout metrics may be used to train our AI models (No sensitive data will be shared).",
            button_options=["Cancel", "Accept & Save"],
            icon_type="warning"  # Orange Title
        )

        if response == "Accept & Save":
            # Placeholder for future Cloud Logic
            print("Cloud Save Initiated...")
            # self.save_to_cloud()