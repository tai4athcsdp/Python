############### USE TUPLE TO RETURN STUDENT ###########################
# def main():
#     student = get_student()
#     student[0] = "Ron"
#     print(f"{student[0]} from {student[1]}")
# def get_student():
#     name = input("Name:")
#     house = input("House:")
#     return (name, house)

############### USE DICT TO RETURN STUDENT ###########################
# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")
# def get_student():
#     student = {}
#     student["name"] = input("Name:")
#     student["house"] = input("House:")
#     return student

############### USE CLASS TO RETURN STUDENT ###########################
# class Student:
#     ...
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
# def get_student():
#     student = Student()
#     student.name = input("Name:")
#     student.house = input("House:")
#     return student

############### CLASS INITIALIZE ####################################
# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
# def get_student():
#     name = input("Name:")
#     house = input("House:")
#     student = Student(name, house)
#     return student


########### RAISE KEY WORD ##################################################
# class Student:
#     def __init__(self, name, house):
#         if not name:  ## name == ""
#             raise ValueError("Missing name")
#         if house not in ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
# def get_student():
#     name = input("Name:")
#     house = input("House:")
#     return Student(name, house)
# if __name__ == "__main__":
#     main()

########### __str___  FUNCTION ##################################################
# class Student:
#     def __init__(self, name, house):
#         if not name:  ## name == ""
#             raise ValueError("Missing name")
#         if house not in ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house
#     def __str__(self):
#         return "a student"

# def main():
#     student = get_student()
#     print(student)
# def get_student():
#     name = input("Name:")
#     house = input("House:")
#     return Student(name, house)
# if __name__ == "__main__":
#     main()


########### charm() FUNCTION ##################################################
class Student:
    def __init__(self, name, house, patronus):
        if not name:  ## name == ""
            raise ValueError("Missing name")
        if house not in ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.partronus = patronus
    def __str__(self):
        return f"{self.name} from {self.house}"
    def charm(self):
        match self.partronus:
            case "Stag":
                return "Stag Patronus!"
            case "Otter":
                return "Otter Patronus!"
            case "Jack Russel terrier":
                return "Jack Patronus!"
            case _: 
                return "Oh la la!"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())
def get_student():
    name = input("Name:")
    house = input("House:")
    patronus = input("Patronus:")
    return Student(name, house, patronus)
if __name__ == "__main__":
    main()