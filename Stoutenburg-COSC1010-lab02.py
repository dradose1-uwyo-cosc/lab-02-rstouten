# Reuben Stoutenburg
# UWYO
# 9/19/2024
# Lab 02
# Lab Section: 18
# Sources

# Print out "Hello, COSC1010"
print("Hello, COSC1010")

# Assign this string to a variable

hello_message = "Hello, COSC1010"
print(hello_message)

# create "Cowboy Joe" variable and print it

mascot = "Cowboy Joe"
print(mascot)

# Complete the following f-string print message 
    # You will need to create your own variables and insert them  
    # the final message should read `The University of Wyoming was founded in 1886`

college = "University of Wyoming"
date = "1886"

print(f"The {college} was founded in {date}")

# Now let's do some math with variables 
    # Create two variables x and y and assign them the values 5 and 10 respectively 
    # Complete the following print statements using your variables
    #All math must be done within the braces in the f-strings
x = 5
y = 10
print(f"x + y = {x+y}")
print(f"x - y = {x-y}")
print(f"x * y = {x*y}")
print(f"x / y = {x/y}")

# String concatenation 
    # Finally we will take a look at string concatenation
    # String concatenation combines two strings together
    # It is done using the + operator
    # Create three variables:
        # first_name, which is your first name 
        # last_name, which is your last name
        # space, which is a space character 
    # Use string concatenation to print out your full name 
first_name = "reuben"
last_name = "stoutenburg"
space = " "
full_name = first_name + space + last_name
print(full_name.title())







