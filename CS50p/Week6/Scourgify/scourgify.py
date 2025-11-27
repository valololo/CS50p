import csv
from sys import argv
from sys import exit

if len(argv) < 2:
    exit("Too few command-line arguments")

if len(argv) > 3:
    exit("Too many command-line arguments")

if argv[1].endswith(".csv") == False and argv[2].endswith(".csv"):
    exit("Not a CSV file")


def main():

    file_name = argv[1]
    students = []

    try:
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:

                last, first = row["name"].split(",")
                first = first.strip()

                students.append({"first": first, "last": last, "house": row["house"]})

    except FileNotFoundError:
        exit("Could not read " + file_name)

    print_file = argv[2]

    with open(print_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow({"first": student['first'],
                            "last": student['last'], "house": student['house']})


if __name__ == "__main__":
    main()
