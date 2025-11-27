from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if (len(sys.argv) not in [1, 3]):
    sys.exit("Invalid usage")

if len(sys.argv) == 1:

    rdmFont = input("Input: ")

    figlet = Figlet(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(rdmFont))
    sys.exit()


if (sys.argv[1] not in ["-f", "--font"]):
    sys.exit("Invalid usage")

if (sys.argv[2] not in figlet.getFonts()):
    sys.exit("Invalid usage")

if len(sys.argv) == 3:
    spcFont = input("Input: ")
    font = sys.argv[2]

    figlet = Figlet(font=font)
    print(figlet.renderText(spcFont))
