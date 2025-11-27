def main():

    while True:
        tank = input("Fraction: ").strip()

        # Validate input
        if "/" in tank:
            x, y = tank.split("/")

            # Check if x and y are digits and valid
            if not x.isdigit() or not y.isdigit():
                continue

            # Check if y is zero or x greater than y
            elif int(x) > int(y):
                continue
            elif int(y) == 0:
                continue

            # Convert to integers and break loop
            else:
                x = int(x)
                y = int(y)
                break

    # Calculate percentage
    percent = (x / y) * 100

    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{round(percent)}%")


main()
