# Exercise
# Write a program that asks the user to input their name, age, and country. 
# The program should then print out a message that includes this information in a sentence. The program should include:

# Taking a name as input using input().
# Taking an age as input using input(), and converting it to an integer.
# Taking a country name as input using input().
# Formatting the output to display a sentence that includes the name, age, and country.
# The program should demonstrate input handling and string formatting in Python.

# Taking the name input using input()
name = input("Enter your name: ")

# Taking the age input using input() and converting it to integer
age = int(input("Enter your age: "))

# Taking the country input using input()
country = input("Enter your country: ")

# Displaying the formatted sentence with name, age, and country
print("Hello, my name is {}, I am {} years old, and I am from {}.".format(name, age, country))

