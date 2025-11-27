import random
import cs50


def main():

    level = get_level()

    # Initialize counters for successful and failed attempts
    succ = 0
    fail = 0

    while (succ + fail) < 10:

        # Generate two random integers based on the selected level
        x = generate_integer(level)
        y = generate_integer(level)

        # Initialize solution status and wrong attempt counter
        solution = False
        wrong = 0

        # Prompt the user for the answer until the correct solution is provided or attempts are exhausted
        while solution == False:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                succ += 1
                solution = True
            else:
                if wrong < 2:
                    wrong += 1
                    print("EEE")
                else:
                    print(f"EEE\n{x} + {y} = {x + y}")
                    fail += 1
                    solution = True

    print(f"Score: {succ}")


def get_level():

    # Prompt the user for a level until a valid level is entered
    while True:

        n = cs50.get_int("Level: ")

        if n in [1, 2, 3]:
            return n


def generate_integer(level):

    # Define the range of numbers for each level
    levels = {
        1: (0, 9),
        2: (10, 99),
        3: (100, 999)
    }

    a, b = levels[level]

    return random.randint(a, b)


if __name__ == "__main__":
    main()
