import csv
from sys import argv
from sys import exit
from tabulate import tabulate

if len(argv) < 2:
    exit("Too few command-line arguments")

if len(argv) > 2:
    exit("Too many command-line arguments")

if argv[1].endswith(".csv") == False:
    exit("Not a CSV file")


def main():

    file_name = argv[1]
    lines = []

    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            for row in reader:
                lines.append(row)

    except FileNotFoundError:
        exit("File does not exist")

    print(tabulate(lines, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
