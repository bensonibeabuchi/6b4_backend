# class Humans:
#     eyes = 2
#     legs = 2
#     nose = 1

#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def profile(self):
#         return f"Hello {self.name}, you are {self.age} years old."


# human_1 = Humans("prosper", 50, "Male")
# human_2 = Humans("Ella", 80, "Female")

# print(human_1.profile())


# class African(Humans):
#     skin_color = "black"

#     def __init__(self, name, age, gender, country):
#         super().__init__(name, age, gender)
#         self.country = country

#     def profile(self):
#         return f"Hello {self.name}, you are {self.age} years old and from {self.country}"


# guy_1 = African("evans", 50, "Male", "Nigeria")
# guy_2 = African("Benson", 32, "Cis-Male", "Nigeria")

# print(guy_1.profile())


########################################################################################################################


# class Employee:
#     raise_percentage = 1.20

#     def __init__(self, name, job, salary):
#         self.name = name
#         self.job = job
#         self.salary = salary
#         self.email = name + "@univelcity.com"

#     def increase_salary(self):
#         self.salary = self.salary * self.raise_percentage
#         return self.salary

# class Developer(Employee):
#     raise_percentage = 1.30
#     def __init__(self, name, job, salary, stack):
#         super().__init__(name, job, salary)
#         self.stack = stack

#     def increase_salary(self):
#         self.salary = self.salary * self.raise_percentage
#         return self.salary

# class Marketer(Employee):
#     raise_percentage = 1.25
#     def __init__(self, name, job, salary):
#         super().__init__(name, job, salary)

#     def increase_salary(self):
#         return super().increase_salary()

# m_1 = Marketer("Kola", "Marketer", 1000)

# print(m_1.increase_salary())

########################################################################################################################

class Vehicles:
    no_of_tyres = 4
    no_of_mirrors = 3

    def __init__(self, brand, mileage, year):
        self.brand = brand
        self.mileage = mileage
        self.year = year

class Bus(Vehicles):
    
