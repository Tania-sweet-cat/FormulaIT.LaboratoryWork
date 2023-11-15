import json


INPUT_FILE = "input.json"


def task() -> float:
    with open(INPUT_FILE) as file:
        json_data = json.load(file)

    sum_values = sum(current_dict["score"] * current_dict["weight"] for current_dict in json_data)
    return round(sum_values, 3)


print(task())
