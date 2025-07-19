# name = input("What 's your name?")

# file = open("name.txt", "a")
# file.write(f"{name}\n")
# file.close()

# with open("name.txt", "a") as file:
#     file.write(f"{name}\n")

##############################
#read the file

#way1
# with open("name.txt") as file:
#     lines = file.readlines()
# for line in lines:
#     print(f"hello, {line.rstrip()}")

#way2
# with open("name.txt") as file:
#     for line in file:
#         print(f"hello, {line.strip()}")

#way3: with "sorted" function
names= []
with open("name.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}")

##############################