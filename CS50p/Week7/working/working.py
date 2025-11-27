import re


def main():
    print(convert(input("Hours: ")))


def convert(time):
    am_times = {"12": "00:00", "1": "01:00", "2": "02:00", "3": "03:00", "4": "04:00", "5": "05:00", "6": "06:00",
                "7": "07:00", "8": "08:00", "9": "09:00", "10": "10:00", "11": "11:00"}
    pm_times = {"12": "12:00", "1": "13:00", "2": "14:00", "3": "15:00", "4": "16:00", "5": "17:00", "6": "18:00",
                "7": "19:00", "8": "20:00", "9": "21:00", "10": "22:00", "11": "23:00"}

    if match := re.search(r"^(1[0-2]|\d)(?::00)? (AM|PM) to (1[0-2]|\d)(?::00)? (AM|PM)$", time):
        order = [match.group(2), match.group(4)]

        if order.index("AM") < order.index("PM"):
            return f"{am_times[match.group(1)]} to {pm_times[match.group(3)]}"
        else:
            return f"{pm_times[match.group(1)]} to {am_times[match.group(3)]}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
