from TimeExercise import TimeExercise


def testTimeExercise():
    exercises = [
        {
            "id": 326,
            "title": "Back Squat"
        },
        {
            "id": 568,
            "title": "Bench Press"
        },
        {
            "id": 797,
            "title": "Lat Pulldown"
        }
    ]
    time = "2018-03-05 06:42:13"
    blocks = [
            {
                "exercise_id": 568,
                "sets": [
                    {
                        "reps": 3,
                        "weight": 0
                    },
                    {
                        "reps": 6,
                        "weight": 160
                    }
                ]
            },
            {
                "exercise_id": 568,
                "sets": [
                    {
                        "reps": 1,
                        "weight": 155
                    },
                    {
                        "reps": 3,
                        "weight": None
                    },
                    {
                        "reps": 9,
                        "weight": 145
                    }
                ]
            },
            {
                "exercise_id": 797,
                "sets": [
                    {
                        "reps": 12,
                        "weight": None
                    },
                    {
                        "reps": 4,
                        "weight": 145
                    },
                    {
                        "reps": 1,
                        "weight": 155
                    },
                    {
                        "reps": 0,
                        "weight": 160
                    }
                ]
            }
        ]
    result = TimeExercise.createTimeExerciseFromBlocks(blocks, time, exercises)
    assert len(result) == 2, f"Expected 2 exercises, got {len(result)}"

    # Find the exercises by name
    bench_press = next((ex for ex in result if ex.exerciseName == "Bench Press"), None)
    lat_pulldown = next((ex for ex in result if ex.exerciseName == "Lat Pulldown"), None)

    # Assert Bench Press calculations
    assert bench_press is not None, "Bench Press exercise not found"
    assert bench_press.time == time
    assert bench_press.totalAndPr.total == 2420, f"Expected Bench Press total 2420, got {bench_press.totalAndPr.total}"
    assert bench_press.totalAndPr.pr == 160, f"Expected Bench Press PR 160, got {bench_press.totalAndPr.pr}"

    # Assert Lat Pulldown calculations
    assert lat_pulldown is not None, "Lat Pulldown exercise not found"
    assert lat_pulldown.time == time
    assert lat_pulldown.totalAndPr.total == 735, f"Expected Lat Pulldown total 735, got {lat_pulldown.totalAndPr.total}"
    assert lat_pulldown.totalAndPr.pr == 155, f"Expected Lat Pulldown PR 155, got {lat_pulldown.totalAndPr.pr}"
testTimeExercise()