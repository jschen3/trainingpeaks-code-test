class TotalAndPr:
    def __init__(self, exerciseName, total, pr):
        self.exerciseName = exerciseName
        self.total = total
        self.pr = pr

    @staticmethod
    def createTotalAndPr(block, exercises):
        idToExercise = {}
        for exercise in exercises:
            idToExercise[exercise["id"]] = exercise["title"]
        exercise_name = idToExercise[block["exercise_id"]]
        total = 0
        pr = 0
        for set in block["sets"]:
            weight = 0 if set["weight"] is None else set["weight"]
            total += weight * set["reps"]
            if set["reps"] > 0:
                pr = max(weight, pr)
        return TotalAndPr(exercise_name, total, pr)
