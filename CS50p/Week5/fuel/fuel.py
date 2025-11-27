def main():

    while True:
        tank = input("Fraction: ").strip()
        percent = convert(tank)

        if percent is None:
            continue
        else:
            break

    print(gauge(percent))


def convert(fraction):
    try:
        x, y = fraction.split("/")

        # Check if y is zero
        if int(y) == 0:
            raise ZeroDivisionError

        # Check if x and y are digits and valid
        if not x.isdigit() or not y.isdigit():
            raise ValueError

        # Check if x greater than y
        if int(x) > int(y):
            raise ValueError

        # Convert to integers and break loop
        return (int(x) / int(y)) * 100

    except ValueError:
        raise ValueError

def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
         return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
