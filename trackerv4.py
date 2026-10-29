# Environmental Awareness Project: Personal Environmental Impact Tracker 3

# Input prompts template
input_template = "Enter the number of {}"

# Input prompt variables in tuples
input_prompts = (
    "miles you have driven: ",
    "showers you have taken: ",
    "meals you have eaten: "
)

# Input
inputs = []
for prompt in input_prompts:
    user_input_prompt = input_template.format(prompt)
    user_input_string = input(user_input_prompt)
    user_input_float = float(user_input_string)
    inputs.append(user_input_float)

# Constants for impact factors
miles_impact = 0.5  # Impact per mile driven (in CO2 emissions)
shower_impact = 2   # Impact per shower (in gallons of water)
meal_impact = 5     # Impact per meal (in pounds of food)

# Calculations
total_impact = (inputs[0] * miles_impact) + (inputs[1] * shower_impact) + (inputs[2] * meal_impact)

# Output
print("Your total environmental impact is: {:.2f} units".format(total_impact))
