from validator_collection import checkers

def main():
    print(email(input("What is your email address? ")))


def email(str):
    if checkers.is_email(str):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()
