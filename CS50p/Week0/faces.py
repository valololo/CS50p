def main():
    smiley = convert(input("Smile for me! "))
    print(smiley)

def convert(phrase):
    phrase = phrase.replace(":)", "🙂")
    phrase = phrase.replace(":(", "🙁")
    return phrase
    
main()
