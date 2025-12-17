############## PROBLEM: WE CAN INIT MULTIPLE HAT WItH BELOW CODE ####################################
# import random

# class Hat:
#     def __init__(self):
#         self.houses = ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))
# hat = Hat()
# hat.sort("Harry")

################## USE CLASSMETHOD ######################################################################
import random

class Hat:
    houses = ["Griffindor", "Hufflepuff", "RavenClaw", "Slytherin"]
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")