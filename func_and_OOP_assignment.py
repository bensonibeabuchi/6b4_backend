# # QUESTION 1: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# result = []

# def divisible():
#     for num in range(2000, 3201):
#         if num % 7 == 0 and num % 5 != 0:
#             result.append(num)

# print(divisible())

# ################################################################################

# # QUESTION 2 With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.


# ################################################################################


# # QUESTION 3: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

# sequence = input("Enter different numbers: ")

# number_list = sequence.split(",")

# number_tuple = tuple(number_list)

# print("List:", number_list)
# print("Tuple:", number_tuple)

# ################################################################################

# # QUESTION 4: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

# results = []


# def even_numbers():
#     for num in range(1000, 3001):
#         if num % 2 == 0:
#             return num
#         results.append(num)


# print(even_numbers())


# ################################################################################

# # QUESTION 5: Write a program that accepts a sentence and calculate the number of letters and digits.Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10  DIGITS 3



# ################################################################################


# # QUESTION 6: Write a Python program to create a calculator class. Include methods for basic arithmetic operations. E.g addition, subtraction.

# class Calculator:

#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self):
#         return self.num1 + self.num2

#     def substract(self):
#         return self.num1 - self.num2

#     def multiply(self):
#         return self.num1 * self.num2

#     def divide(self):
#         return self.num1 / self.num2


# numbers = Calculator(3, 2)

# print(numbers.divide())

# ################################################################################

# # QUESTION 7; Write a Python program to create a class representing a Triangle. Include a method to calculate its area.


# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def calculate_area(self):
#         area = 0.5 * self.base * self.height
#         return area


# triangle1 = Triangle(4, 6)

# print(triangle1.calculate_area())

# ################################################################################

# QUESTION 8: In Python, a class is  blueprint for a concrete object.

# QUESTION 9: Object and class attributes are accessed using DOT notation in Python.


# QUESTION 10: In Python, a function within a class definition is called a: Method
