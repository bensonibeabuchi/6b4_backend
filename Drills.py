# first_name = "Benson"
# last_name = "Ibeabuchi"

# # print(len(last_name))
# # print(last_name[-3:])

# # list is identified with square brackets. a list permits different types of values inside

# numbers = [2, 4, [6, 8], 10]
# numbers[0] = 3
# # print(numbers)

# a = [9, 3, 8]
# b = [4, 5, 6]

# c = a + b

# # print (c)
# # print(a+b)


# a.sort(reverse=True)
# # print(a)

# students = ["Jamiu", "Benson", "Princewill", "Kola", "Samuel", "Joseph"]

# # a code that displays the number of elements in the list
# # change the 2nd element in the list to prosper
# # Remove my name from the list
# # add a new list ["Esther", "Valerie"]
# # return the first 3 elements of the student list
# # the last 3 elements of the student list

# print(len(students))

# students[1] = "prosper"

# print(students)

# students.pop(1)
# print(students)


# new_student = ["Esther", "Valerie"]
# students.extend(new_student)

# print(students)


# print(students[0: 3])

# print(students[-3:])


# var1 = ("Prosper")
# var2 = ("Prosper",)

# print(type(var1))
# print(type(var2))

# letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# print(letters[2:5])
# print(letters[4:7])
# print(letters[-3:])
# print(letters[1:4])
# print(letters[:3])
# print(letters[:])

# a = 5
# b = 5
# print(a == b)


#     print(students)


# create a function called dailyPayment that accepts parameters called (hoursWorked)
# create a variable called payment

################################################################################################################################

# rates = int(input('Whats is your Rate?:  '))
# hoursWorked = int(input('How long did you work today?: '))


# def dailyPayment(hoursWorked):
#     wages = hoursWorked * rates
#     return f"Your wages for today is ₦{wages}"


# print(dailyPayment(hoursWorked))


################################################################################################################################


# def citizen(country="Nigeria"):
#     return f"You are from {country}"


# print(citizen())
# print(citizen("Canadian"))


################################################################################################################################

# paidWorkers = ["Benson"]

# bricklayer = 1000
# tiler = 1500
# painter = 2000
# plumber = 2500

# jobDescription = int(
#     input('Job Description (1: Bricklayer, 2: Tiler, 3: Painter, 4: Plumber): '))
# hoursWorked = int(input('How long did you work today?: '))
# nameOfWorker = input('Wetin be your name?: ')

# if nameOfWorker not in paidWorkers:
#     paidWorkers.append(nameOfWorker)

# else:
#     print("You be THIEF")


# if jobDescription == 1:
#     jobDescription = bricklayer
# elif jobDescription == 2:
#     jobDescription = tiler
# elif jobDescription == 3:
#     jobDescription = painter
# elif jobDescription == 4:
#     jobDescription = plumber


# def payment(hoursWorked):
#     wages = hoursWorked * jobDescription
#     return f"Your wages for today {nameOfWorker} is ₦{wages}"


# print(payment(hoursWorked))

################################################################################################################################


# listOfWorkers = ["Benson", "Princewill", "Rashford"]
# newList = []


# def backwards():

#     for value in range(len(listOfWorkers)):
#         newList.append(listOfWorkers.pop())

#     return newList


# print(backwards())


# list1 = [1,2,3,4,5,5,6,6,7,1,8,9,2,3,5]
# list2 = []

# def unique():
#     for values in list1:
#         if values % 2 == 0:
#             list2.append(values)
#     print(list2)


# unique()


################################################################################################################################

# studentList = []


# def registrations():
#     count = 0
#     while count < 2:
#         name = input("Write your name here: ")

#         age = int(input('Please enter your age: '))
#         gender = int(input('Please enter your gender: '))

#         if gender == 1:
#             gender = 'Male'
#         elif gender == 2:
#             gender = 'Female'

#         courses = int(input('Please enter your class: '))

#         if courses == 1:
#             courses = "Backend"
#         elif courses == 2:
#             courses = "Frontend"
#         elif courses == 3:
#             courses = "Product Design"
#         elif courses == 4:
#             courses = "Data Analysis"

#         if name not in studentList:
#             studentList.append(name)
#         else:
#             print("You have already registered")
#         count += 1
#         print(studentList)

#     print(
#         f"Hello {name}, you are {gender} and {age} years old, and your class is {courses}")


# registrations()


################################################################################################################################

# list = []
# name = "school"


# def reverse():
#     for i in name:
#         list.append(name.pop())
#     return list


# print(list)


name = "School"
newList = []


def backwards():

    for i in name:
        newList.append(name.pop())

    return newList


print(backwards())
