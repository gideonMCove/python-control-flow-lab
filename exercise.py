# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    print("enter a letter")
    x = input()
    if x == ("a" or "e" or "i" or "o" or "u"):
        value = (f"The letter {x} is a vowel")
    else :
        value = (f"The letter {x} is a consonant")
    return value
# Call the function
print(check_letter())

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
   votingAge = 18
   print("Please enter your age")
   x = input()
   y = int(x)
  
   if y < 0 :
       print("It is impossible to be a negative number years old. Take this seriously or face the consequences")
   if y < votingAge : 
       print("Read the constitution. you MUST be 18 in order to vote. Please wait till your 18 or face the consequences.")
   if y >= votingAge :
       print("Congratulations, you are eligible to vote!")
       
   # Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
   print("Enter your dogs age NOW!")
   x = input()
   y = int(x)

   if y < 3 :
       age = y * 10
   elif y > 2 :
       w = y - 2
       age = 20 + (w * 7)
   return age


# Call the function
print(calculate_dog_years())

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    print("RIDDLE ME THIS. IS IT COLD, CHILD? ")
    cold = input()
    isCold = str(cold)
    print("VERY WELL. IS IT RAINING CURRENTLY?")
    raining = input()
    isRaining = str(raining)

    if isCold == "yes" and isRaining == "yes" :
        print("I BEQUEATH YOU THIS WATERPROOF COAT, WEAR IT CHILD")
    elif isCold == "yes" and isRaining == "no" :
        print("I BEQUEATH YOU THIS WARM COAT, WEAR IT CHILD")
    elif isCold == "no" and isRaining == "yes" :
        print("I BEQUEATH YOU THIS UMBRELLA, WIELD IT WISELY, CHILD")
    elif isCold == "no" and isRaining == "no" :
        print("I BEQUEATH YOU NOTHING, FOR YOU NEED NOT CHILD")


# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    season = ""
    print("Enter the month of the year (Jan - Dec): ")
    months = input()
    month = str(months)
    print("Enter the day of the month")
    days = input()
    day = int(days)

    if month == "Jan" or "Feb":
        season = "Winter"
    if month == "Apr" or "May":
        season = "Spring"
    if month == "Jul" or "Aug":
        season = "Summer"
    if month == "Oct" or "Nov":
        season = "Autumn"
    if month == "Dec" and day < 21 :
        season = "Autumn"
    if month == "Dec" and day >= 21 :
        season = "Winter"
    if month == "Mar" and day < 21 :
        season = "Winter"
    if month == "Mar" and day >= 21 :
        season = "Spring"
    if month == "Jun" and day < 21 :
        season = "Spring"
    if month == "Jun" and day >= 21 :
        season = "Summer"
    if month == "Sept" and day < 21 :
        season = "Summer"
    if month == "Dec" and day >= 21 :
        season = "Autumn"
    
    return season




# Call the function
print(determine_season())




