"""
Your module description
"""
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
import random
number = random.randint(1,10)
isGuessRight = False
print("Count to 10!")
for x in range (0, 11):
    print(x)