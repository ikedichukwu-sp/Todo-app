feet_inches = input("enter feet, inch: eg. (3, 4): ")


def converter(feet_inches):
    feet, inch = feet_inches.strip("()").split(",")
    feet = int(feet.strip())
    inch = int(inch.strip())
    feet1 = feet * 0.3048
    inch1 = inch * 0.0254
    meter = feet1 + inch1
    return meter

n = converter(feet_inches)
print(n)
