#Calories Burned Excercise
#July 7,2019
#CTI-110 P4HW1 - Calories Burned
# Darrius Brower
#
#1 minute = 5 calories
#Enter calories burned
#Calculate calorie burned for 20, 35, 45 minutes.
caloriesBurnedPerMinute = 5

for numberOfminutes in range(20, 46, 5):
    numberOfCaloriesBurned = (numberOfminutes / 1) * caloriesBurnedPerMinute
    print('You will burn', numberOfCaloriesBurned,'calories in',numberOfminutes,'minutes' )
