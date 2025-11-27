dollars = "$15"

f = float(dollars.removeprefix("$"))

tip = "20%"

e = "0." + tip.removesuffix("%")
e = float(e)

print(f)
print(e)

