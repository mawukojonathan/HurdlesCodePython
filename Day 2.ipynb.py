#Subscripting
#the method of pulling out a particular element from a string is called subscripting.
#the number in the square brackets [] determines which character you are going to pull out.
#e.g 

print("Hello"[0])
print("\n")
# you can use the type() function to know the type of data type you are working with.
#e.g

a = 24
print(type(a))
print("\n")
#Day 2 ineractive coding exercise Data Types

two_digit_number = input("Type a two digit number: ")
subscript1_two_digit_number = two_digit_number[0]
subscript2_two_digit_number = two_digit_number[1]
sub_int1 = int(subscript1_two_digit_number)
sub_int2 = int(subscript2_two_digit_number)
print(sub_int1 + sub_int2)
print("\n")
#Interacive Coding Exercise BMI Calculator
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight // (height ** 2)
int_bmi = int(bmi)
print(int_bmi)
print("\n")
#You can use the round function to round a floating point number to the nearest whole number.
#You can specify the number of digits you want to round it to by adding a comma.
#e.g
print(round(8 / 3))
print(round( 8 / 3, 2))
print("\n")

#Interactive Coding Exercise Life in Weeks

age = int(input("What is your current age? "))
days = (365 * 90) - age * 365
weeks = (52 * 90) - age *52
months = (12* 90) - age * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
print("\n")

#Day 2 Project: Tip Calculator

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
percentage = int(input("What percentage would you like to give? 10, 12,  or 15? "))
split_bill = int(input("How mant people to split the bill? "))

payment_for_each = total_bill / split_bill
percentage_to_give = (percentage / 100 * total_bill) / split_bill
total_payment = payment_for_each + percentage_to_give
round_total_payment = "{: .2f}".format(total_payment)
print(f"Each persom should pay ${round_total_payment}")
print("\n")

# Another way of rounding a number to two (2) decimal places or more is by using the format function.
#e.g above (round_total_payment)






                 

                         



