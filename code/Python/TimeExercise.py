from TotalAndPr import TotalAndPr


def updateTotalAndPr(existingTotalAndPr, curTotalAndPr):
    return TotalAndPr(
        existingTotalAndPr.exerciseName,
        existingTotalAndPr.total + curTotalAndPr.total,
        max(existingTotalAndPr.pr, curTotalAndPr.pr)
    )


class TimeExercise:
    def __init__(self, time, totalAndPr):
        self.time = time
        self.totalAndPr = totalAndPr
        self.exerciseName = totalAndPr.exerciseName

    @staticmethod
    def createTimeExerciseFromBlocks(blocks, time, exercises):
        exercisesMap = {}
        for block in blocks:
            curTotalAndPr = TotalAndPr.createTotalAndPr(block, exercises)
            curExerciseName = curTotalAndPr.exerciseName
            if curExerciseName in exercisesMap:
                exercisesMap[curExerciseName] = updateTotalAndPr(exercisesMap[curExerciseName],
                                                                 curTotalAndPr)
            else:
                exercisesMap[curExerciseName] = curTotalAndPr

        timeExercises = []
        for singleExercise in exercisesMap:
            timeExercises.append(TimeExercise(time, exercisesMap[singleExercise]))
        return timeExercises
