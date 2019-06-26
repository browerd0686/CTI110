#CTI-110
#P3HW1 - Color Mixer
#Darrius Brower
#June 25, 2019
#
#input the color red
#input the color blue
#input the color yellow
#Calculate color red + color blue
#Calculate color blue + color yellow
#Calculate color yellow + color red

#Name the Colors
#primarycolor1 = red
#primarycolor2 = blue
#primarycolor3 = yellow

#Display results
#red + blue = purple
#blue + yellow = green
#yellow + red = orange



primarycolor1 = input('Please enter primary color 1: ')
primarycolor2 = input('Please enter primary color 2: ')

if primarycolor1 == "red" and primarycolor2 == "blue":
    print('You get the secondary color purple')
elif primarycolor1 == "blue" and primarycolor2 == "red":
    print('You get the secondary color purple')
if primarycolor1 == "yellow" and primarycolor2 == "red":
    print('You get the secondary color orange')
elif primarycolor1 == "red" and primarycolor2 == "yellow":
    print('You get the secondary color orange')
if primarycolor1 == "blue" and primarycolor2 == "yellow":
    print('You get the secondary color green')
elif primarycolor1 == "yellow" and primarycolor2 == "blue":
    print('You get the secondary color green')
else:
    print("At least one of the primary colors is not a primary color.")
   
