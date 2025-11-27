def main():

    # Dictionary to map month names to their respective numbers
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    while True:
        date = input("Date: ").strip().capitalize()

        try:
            # Check for MM/DD/YYYY format
            if "/" in date:
                month, day, year = date.split("/")

                # Validate that month, day, and year are numeric
                if not month.isdigit() or not day.isdigit() or not year.isdigit():
                    continue

                # Convert to integers
                month = int(month)
                day = int(day)
                year = int(year)

                # Validate month, day, and year ranges
                if not 0 < month <= 12 or not 0 < day <= 31 or not len(str(year)) == 4:
                    continue

                print(f"{year}-{month:02}-{day:02}")
                break

            # Check for Month DD, YYYY format
            elif date.startswith(tuple(months.keys())):
                month, day, year = date.split(" ")

                # Validate that day ends with a comma
                if not day.endswith(","):
                    continue

                day = day.rstrip(",")

                # Validate that day and year are numeric
                if not day.isdigit() or not year.isdigit():
                    continue

                # Convert to integers
                day = int(day)
                year = int(year)

                # Validate day, and year ranges
                if not 0 < day <= 31 or not len(str(year)) == 4:
                    continue

                print(f"{year}-{months[month]:02}-{day:02}")
                break

        except ValueError:
            continue


main()
