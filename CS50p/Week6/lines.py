from sys import argv
from sys import exit

if len(argv) < 2:
    exit("Too few command-line arguments")

if len(argv) > 2:
    exit("Too many command-line arguments")

if argv[1].endswith(".py") == False:
    exit("Not a Python file")


def main():

    file_name = argv[1]
    lines = 0

    try:
        with open(file_name) as file:
            for line in file:

                if line.strip().startswith("#") == True:
                    continue

                if line.strip() == "":
                    continue

                lines += 1

    except FileNotFoundError:
        exit("File does not exist")

    print(lines)


if __name__ == "__main__":
    main()
