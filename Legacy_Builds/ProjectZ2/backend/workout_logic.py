class WorkoutLogic():
    def __init__(self, app):
        self.app = app

        self.current_workout_type1_plan = {
                        'exercises': [],
                        'exercise_sets': [],
                        'exercise_reps': [[]],
                        'exercise_times': [[]],
                        'sets_rest_times': [[]],
                        'exercise_rest_times': [],
                        'Type': []
                        }

        self.workout_done = {
                        'exercises': [],
                        'exercise_sets': [],
                        'exercise_reps': [[]],
                        'exercise_times': [[]],
                        'sets_rest_times': [[]],
                        'exercise_rest_times': [],
                        'Type': []
        }


        self.current_workout_type2_plan = {
            'exercises': [],
            'exercise_reps': [[]],
            'exercise_times': [[]],
            'rounds_number' : [],
            'rounds_rest':[],
            'Type': []

        }




        self.pulling_exercises = ["Pull ups",
                     "Chin ups",
                     "Rows",
                     "Archer Pull ups",
                     "Weighted Pull ups",
                     "OneArm Pull ups"
                                 ]
        self.pulling_timed = ["Dead Hangs"]

        self.pushing_exercises = ["Push ups",
                     "Diamond Push ups",
                     "Inclined Push ups",
                     "Declined Push ups",
                     "Weighted Push ups",
                     "OneArm Push ups",
                     "Pike Push ups",
                     "Advanced Pike Push ups",
                     "HandStand Push ups",
                     "Archer Push ups"
                                  ]

        self.pushing_timed = ["Handstand Hold",
                          "StraightArm Plank Hold",
                          "Pike Position Hold"
                              ]



        self.legs_exercises = ["BW Squats",
                     "BW Lunges",
                     "Weighted Squats",
                     "Weighted Lunges",
                     "Pistol Squats"
                               ]


        self.legs_timed = []



        self.abs_exercises = ["Hanging Knee Raises",
                     "Sit Ups",
                     "Toes To Bar"
                              ]


        self.abs_timed = ["L-Sit",
                          "Plank",
                          "Flutter Kicks",
                          "Bicycle Kicks",
                          "Dragon Flag"
                          ]




