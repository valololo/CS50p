def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str):

    # Rule 1: starts with at least two letters
    for char in str[:2]:
        if not char.isalpha():
            return False

    # Rule 2: length between 2 and 6 characters
    if len(str) < 2 or len(str) > 6:
        return False

    # Rule 3: only letters and numbers
    for char in str:
        if not char.isalnum():
            return False

    # Rule 4: numbers at the end, no leading zeros
    digits_started = False

    for char in str[2:]:
        if char.isdigit():
            if not digits_started:
                if char == '0':
                    return False  # leading zero
                digits_started = True
        elif char.isalpha() and digits_started:
            return False  # letters after numbers

    return True


if __name__ == "__main__":
    main()
