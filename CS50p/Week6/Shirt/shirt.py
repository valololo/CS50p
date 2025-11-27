from sys import argv
from sys import exit
from PIL.Image import open
from PIL.ImageOps import fit


if len(argv) < 3:
    exit("Too few command-line arguments")

if len(argv) > 3:
    exit("Too many command-line arguments")


def main():
    try:
        input_image = open(argv[1])
        shirt = open("shirt.png")
    except FileNotFoundError:
        exit("Input does not exist")

    size = shirt.size
    input_image = fit(input_image, size=size)

    input_image.paste(shirt, (0, 0), shirt)
    input_image.save(argv[2])


def check_file_input(file1, file2):

    for file in [file1, file2]:
        if not file.endswith((".jpg", ".jpeg", ".png")):
            exit("Invalid input" if file == file1 else "Invalid output")

    if file1.split(".")[-1] != file2.split(".")[-1]:
        exit("Input and output have different extensions")


check_file_input(argv[1], argv[2])

if __name__ == "__main__":
    main()
