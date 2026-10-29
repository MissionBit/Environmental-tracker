# Environmental Awareness Project: Personal Environmental Impact Tracker

# Input prompts template
input_template = "Enter the number of {}"

# Input prompt variables in tuples
input_prompts = (
    "miles you have driven: ",
    "showers you have taken: ",
    "meals you have eaten: "
)

# Input
user_input_prompt = input_template.format(input_prompts[0])
user_input = input(user_input_prompt)
miles_driven = float(user_input)

user_input_prompt = input_template.format(input_prompts[1])
user_input = input(user_input_prompt)
num_showers = float(user_input)

user_input_prompt = input_template.format(input_prompts[2])
user_input = input(user_input_prompt)
num_meals = float(user_input)

# Constants for impact factors
miles_impact = 0.5  # Impact per mile driven (in CO2 emissions)
shower_impact = 2   # Impact per shower (in gallons of water)
meal_impact = 5     # Impact per meal (in pounds of food)

# Calculations
total_impact = (miles_driven * miles_impact) + (num_showers * shower_impact) + (num_meals * meal_impact)

# Output
print("Your total environmental impact is: {:.2f} units".format(total_impact))
