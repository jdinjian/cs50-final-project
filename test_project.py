import project

ocean = [
    {"fish": "Shark", "expected": 3, "population": 3},
    {"fish": "Tuna", "expected": 9, "population": 9},
    {"fish": "Mackerel", "expected": 27, "population": 27},
    {"fish": "Anchovy", "expected": 81, "population": 81},
    ]

pop_healthy = [3, 9, 27, 81]

def test_change_location():
    assert project.change_location("lake") == "lake"
    assert project.change_location("ocean") == "ocean"
    assert project.change_location("river") == "river"
    assert project.change_location("anything") == None


def test_get_pop_value():
    assert round(project.get_pop_value(0, ocean)) == 0
    assert round(project.get_pop_value(1, ocean)) == 0
    assert round(project.get_pop_value(2, ocean)) == 0

def test_calculate_health():
    assert project.calculate_health(ocean) == "healthy"

