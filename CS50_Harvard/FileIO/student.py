# with open("student.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

############with sorted funtion##################
# students = []
# with open("student.txt") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)

################store infomation in dictionary######################
# students = []
# with open("student.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# for student in students:
#     print(f"{student['name']} is in {student['house']}")

#####################sorted with lambda function ==========================
# students = []
# with open("student.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

#################use csv library################################
# import csv
# students = []

# with open("home.csv") as file:
#         reader = csv.reader(file)
#         for name, home in reader:
#             students.append({"name": name, "home": home})

# for student in sorted(students, key = lambda student: student['home']):
#     print(f"{student['name']} is from {student['home']}")

#####################use DictReader() function##############################
# import csv
# students = []
# with open("home.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key = lambda student : student["name"]):
#     print(f"{student['name']} is from {student['home']}")

########## WRITE TO THE FILE  ################################
import csv
name = input("What 's your name?")
home = input("Wher 's your home?")

with open("home.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["home", "name"])
    writer.writerow({"home": home, "name": name})
