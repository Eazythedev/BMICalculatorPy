weight = float(input("Weight(kg): "))
height = float(input("Height (m): "))

# BMI calculation
body_mass_index = weight / (height * height)

if body_mass_index < 18.5:
    print("Underweight")
elif body_mass_index > 25:
    print("Overweight")
else:
    print("Healthy weight")

print(f"Your Body Mass Index is {body_mass_index:.2f}.")
#     ^ f strings right there ^
