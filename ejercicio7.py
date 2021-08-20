#This function converts miles to kilometers (km).
#Complete the function to return the result of the conversion
#Call the function to convert the trip distance from miles to kilometers
#Fill in the blank to print the result of the conversion
#Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result

def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km
my_trip_km = convert_distance(55)
print("The distance in kilometers is " + str(my_trip_km))
print("The round-trip in kilometers is " + str(2*my_trip_km))