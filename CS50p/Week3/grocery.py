def main():

    # Initialize an empty dictionary to store grocery items and their counts
    groceries = {}

    while True:
        try:
            item = input().strip().upper()

            # Insert item into dictionary or update its count
            if not item in groceries:
                groceries[item] = 1
            else:
                groceries[item] += 1

        except EOFError:
            break

    # Print items and their counts in alphabetical order
    for key, value in sorted(groceries.items()):
        print(value, key)


main()
