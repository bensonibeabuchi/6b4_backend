dict1 = {0: 10, 1: 20}

dict1[2] = 3

print(dict1)


dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

concatenated_dict = {}

concatenated_dict.update(dict1)

concatenated_dict.update(dict2)

concatenated_dict.update(dict3)

print(concatenated_dict)
