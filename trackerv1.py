# Environmental Awareness Project: Personal Environmental Impact Tracker

# Input
user_input = input("showers you have taken: ")
num_showers = int(user_input)

# Constants for impact factors
shower_impact = 2  # Impact per shower (in gallons of water)

# Calculations
total_impact = num_showers * shower_impact

# Output
output = "Your total environmental impact is: " + str(total_impact)
print(output)
