from parser import f_inches
from converter import convert

feet_inches = input("enter feet and inches")

first_def = f_inches(feet_inches)
result = convert(first_def['feet'], first_def['inches'])
print(result)

if result < 1:
    print("kid is too small.")
else:
    print("kid can use the slide")