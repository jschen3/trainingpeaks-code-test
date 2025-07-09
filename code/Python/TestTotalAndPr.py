from TotalAndPr import TotalAndPr

def test_total_and_pr_calculation():
    """Test that TotalAndPr correctly calculates total weight and PR."""
    block = {
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
    }
    
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
    
    total_and_pr = TotalAndPr(block, exercises)
    
    # Test total calculation: 6 reps * 160 weight = 960
    assert total_and_pr.total == 6 * 160
    # Test PR calculation: max weight should be 160
    assert total_and_pr.pr == 160


def test_total_and_pr_with_zero_weight():
    """Test that zero weight sets are handled correctly."""
    block = {
        "exercise_id": 568,
        "sets": [
            {
                "reps": 5,
                "weight": 0
            },
            {
                "reps": 3,
                "weight": 100
            }
        ]
    }
    
    exercises = [
        {
            "id": 568,
            "title": "Bench Press"
        }
    ]
    
    total_and_pr = TotalAndPr(block, exercises)
    
    # Total should be 0*5 + 100*3 = 300
    assert total_and_pr.total == 300
    # PR should be max(0, 100) = 100
    assert total_and_pr.pr == 100


def test_total_and_pr_with_none_weight():
    """Test that None weight values are treated as 0."""
    block = {
        "exercise_id": 568,
        "sets": [
            {
                "reps": 4,
                "weight": None
            },
            {
                "reps": 2,
                "weight": 150
            }
        ]
    }
    
    exercises = [
        {
            "id": 568,
            "title": "Bench Press"
        }
    ]
    
    total_and_pr = TotalAndPr(block, exercises)
    
    # Total should be 0*4 + 150*2 = 300
    assert total_and_pr.total == 300
    # PR should be max(0, 150) = 150
    assert total_and_pr.pr == 150

test_total_and_pr_calculation()
test_total_and_pr_with_none_weight()
test_total_and_pr_with_zero_weight()