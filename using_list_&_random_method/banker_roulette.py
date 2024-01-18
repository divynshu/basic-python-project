#Banker roulete _it is just who will going to pay the bill
import random


# Split string method
names_string = input("Give me everybody's names, separated by a comma and a space.\n")
names = names_string.split(", ")


numberList = len(names)


random_Num = random.randint (0,numberList - 1)

theChoice = names[random_Num]

print(f"{theChoice} is going to buy the meal today!")