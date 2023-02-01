### BMI CALCULATOR ###
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


bmi=round(weight / height ** 2)

if bmi <18.5:
   print(f"Your BMI is {bmi},You are SKINNY AS")
elif bmi <25:
   print(f"Your BMI is {bmi},You are NORMAL WEIGHT")
elif bmi <30:
    print(f"Your BMI is {bmi},You are getting CHUBBY")
elif bmi <35:
   print(f"Your BMI is {bmi},You are OBESE")
else:
 print(f"Your BMI is {bmi},You are one FAT FUCK")
