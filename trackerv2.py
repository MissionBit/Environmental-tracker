# Environmental Awareness Project: Personal Environmental Impact Tracker

# Input prompts as string variables
prompt_meals = "meals you have eaten: "
prompt_showers = "showers you have taken: "

# Input
input_meals = input(prompt_meals)
num_meals = int(input_meals)
input_showers = input(prompt_showers)
num_showers = int(input_showers)

# Constants for impact factors
meal_impact = 5     # Impact per meal (in pounds of food)
shower_impact = 2   # Impact per shower (in gallons of water)

# Calculations
total_impact = (num_meals * meal_impact) + (num_showers * shower_impact)

# Output
output = "Your total environmental impact is: {} units".format(total_impact)
print(output)
