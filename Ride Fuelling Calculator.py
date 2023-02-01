#### Ride Fuelling Calculator ####

print ("Ride Fuelling Calculator\n\n")

easy_ride_carbs_per_kg=0.5
moderate_ride_carbs_per_kg=0.7
hard_ride_carbs_per_kg=1.0
weight = input("Please enter your current weight in kg: ")
carbs_required_easy=float(easy_ride_carbs_per_kg) * float(weight)
carbs_required_moderate=float(moderate_ride_carbs_per_kg) * float(weight)
carbs_required_hard=float(hard_ride_carbs_per_kg) * float(weight)

print()
print("Easy Z1/Z2 ride:\nYou require " + str(carbs_required_easy)+ " grams per hour\n")
print("Tempo to Sweetspot ride:\nYou require " + str(carbs_required_moderate)+ " grams per hour\n")
print("Hard to Full Gas ride:\nYou require " + str(carbs_required_hard)+ " grams per hour\n")

ride_time=input("Please enter your proposed ride time in hours: ")
print()
ride_time_float=float(ride_time)
carbs_for_time_easy=ride_time_float * carbs_required_easy
carbs_for_time_moderate=ride_time_float * carbs_required_moderate
carbs_for_time_hard=ride_time_float * carbs_required_hard

results=f"Based on a {ride_time_float} hour ride, you will need the following:\n{carbs_for_time_easy} grams of carbs for an Easy ride.\n{carbs_for_time_moderate} grams of carbs for a Moderate ride.\n{carbs_for_time_hard} grams of carbs for a Full Gas ride."

print(results)
