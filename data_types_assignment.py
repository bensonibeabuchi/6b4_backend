
from functools import reduce
from operator import mul

# 6B4 BACKEND QUIZ on DATA TYPES

# 1. Write a Python script to add a key to a dictionary.


dict1 = {0: 10, 1: 20}

dict1[2] = 30

print(dict1)


print(" ")


# 2.  Write a Python script to concatenate the following dictionaries to create a new one.


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic4 = {}

dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)

print(dic4)


print(" ")


# 3.  Write a Python script to check whether a given key already exists in a dictionary. (Use any dictionary as an example)


key_to_check = "name"

my_dict = {"name": "John", "age": 30, "city": "New York"}

if key_to_check in my_dict:
    print(f"{key_to_check} exists")
else:
    print(f"{key_to_check} doesn't exists")


print(" ")


# 4.  Write a Python program to iterate over dictionaries using for loops.
#  (Use any dictionary as an example)

my_dict2 = {"surname": "Doe", "how old": 30, "country": "Japan"}


for x, y in my_dict2.items():
    print(x, y)


print(" ")


My_list = [34, 56, 78, 976, 45, 23, 46, 788, 244]

# 5. Write a Python program to sum up all the items in a list.

sum_list = sum(My_list)

print(sum_list)

print(" ")

# 6. Write a Python program to multiply all the items in a list.


def multiply_list(My_list):
    result = 1
    for x in My_list:
        result = result * x
    return result


print(multiply_list(My_list))


print(" ")


# 7. Write a Python program to get the largest number from a list.

max_list = max(My_list)

print(max_list)

print(" ")

# 8. Write a Python program to get the largest number from a list.

min_list = min(My_list)

print(min_list)

print(" ")
