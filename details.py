# -*- coding: utf-8 -*-
"""
This is a phyton program that accepts users information.

 The program name is details.py
 Step one : declare a variable name
 Step two: Accept username information
 Step three: Use the concatenation sign to make a sentence
 Step Four: Print the output of the program
 
 """
 
 # Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")
house_number = input("Enter your house number: ")
street_name = input("Enter your street name: ")

# Print a sentence with user details
print(f"Hello, {name}! You are {age} years old, and you live at {house_number} {street_name}.")
