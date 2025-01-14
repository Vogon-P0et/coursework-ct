
#module 1 lesson 2
# name = input("What is your name?")
# age = input("What is your age?")
# fav_color = input("What is your favorite color?")
# message = (f"Hello {name}, I see that you are {age} years old and your favorite color is {fav_color}")
# print(message)
# score = int(input("Let's see how you did. What is your exam score?"))
#--------------

#final challenge lesson 2
# Final Challenge: Build a program that asks the user to input their exam score and then prints a message.
# Outputs should be as follows:

# "Excellent" if the score is greater than 90.
# "Good" if the score is between 70 and 90.
# "Needs Improvement" if the score is below 70.
#--
# if score >= 70 <= 90:
#     print("Good")
# elif score > 90:
#     print("Excellent")
# else:
#     print("Needs Improvement")

#----------------------------------------------------------------------------------------------------------
#module 1 lesson 3
# str = "    Coding Temple is awesome!    "
# print(str.upper())
# print(str.strip())
# print(str.replace("Coding", "My"))
# print(str.split())
#--------------

#final challenge lesson 3
# #👾💻 Final Challenge: Build a text-based name generator that combines random first and last names using string manipulation.
# HINT:  Look up and import the "random" module.

# # You can use these two lists of names or you own.

# first_names = ["Christian", "Dylan", "Travis", "Katelyn"]
# last_names = ["Sachs", "Katina", "Peck", "Mehner"]
#---
# import random

# first_names = random.choice(["Paul", "Aaron", "Daniel", "Sara", "Christian", "Dylan", "Travis", "Katelyn"])
# last_name = random.choice(["Jaghab", "Makary", "Sachs", "Katina", "Peck"])

# print(f"{first_names} {last_name}")
#-----------------------------------------------------------------------------------------------------------
#module 1 lesson 4
# milk = 5
# eggs = 3
# coffee = 10

# total_cost = milk+eggs+coffee
# discounted_price = total_cost*0.9

# print(total_cost)
# print(discounted_price)
#---------------
# final challenge lesson 4
# Final Challenge: Design a simple calculator that performs operations on two integers provided by the user.
# Steps:

# Ask the user to input two numbers.
# Perform basic arithmetic operations (add, subtract, multiply, divide) on the inputs.
# Display the results.
#----
# num_1 = int(input("Lets do some basic math! Please enter any whole number.\n"))
# num_2 = int(input("Great! Now enter one more number and we'll get started.\n"))

# if type(num_1) == int and type(num_2) == int:
#     div = num_1 // num_2
#     div_2 = num_2 // num_1
#     mult = num_2 * num_1
#     add = num_1 + num_2
#     sub = num_1 - num_2
#     sub_2 = num_2 - num_1
#     print("All answers are rounded to the nearest whole number")
#     print(f"Dividing the first number by the second, the solution is {num_1}/{num_2}={div}")
#     print(f"Dividing the second number by the first, the solution is {num_2}/{num_1}={div_2}")
#     print(f"Multiplying the two numbers, regardless of order, you get {num_1}*{num_2}={mult}")
#     print(f"Adding the two numbers, regardless of order, you get {num_1}+{num_2}={add}")
#     print(f"Subtracting the second number from the first, the solution is {num_1}-{num_2}={sub}")
#     print(f"Subtracting the first number from the second, the solution is {num_2}/{num_1}={sub_2}")
# else:
#     print("Invalid entry")

#-------------------------------------------------------------------------------------------
# module 1 lesson 5

# weather = input("How's the weather today? \nPlease tell me by typing the words \"Sunny\" or \"Raining.\"\n")        
# if weather.lower() == "sunny":
#     print("Go taka a hike, pal!") 
# elif weather.lower() == "raining":
#     print("You should probably just stay home in your PJ's!")
# else: 
#     print("invalid input\n\n")
#     weather = input("How's the weather today? \nPlease tell me by typing the words \"Sunny\" or \"Raining.\"\n")
# I had a hard time with this one because of the difference between assignment and equivalence
# I also tried a while loop that didn't work out as intended
#-------
# Final Challenge: Write a program where the user has to guess a secret number between 1 and 10. The program should provide feedback if the guess is too high or too low and congratulate the user if they guess correctly.
# HINT: Remember that random module we used a few lessons ago? It would be extremely helpful here... 
# Steps:

# Randomly select a secret number between 1-10.
# Ask the user to make a guess between 1-10.
# If the user is correct, print "Congratulations, You guessed the secret number!"
# If the user is too low, print "Too low!"
# If the user is too high, print "Too high!"
# import random
# secret_num = random.randint(1,10)
# guess = int(input("I'd like you to guess a secret number. Please choose a number between 1 and 10\n"))
# if guess == secret_num:
#     print("Congratulations! You guessed the secret number!")
# elif guess > secret_num:
#     print("Too high.")
# elif guess < secret_num:
#     print("Too low.")
    
#-------------------------------------------------------------------------------------------
# module 1 lesson 6
# fruits = ["apple", "banana", "cherry", "date",]
# print(fruits)
# print(fruits[0])
# print(fruits[-1])
# fruits.append("elderberry")
# print(fruits)
# fruits.insert(0,"blueberry")
# print(fruits)
# fruits.remove("banana")
# print(fruits)
# del fruits[0]
# print(fruits)
# citrus_fruits = fruits[1:3]
# print(citrus_fruits)

#other significant list methods include
# min() and max() --argument must be the list itself rather than the variable name for the list
# .sort() and .sorted() --sort changes the list, sorted creates a new list that can be assigned
# .reverse()
#--------
# lesson 6 final challenge
# Final Challenge: Create a program that asks the user for their top 3 favorite books, stores them in a list, and prints the list in a sorted order.
# Steps:

# Initialize an Empty List.
# Prompt the User for Input.
# Store the Books in the List.
# Sort the List
# Print the Sorted List

# books = []
# fav_1 = input("What are your three favorite books?\n\tPlease type your absolute favorite book:\n")
# fav_2 = input("What book is number two on your list?\n")
# fav_3 = input("What book is number three on your list?\n")
# books.append(fav_1)
# books.append(fav_2)
# books.append(fav_3)
# books.sort()
# print(books)

#------------------------------------------------------------------------------------------


