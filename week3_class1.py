# class Student:
#     name = ""
#     age = 0


# student_1 = Student()
# student_2 = Student()

# student_1.name = "Benson"
# student_1.age = 25

# print(f"Your name is {student_1.name}, you are {student_1.age} years old")

# print(f"Your name is {student_2.name}, you are {student_2.age} years old")

########################################################################################################################


# class Room:
#     lenght = 0
#     width = 0

#     def get_room_area(self):
#         return self.lenght * self.width


# joseph_room = Room()
# benson_room = Room()

# joseph_room.lenght = 200
# joseph_room.width = 300

# print(joseph_room.get_room_area())


########################################################################################################################


# class Room:
#     def __init__(self, lenght, breadth):
#         self.lenght = lenght
#         self.breadth = breadth

#     def get_room_area(self):
#         return self.lenght * self.breadth


# room_1 = Room(300, 200)

# print(room_1.get_room_area())


########################################################################################################################

# class Student:
#     school = "Univelcity"

#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#         self.email = first_name + last_name + "@gmail.com"

#     def get_profile(self):
#         return f"Your name is {self.first_name}"


# student_1 = Student("Prosper", "Edward")
# student_2 = Student("Benson", "Ibeabuchi")
# student_1.school = "Babcock"
# Student.school= "Unilag"

# print(student_1.school)
# print(student_1.first_name)
# print(student_1.email)
# print(student_2.school)


########################################################################################################################


# class Employee:
#     company = "Dangote"
#     raise_percentage = 1.10
#     def __init__(self, name, job, salary):
#         self.name = name
#         self.job = job
#         self.salary = salary

#     def bio(self):
#         return f"Hello {self.name}, your salary is {self.salary}"

#     def raisepercent(self):
#         self.salary = self.salary * self.raise_percentage
#         return f"Your new salary is {self.salary}"


# emp_1 = Employee("Princewill", "accountant", 3000000)
# emp_2 = Employee("Benson", "Founder", 500000000)

# print(emp_1.bio())
# print(emp_1.__dict__)
# print(emp_1.raisepercent())
# print(emp_1.salary)


########################################################################################################################

class Laptop:
    discount_percentage = 0.90

    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def get(self):

        return f"all the attribute is {self.__dict__}"
    
    def add_discount(self):
        self.price = self.price * self.discount_percentage
        return f" your new price is {self.price}"


laptop1 = Laptop("apple", 500000, "grey")
laptop2 = Laptop("HP", 20000, "blue")


print(laptop1.add_discount())
