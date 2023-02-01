### LIFE IN WEEKS ###
age = input("What is your current age? ")

years_left = 90 - int(age)
months_left = round(years_left * 12)
weeks_left = round(years_left * 52)
days_left = round(years_left * 365)

message=f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)
