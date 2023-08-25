#A modulo is mathematical operator in python it divides a number by another number and gives you the remainder.
#It is represented with the percent sign (%)

#Day 3 Interactive Coding Exercise Odd or Even

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")
print("\n")

#Interactive Coding Exercise BMI 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your height in kg: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print ("normal weight")
elif bmi < 30:
    print("slightlyt overweught")
elif bmi < 35:
    print("obese")
else:
    print("clinically obese")

print("\n")

#Interactive Coding Exercise Leap Year

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    print("leap year")
elif year % 100 == 0:
    print("not leap year")
elif year % 400 == 0:
    print("leap year")
else:
    print("not a leap year")

print("\n")

#Interactive Coding Exercise Pizza Order Practice

print("Welome to python pizza Deliveries")

size = input("What size pizza do you want? S M or L ")
add_peperoni = input("Do you want peperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size ==  "S":
    bill += 15
    if add_peperoni == "Y":
        bill += 2
    elif add_peperoni == "N":
        bill += 0
    if extra_cheese == "Y":
        bill += 1
    elif extra_cheese == "N":
        bill += 0
    print(f"your total bill is ${bill}")
if size  == "M":
    bill += 20
    if add_peperoni =="Y":
        bill += 3
    elif add_peperoni == "N":
        bill += 0
    if extra_cheese == "Y":
        bill += 1
    elif extra_cheese == "N":
        bill += 0
    print(f"your total bill is ${bill}")
if size == "L":
    bill += 25
    if add_peperoni == "Y":
        bill += 3
    elif add_peperoni == "N":
        bill += 0
    if extra_cheese == "Y":
        bill += 1
    else:
        bill += 0
    print(f"Your total balance is ${bill}")

print("\n")

#Interactive Coding Exercise Love Calculator

print("Welcome to the Love Calculator")
name1 = input("What is you name? \n").lower()
name2 = input("What is their name? \n").lower()

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")
total_true = t + r + u + e
str_true = str(total_true)

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")
total_love = l + o + v + e
str_love = str(total_love)
subs_score = str_true[0] + str_love[0]
int_subs = int(subs_score)

if int_subs <= 10:
    print(f"your score is {int_subs} you go together like coke and mentos")
elif int_subs > 40 and int_subs <= 50:
    print(f"your score is {int_subs} you are alright together")
else:
    print(f"your score is {int_subs}")

#the string.count() function is used to count for the input substring in the particular string.

print("\n")

#Day 3 Project Treasure Island

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcom to the Treasure Island")
print("your mission is to find the treasure")

left = input("You are in the middle of a road, which way would you go? left or right: ").lower()

if left == "left":
    wait = input("You are now at the beach shore, you are being chased by the warlords, what will you do? swim or wait: ").lower()
    if wait == "wait":
        yellow_door = input("You are at an unknown location with three doors, red,blue and yellow, which door will you go through: ").lower()
        if yellow_door == "yellow":
            print("congratulations you found the treasure")
        else:
            print("NOOOOOO!!!! you went through the wrong door game over")
    elif wait == "swim":
        print("You got eaten by a crocodile game over")
else:
    print("You fell into a pit game over")
    















