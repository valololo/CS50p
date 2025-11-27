ex = input("Expression: ")

x, y, z = ex.split(" ")

x = float(x)
z = float(z)

if y == "+":
    result = float(x + z)
    print(f"{result:.1f}")
elif y == "-":
    result = float(x - z)
    print(f"{result:.1f}")
elif y == "*":
    result = float(x * z)
    print(f"{result:.1f}")
else:
    result = float(x / z)
    print(f"{result:.1f}")
