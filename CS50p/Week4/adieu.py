from sys import exit

names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break

if not len(names) > 0:
    exit()

print("\nAdieu, adieu, to ", end="")

if len(names) == 1:
    print(names[0])
    exit()

if len(names) == 2:
    print(f"{names[0]} and {names[1]}")
    exit()

amount = len(names) - 1

for name in names[:amount]:
    print(f"{name}, ", end="")

print(f"and {names[(len(names) - 1)]}")
