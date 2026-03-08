import customtkinter as ctk
from pages.widgets import ExerciseRow
from pages.WorkoutStartedPage import  WorkoutStartedPage
from pages.WorkoutPages import WorkoutPagesParent

class Workout1Page(WorkoutPagesParent):
    def __init__(self, container, app):
        super().__init__(container, app, workout_type = 1)

    def override_here(self):
        self.fill_exercise_frames(WorkoutType=1)





























