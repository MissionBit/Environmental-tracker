# Project Brief: Environmental Awareness Project - Personal Environmental Impact Tracker
This project is a simple win project that will get students to think about their daily habits and their impact on the environment.

**Skills and concepts:**

- Python syntax
- Strings
- Data types
- Simple data structures

**Project outline:**

1. Input and Output
2. Basic calculations
3. Tracking over time

## Version 1
**Goals:**
In this step, you will create a simple Python program to track your personal environmental impact, specifically focusing on the number of showers you take and their water consumption. This step aims to introduce you to basic Python programming concepts such as input/output, variables, constants, and simple calculations.

**Stage 1: Understanding and Input**
- **Objective:** Understand the basic structure of the project and learn how to take user input.
- **Tasks:**
  1. Read and understand the provided code.
  2. Identify the input statement and its purpose.
  3. Run the code and observe how the program prompts the user for input.
  4. Enter a number representing the number of showers you have taken and observe the program's output.
  
**Stage 2: Constants and Calculations**
- **Objective:** Learn how to define constants and perform simple calculations in Python.
- **Tasks:**
  1. Identify the constant `shower_impact` and understand its purpose.
  2. Explore how constants are used in calculations.
  3. Calculate the environmental impact of different numbers of showers based on the given impact factor.
  4. Modify the code to calculate and display the environmental impact for different numbers of showers.
  
**Stage 3: Output and Formatting**
- **Objective:** Learn how to format output messages in Python.
- **Tasks:**
  1. Analyze the output statement and understand how it combines strings and variables.
  2. Experiment with different output formats, such as using f-strings or the `format()` method.
  3. Modify the output message to display the environmental impact in a clear and informative way.
  
**Stage 4: Project Completion and Reflection**
- **Objective:** Complete the project and reflect on what you've learned.
- **Tasks:**
  1. Review and finalize your code, ensuring it meets the project requirements.
  2. Test your program with different input values to verify its correctness.
  3. Reflect on your experience and the concepts you've learned during the project.
  4. Consider potential improvements or additional features you could implement in the future.

## Version 2
**Goals:**
In this update, you will learn how to refactor and improve your existing Environmental Awareness Project by incorporating string variables for input prompts. We will also add another variable, number of meals per week, to our calculations.

**Step 1: Understanding Changes**
- **Objective:** Understand the changes introduced in Version 2 of the project.
- **Changes:** 
  - Input prompts are defined as string variables (`prompt_meals` and `prompt_showers`).
  - Input statements use these string variables for prompting the user.

**Step 2: Refactoring Input**
- **Objective:** Learn how to refactor input statements to use string variables.
- **Tasks:**
  1. Identify the new string variables (`prompt_meals` and `prompt_showers`).
  2. Understand how these variables are used in the input statements to prompt the user.
  3. Update your existing code to replace the direct input prompts with the new string variables.
  
**Step 3: Review Constants and Calculations**
- **Objective:** Review the existing constants and calculations in your code.
- **Changes:** 
  - No changes are made to the constants or calculations in this update.
  - Constants (`meal_impact` and `shower_impact`) and calculations remain the same as in Version 1.
  
**Step 4: Output Formatting**
- **Objective:** Understand how output formatting is handled in the updated code.
- **Changes:** 
  - The output message formatting remains the same as in Version 1.
  - The output message combines a string with the calculated `total_impact` variable using the `format()` method.
  
**Step 5: Update Your Code**
- **Objective:** Update your existing code to incorporate the changes from Version 2.
- **Tasks:**
  1. Replace the direct input prompts with the new string variables (`prompt_meals` and `prompt_showers`).
  2. Ensure that the constants and calculations remain unchanged from Version 1.
  3. Test your updated code to verify that it functions correctly.

## Version 3
**Goals:**
In this update, you will further improve your project by using a template for input prompts and storing input prompt variables in a tuple. You will also add one final variable, miles driven, and start working with a new datatype: floats.

**Step 1: Understanding Changes**
- **Objective:** Understand the changes introduced in Version 3 of the project.
- **Changes:** 
  - Input prompts are defined using a template (`input_template`) and stored in a tuple (`input_prompts`).

**Step 2: Refactoring Input Prompts**
- **Objective:** Learn how to refactor input prompts using a template and tuple.
- **Tasks:**
  1. Identify the new `input_template` variable and understand its purpose.
  2. Explore how this template is used to generate input prompts dynamically.
  3. Understand how input prompt variables are stored in a tuple (`input_prompts`).
  4. Update your existing code to use the template and tuple for input prompts.

**Step 3: Review Input and Constants**
- **Objective:** Review the existing input handling and constants in your code.
- **Changes:** 
  - No changes are made to the input handling or constants in this update.
  - The input prompts are now generated dynamically using the template and tuple.
  
**Step 4: Constants and Calculations**
- **Objective:** Ensure that constants and calculations remain consistent with previous versions.
- **Changes:** 
  - Constants (`miles_impact`, `shower_impact`, and `meal_impact`) and calculations remain unchanged from previous versions.

**Step 5: Update Your Code**
- **Objective:** Update your existing code to incorporate the changes from Version 3.
- **Tasks:**
  1. Replace the direct input prompts with the dynamic prompts generated using the template and tuple.
  2. Verify that the constants and calculations remain consistent with previous versions.
  3. Test your updated code to ensure it functions correctly.


## Version 4
**Goals:**
Your final version will update the tracker with an array to store each user input, then loop through the array programmatically using a for loop.

**Key Features:**
1. Input prompts are generated dynamically using a template (`input_template`) and stored in a tuple (`input_prompts`).
2. Users are prompted to input the number of miles driven, showers taken, and meals eaten.
3. Constants for impact factors, such as CO2 emissions per mile driven and gallons of water per shower, are defined for calculations.
4. The program calculates the total environmental impact based on user inputs and predefined impact factors.
5. The calculated impact is displayed to the user with two decimal places for precision.

**Project Guide:**
1. **Input Prompts Template:**
   - The `input_template` variable contains the template for input prompts. It uses curly braces `{}` as placeholders for dynamic content.
   - Input prompt variables are stored in a tuple named `input_prompts`. Each prompt represents a specific daily activity (miles driven, showers taken, meals eaten).
   
2. **Input Handling:**
   - The program prompts the user to input the number of miles driven, showers taken, and meals eaten using a loop that iterates over the `input_prompts` tuple.
   - For each prompt, the program dynamically generates the input prompt message using the `input_template` and the corresponding prompt from the tuple.
   - User inputs are converted to float values and stored in a list named `inputs`.
   
3. **Constants and Calculations:**
   - Constants for impact factors, such as CO2 emissions per mile driven and gallons of water per shower, are defined for calculations.
   - The program calculates the total environmental impact by multiplying user inputs with the corresponding impact factors and summing the results.
   
4. **Output:**
   - The calculated total environmental impact is displayed to the user with two decimal places for precision using the `print()` function and string formatting.
