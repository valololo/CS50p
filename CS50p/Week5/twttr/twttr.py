def main():
    tweet = input("Input: ")
    print("Output: " + shorten(tweet))


def shorten(word):
    vowel = "aeiou"
    shrtnd = ""

    for char in word:
        if char.lower() not in vowel:
            shrtnd += char

    return shrtnd

if __name__ == "__main__":
    main()
