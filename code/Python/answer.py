#!/usr/bin/env python3

import calendar
import json
from datetime import datetime

from TimeExercise import TimeExercise

# Load data
with open('../../data/users.json') as json_file:
    users = json.load(json_file)

with open('../../data/exercises.json') as json_file:
    exercises = json.load(json_file)

with open('../../data/workouts.json') as json_file:
    workouts = json.load(json_file)


    def idToAthleteName():
        idToAthlete = {}
        for user in users:
            idToAthlete[user['id']] = f"{user['name_first']} {user['name_last']}"
        return idToAthlete


    def processWorkouts(workouts):
        idToAthlete = idToAthleteName()
        athletes = {}
        for workout in workouts:
            userId = workout['user_id']
            athleteName = idToAthlete.get(userId, 'unknown')
            time = workout["datetime_completed"]
            blocks = workout["blocks"]
            timeExercises = TimeExercise.createTimeExerciseFromBlocks(blocks, time, exercises)
            if athleteName not in athletes:
                athletes[athleteName] = []
            athletes[athleteName].extend(timeExercises)
        return athletes


    def q1(athletes):
        total = 0
        for timeExercises in athletes.values():
            for timeExercise in timeExercises:
                exerciseName = timeExercise.exerciseName
                if exerciseName == "Bench Press":
                    total += timeExercise.totalAndPr.total
        return total


    def q2(athletes):
        barryMoore = athletes["Barry Moore"]
        total = 0
        for timeExercises in barryMoore:
            exerciseName = timeExercises.exerciseName
            time = timeExercises.time
            if exerciseName == "Back Squat":
                dateFormat = "%Y-%m-%d %H:%M:%S"
                dateObject = datetime.strptime(time, dateFormat)
                if dateObject.year == 2016:
                    total += timeExercises.totalAndPr.total
        return total


    def q3(athletes):
        barryMoore = athletes["Barry Moore"]
        monthTotals = {}
        for timeExercises in barryMoore:
            exerciseName = timeExercises.exerciseName
            time = timeExercises.time
            if exerciseName == "Back Squat":
                dateFormat = "%Y-%m-%d %H:%M:%S"
                dateObject = datetime.strptime(time, dateFormat)
                if dateObject.year == 2017:
                    month = dateObject.month
                    monthTotals[month] = monthTotals.get(month, 0) + timeExercises.totalAndPr.total

        maxMonth = max(monthTotals, key=monthTotals.get)
        return calendar.month_name[maxMonth]


    def q4(athletes):
        abbySmith = athletes["Abby Smith"]
        pr = 0
        for timeExercises in abbySmith:
            exerciseName = timeExercises.exerciseName
            if exerciseName == "Bench Press":
                pr = max(pr, timeExercises.totalAndPr.pr)
        return pr


    # Collect answers
    def buildAnswer(athletes):
        q1Answer = q1(athletes)
        q2Answer = q2(athletes)
        q3Answer = q3(athletes)
        q4Answer = q4(athletes)
        answers = {
            # In total, how many pounds have these athletes Bench Pressed?
            'q1': q1Answer,

            # How many pounds did Barry Moore Back Squat in 2016?
            'q2': q2Answer,

            # In what month of 2017 did Barry Moore Back Squat the most total weight?
            'q3': q3Answer,

            # What is Abby Smith's Bench Press PR weight?
            # PR defined as the most the person has ever lifted for that exercise, regardless of reps performed.
            'q4': q4Answer
        }
        return answers


    athletes = processWorkouts(workouts)
    answers = buildAnswer(athletes)
    print(json.dumps(answers))
