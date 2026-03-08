import customtkinter as ctk
import sqlite3
import json
from datetime import datetime
from PIL import Image
from backend.LocalManager import LocalManager  # Import needed for deletion

class HistoryPage(ctk.CTkFrame):
    def __init__(self, container, app):
        super().__init__(master=container)
        self.app = app
        self.configure(fg_color='#010212')

        self.trash_icon = ctk.CTkImage(Image.open(r"D:\ProjectPhotos\trash_bin.png"), size=(24, 24))
        # --- 1. LOGS FRAME ---
        self.LogsFrame = ctk.CTkFrame(master=self, width=1200, height=660, fg_color='#00283a')
        self.LogsFrame.place(x=10, y=50)
        self.LogsFrame.pack_propagate(False)

        self.HistoryList = ctk.CTkScrollableFrame(self.LogsFrame, fg_color="transparent")
        self.HistoryList.pack(fill="both", expand=True, padx=5, pady=5)

        # --- 2. SLIDING DRAWER ---
        self.DrawerIsOpen = False
        self.SlidingFrame = ctk.CTkScrollableFrame(master=self, width=740, height=660,
                                                   fg_color='Black', corner_radius=10, border_width=0)
        self.slider1 = 1280
        self.SlidingFrame.place(x=self.slider1, y=50)

        # Toggle Button
        self.SideButton = ctk.CTkButton(master=self, width=20, height=50, fg_color='Black',
                                        command=self.toggle_drawer, hover_color='black',
                                        text='\u276F', font=('Arial Bold', 18),
                                        corner_radius=8, border_width=0)
        self.slider2 = 1253
        self.SideButton.place(x=self.slider2, y=335)

    # --- RAISE & ANIMATION ---
    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        self.load_history_cards()
        if self.DrawerIsOpen:
            self.DrawerIsOpen = False
            self.SideButton.configure(text='\u276F')
            self.LogsFrame.configure(width=1200)
            self.slider1 = 1280
            self.slider2 = 1253
            self.SideButton.place(x=self.slider2, y=335)
            self.SlidingFrame.place(x=self.slider1, y=50)

    def toggle_drawer(self):
        if self.DrawerIsOpen:
            self.animate_close()
            self.DrawerIsOpen = False
            self.SideButton.configure(text='\u276E')
            self.LogsFrame.configure(width=1200)
        else:
            self.animate_open()
            self.DrawerIsOpen = True
            self.SideButton.configure(text='\u276F')
            self.LogsFrame.configure(width=495)

    def animate_close(self):
        if self.slider1 < 1280:
            self.slider1 += 20
            self.slider2 += 20
            self.SideButton.place(x=self.slider2, y=335)
            self.SlidingFrame.place(x=self.slider1, y=50)
            self.after(5, self.animate_close)

    def animate_open(self):
        if self.slider1 > 540:
            self.slider1 -= 20
            self.slider2 -= 20
            self.SideButton.place(x=self.slider2, y=335)
            self.SlidingFrame.place(x=self.slider1, y=50)
            self.after(5, self.animate_open)

    # --- DATABASE & UI ---

    def load_history_cards(self):
        for widget in self.HistoryList.winfo_children():
            widget.destroy()

        try:
            conn = sqlite3.connect("project_z.db")
            cursor = conn.cursor()
            # Fetch ID (wid) too!
            cursor.execute("SELECT id, date, duration_seconds, score_percent, details FROM history ORDER BY id DESC")
            rows = cursor.fetchall()
            conn.close()
        except Exception as e:
            print("DB Error:", e)
            return

        for row in rows:
            wid, wdate, wdur, wscore, wdetails = row
            self.create_workout_card(wid, wdate, wdur, wscore, wdetails)

    def delete_entry(self, wid):
        """Calls backend to delete row and refreshes list."""
        print(f"Deleting ID: {wid}")
        manager = LocalManager()
        manager.delete_workout(wid)
        # Refresh the list to show it's gone
        self.load_history_cards()
        # If drawer was open showing deleted item, close it nicely
        if self.DrawerIsOpen:
            self.toggle_drawer()

    def create_workout_card(self, wid, wdate, wdur, wscore, wdetails):
        """Creates the card using Grid layout to prevent visual glitches."""
        try:
            date_obj = datetime.strptime(wdate, "%Y-%m-%d %H:%M:%S")
            display_date = date_obj.strftime("%b %d, %Y")
        except:
            display_date = wdate

        # 1. Main Card Frame
        card = ctk.CTkFrame(self.HistoryList, fg_color="#0a0b15", height=80, corner_radius=10)
        card.pack(fill="x", pady=5)

        # [GRID SETUP]
        # Column 0: Score (Fixed)
        # Column 1: Info (Expands to fill space)
        # Column 2: Trash Bin (Fixed)
        card.grid_columnconfigure(1, weight=1)
        card.grid_rowconfigure(0, weight=1)  # Center vertically

        # Click Event
        def on_click(event):
            self.open_drawer_with_details(wdetails, wscore, display_date)

        card.bind("<Button-1>", on_click)

        # --- COL 0: Score ---
        color = "#66ddaa" if wscore >= 80 else ("#FFB74D" if wscore >= 50 else "#FF5555")
        score_lbl = ctk.CTkLabel(card, text=f"{wscore:.0f}%", font=("Arial Bold", 24), text_color=color, width=80)
        score_lbl.grid(row=0, column=0, padx=10, sticky="w")
        score_lbl.bind("<Button-1>", on_click)

        # --- COL 1: Info (Date/Duration) ---
        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.grid(row=0, column=1, padx=5, sticky="ew")  # sticky="ew" makes it stretch
        info_frame.bind("<Button-1>", on_click)

        date_lbl = ctk.CTkLabel(info_frame, text=display_date, font=("Arial Bold", 16), text_color="white", anchor="w")
        date_lbl.pack(fill="x", pady=(5, 0))
        date_lbl.bind("<Button-1>", on_click)

        dur_mins = wdur // 60
        dur_lbl = ctk.CTkLabel(info_frame, text=f"Duration: {dur_mins} min", font=("Arial", 12), text_color="gray",
                               anchor="w")
        dur_lbl.pack(fill="x")
        dur_lbl.bind("<Button-1>", on_click)

        # --- COL 2: Delete Button ---
        if self.trash_icon:
            del_btn = ctk.CTkButton(card, text="", image=self.trash_icon, width=30, height=30,
                                    fg_color="transparent", hover_color="#330000",
                                    corner_radius=5, border_width=0,
                                    command=lambda: self.confirm_delete(wid))
        else:
            del_btn = ctk.CTkButton(card, text="X", width=30, height=30,
                                    fg_color="transparent", hover_color="#330000",
                                    text_color="#FF5555", font=("Arial Bold", 16),
                                    corner_radius=5, border_width=0,
                                    command=lambda: self.confirm_delete(wid))

        del_btn.grid(row=0, column=2, padx=20)
    # --- REVERTED DRAWER FUNCTION (Original simple version) ---
    def open_drawer_with_details(self, details_json, score, date_str):
        # 1. Clear old content
        for widget in self.SlidingFrame.winfo_children():
            widget.destroy()

        # 2. Parse JSON
        try:
            data = json.loads(details_json)
        except:
            return

        # 3. Header
        ctk.CTkLabel(self.SlidingFrame, text="Mission Report", font=("Arial Bold", 30), text_color="#66ddaa").pack(
            pady=(20, 5), anchor="w", padx=20)
        ctk.CTkLabel(self.SlidingFrame, text=f"{date_str} | Score: {score:.1f}%", font=("Arial", 16),
                     text_color="gray").pack(pady=(0, 20), anchor="w", padx=20)

        # 4. Get Data Lists
        exercises = data.get('exercises', [])
        reps_data = data.get('exercise_reps', [])
        times_data = data.get('exercise_times', [])
        types = data.get('Type', [])

        # [NEW] Try to get Targets (It handles old workouts safely by returning empty list)
        target_reps_data = data.get('exercise_targets', [])

        for i, ex_name in enumerate(exercises):
            # Exercise Name
            ctk.CTkLabel(self.SlidingFrame, text=ex_name, font=("Arial Bold", 20), text_color="#66ddaa").pack(
                anchor="w", padx=20, pady=(10, 0))

            sets_frame = ctk.CTkFrame(self.SlidingFrame, fg_color="#1F2937", corner_radius=10)
            sets_frame.pack(fill="x", padx=20, pady=5)

            current_reps = reps_data[i]
            current_times = times_data[i]

            # Get targets for this specific exercise
            current_targets = target_reps_data[i] if i < len(target_reps_data) else []

            is_timed = (types[i] == 'timed') if i < len(types) else False

            # Loop through Sets
            for set_idx, val in enumerate(current_reps if not is_timed else current_times):
                row = ctk.CTkFrame(sets_frame, fg_color="transparent", height=30)
                row.pack(fill="x", padx=10, pady=2)

                # "Set 1" Label
                ctk.CTkLabel(row, text=f"Set {set_idx + 1}", width=60, anchor="w", text_color="white").pack(side="left")

                # --- FORMAT THE VALUE (Done / Target) ---
                if is_timed:
                    label_text = f"{val}s"
                else:
                    # Check if we have a target for this set
                    if set_idx < len(current_targets) and current_targets[set_idx]:
                        # We have a target! Show "12 / 15 reps"
                        target_val = current_targets[set_idx]
                        label_text = f"{val} / {target_val} reps"
                    else:
                        # No target found (Old history), just show "12 reps"
                        label_text = f"{val} reps"

                # Value Label
                ctk.CTkLabel(row, text=label_text, font=("Arial Bold", 14), text_color="#aaaaaa", anchor="w").pack(
                    side="left", padx=20)

        if not self.DrawerIsOpen:
            self.toggle_drawer()
    def confirm_delete(self, wid):
        """Creates a custom Dark-Themed popup to confirm deletion."""

        # 1. Create the Popup Window
        response = self.app.show_custom_popup(
            title="Confirm Deletion",
            message="Are you sure you want to delete this mission log permanently?\n\nThis action cannot be undone.",
            button_options=["Cancel", "DELETE"],
            icon_type="cancel"
        )

        if response == "DELETE":
            self.delete_entry(wid)
        else:
            print("Deletion cancelled.")