
# line1 = "uio"
# line4 = "hjg"

# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))

# def BMI(weight, height):
#     bmi_value = weight / (height ** 2)
#     print(bmi_value)

#     print(round(bmi_value))

#     if bmi_value < 18.5:
#         print("Underweight")
#     elif bmi_value in range(18, 24):
#         print("Normal")
#     elif bmi_value in range(25, 29):
#             print("Overweight")
#     else:
#          print("Obese")

# BMI(weight, height)

table = []


def multiply(num1):
    for i in range(1, 13):
        multiply = num1 * i
        table.append(multiply)
    return table


print(multiply(5))
