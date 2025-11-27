tweet = input("Input: ")
vowel = "aeiou"
omitted = []

for char in tweet:
    if char.lower() not in vowel:
        omitted.append(char)

print("Output: " + "".join(omitted))
