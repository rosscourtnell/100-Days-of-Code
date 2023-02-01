name=input("What is your name?\n")
if name=="Simon":
    print("You are a LOSER!")
elif name=="Ross":
    print("YOU ARE A LEGEND!")
else:
    print("You are a NOBODY!")





#name=input("What is your name?\n")







# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first_digit=(int(two_digit_number[0]))
second_digit=(int(two_digit_number[1]))
print(first_digit+second_digit)

### Outputting using the length variable and converting an integer to a string ###
name=input("Please type your name and I will give you the number of characters: ")
length_of_name=len(name)
print ("Your name has "+ str(length_of_name)+" characters")


### BMI CALCULATOR ###
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#weight_as_int=int(weight)
#height_as_float=float(height)


bmi=int(weight) / float(height) **2
bmi_as_int=int(bmi)
print(bmi_as_int)

### LIFE IN WEEKS ###
age = input("What is your current age? ")

years_left = 90 - int(age)
months_left = round(years_left * 12)
weeks_left = round(years_left * 52)
days_left = round(years_left * 365)

message=f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)
