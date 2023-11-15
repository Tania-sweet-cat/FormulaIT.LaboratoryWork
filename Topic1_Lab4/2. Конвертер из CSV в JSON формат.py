import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as input_file:
        input_data = [current_dict for current_dict in csv.DictReader(input_file)]

    with open(OUTPUT_FILENAME, "w") as output_file:
        json.dump(input_data, output_file, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
