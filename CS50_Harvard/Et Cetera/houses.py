########### FIND UNIQUE HOUSE IN LIST OF DICT USE FOR LOOP #######################
# students = [
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"}
# ]

# houses = []

# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])

# for house in houses:
#     print(house)

################## USE SET DATA TYPE ###########################################
students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

houses = set()

for student in students:
        houses.add(student["house"])

for house in houses:
    print(house)