import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        # numbers from 1-255, no leading zeros
        numbers = ip.split(".")
        if not len(numbers) == 4:
            return False
        for number in numbers:
            if not int(number) < 256:
                return False
            if re.search(r"0\d", number):
                return False
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
