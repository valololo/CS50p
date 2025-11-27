from datetime import date
from sys import exit
import inflect

def main():
    birthday = get_birthday()
    today = date.today()

    time_to_birthday = abs(birthday - today)
    p = inflect.engine()
    minutes = time_to_birthday.days * 24 * 60

    result = p.number_to_words(minutes)
    result = result.replace(" and ", " ")
    result = result.capitalize()

    print(result, "minutes")


def get_birthday():
    try:
        if birth := date.fromisoformat(input("Date of Birth: ")):
            return birth
    except ValueError:
        exit("Invalid date")


if __name__ == "__main__":
    main()
