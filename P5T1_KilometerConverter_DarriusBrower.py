# Kilometer Converter Excercise
# July 13, 2019
# CTI-110 P5T1_KilometerConverter
# Darrius Brower
#
# Write a program that converts kilometers to miles.
# miles = kilometers * 0.6214
# Display the conversion in miles.
#
CONVERSION_FACTOR = 0.6214

def main():
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    #Display the distance converted to miles.
    show_miles(kilometers)
                       
def show_miles(km):
    #Calculate miles
    miles = km * CONVERSION_FACTOR

    #Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

main()                       
