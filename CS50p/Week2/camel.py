camel = input("camelCase: ").strip()
snake = []

for char in camel:
    if char.isupper():
        snake.append("_" + char.lower())
    else:
        snake.append(char)

print("snake_case: " + "".join(snake))
