########## USE GLOBAL CONSTANT #########################
# MEOW = 3
# for _ in range(MEOW):
#     print("meow")

################## CLASS CONSTANT ######################
# class Cat:
#     MEOW = 3
#     def meow(self):
#         for _ in range(Cat.MEOW):
#             print("meow")

# cat = Cat()
# cat.meow()

################ TYPE HINT ################################
def meow(n : int):
    for _ in range(n):
        print("meow")

number = input("Number: ")
meow(number)