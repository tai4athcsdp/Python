################## FILTER ################################
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"}
# ]

# def is_gryffindor(student):
#     return student["house"] == "Gryffindor"

# gryfindors = filter(is_gryffindor, students)

# for gryfindor in sorted(gryfindors, key = lambda s : s["name"]):
#     print(gryfindor["name"])

##################### LIST CONPREHENSION ########################

# students = ["Hermione", "Harry", "Ron"]

# gryfindors = [{"name": student, "house": "Gryffindor"} for student in students]

# print(gryfindors)

####################### DICTIONARY COMPREHENSION ########################

# students = ["Herminone", "Harry", "Ron"]
# gryffindors = {student: "Gryffindor" for student in students}
# print(gryffindors)


####################### Enumerate ########################
# students = ["Hermione", "Harry", "Ron"]
# for i, student in enumerate(students):
#     print(i+1, student)

####################### GENERATOR ########################
# def main():
#     n = int(input("What's n? "))
#     for s in sheep(n): 
#         print(s)
# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * n)
#     return flock
# if __name__ == "__main__":
#     main()

####################### YEILD ########################
def main():
    n = int(input("What's n? "))
    for s in sheep(n): 
        print(s)
def sheep(n):
    for i in range(n):
        yield ("🐑" * i)
if __name__ == "__main__":
    main()