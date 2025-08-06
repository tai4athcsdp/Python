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
# def meow(n : int):
#     for _ in range(n):
#         print("meow")

# number = input("Number: ")
# meow(number)

################ COMMAND LINE ARRGUMENT ################################
# import sys

# if len(sys.argv) == 1: 
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     print("meow\n" * n, end="")
# else:
#     print("usage: meow.py")
################ COMMAND LINE ARRGUMENT WITH ARGPARSE LIBRARY ################################
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default= 1,  help= "Number of time to meow", type=int)
arg = parser.parse_args()

for _ in range(arg.n):
    print("Meow")
