x = input("Greeting: ").strip()

if x.lower() == "hello" or x.lower().startswith("hello"):
    print("$0")
elif x.lower().startswith("h"):
    print("$20")
else:
    print("$100")
