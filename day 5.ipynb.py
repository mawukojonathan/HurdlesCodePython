# the loop allows us to execute the same line of code multiple times
#the (sum) function in python gives the total of all the items from a list 

#day 5 (interactive coding exercise) average height

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of student = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")

#soloution code above!!!

print("\n")

#the max() function gives the highest value in a particular list 
#the min() finction gives the lowers value in a particular list

#Interactive Coding Exercise: High Score 

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])    
print(student_scores)

highest_score = 0

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
    #print(highest_score)

print(f"The highest score in the class is: {highest_score}")

#Soloution code above!!!

#Intrative Coding Exercise: Adding Even Numbers

#draft code
total = 0

for number in range(1, 101):
   total += number
print(total)

total_even = 0

for even_number in range(0, 101, 2):
   total_even += even_number
print(total_even)

#Interactive coding exercise: Fizzbuzz

for numbers in range(1, 101):
   if numbers % 3 == 0 and numbers % 5 == 0:
      print("fizzbuzz")
   elif numbers % 3 == 0:
      print("fizz")
   elif numbers % 5 == 0:
      print("buzz")  
   else:
      print(numbers)

#password generator project 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

print("\n")

password = []

for i in range(nr_letters ):
    randomletter = random.choice(letters)
    password.append(randomletter)
   

for j in range(nr_symbols ):
    randomsymbol = random.choice(symbols)
    password.append(randomsymbol)

    

for k in range(nr_numbers ):
    randomnumber = random.choice(numbers)
    password.append(randomnumber)
    
k = len(password)
randompassword = random.sample(password, k)
#print(f"Here is your password: {str(randompassword)}")
print(type(randompassword))
orandompassword = ( ''.join(randompassword))  
print(f"Here is your password {orandompassword}")

# you can use the random.sample(sequence, k) to shuffle elements in a list 
# where the sequence is the name of the list and k is the number of elements in the list 
     
    
    




    



