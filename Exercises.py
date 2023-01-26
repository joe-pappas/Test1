


# if else exercise

# Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south,
# and evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999,
# and service the primary highway indicated by the rightmost two digits. Thus, I-405 services I-5,
# and I-290 services I-90.

# Given a highway number, indicate whether it is a primary or auxiliary highway.
# If auxiliary, indicate what primary highway it serves.
# Also indicate if the (primary) highway runs north/south or east/west.

# Ex. If the input is: 90
# the output is: I-90 is primary, going east/west.

# Ex: If the input is: 290
# the output is: I-290 is auxiliary, serving I-90, going east/west.

# Try this yourself! if you are stuck, the solution is commented on line 40
# to uncomment, highlight the code and press Ctrl + k + u (only works for visual studio code)





"""

highway_number = int(input("Enter highway number: "))
direction = ''
interstate = 0

''' Type your code here. '''

if highway_number % 2 == 0: # get highway direction
    direction = "east/west"
else:
    direction = "north/south"

if highway_number >= 1000 or highway_number < 0: # check if the highway number is between 0 and 1000 to start
    print("This is not a highway number: " + str(highway_number)) # print an error saying this is not a highway number
elif 1 <= highway_number < 100: # indicate if its a primary highway
    print("I-" + str(highway_number) + " is primary, going " + direction) #print out result
else:
    interstate = highway_number % 100 #check if highway number has a remainder after divided by 100
    print("I-" + str(highway_number) + " is auxiliary, serving I-" + str(interstate) + ", going " + direction)



"""

"""i = 1
while i <= 0:
    print(i * " ")
    i = i + 1

names = ["john", "bob", "mosh", "joe", "brendan"]
print(names)"""

# #Solution
# highway_number = int(input())
# direction = ''
# interstate = 0

# ''' Type your code here. '''
# if highway_number % 2 == 0:
#     direction = 'east/west'
# else:
#     direction = 'north/south'

# if highway_number <= 0 or highway_number >= 1000:
#     print(highway_number, 'is not a valid interstate highway number.')
# elif highway_number < 100:
#     print('I-{} is primary, going {}.'.format(highway_number, direction))
# else:
#     interstate = highway_number%100
#     print('I-{} is auxiliary, serving I-{}, going {}.'.format(highway_number,interstate, direction))


# for/while loop problem
# Given a line of text as input, output the number of characters excluding spaces, periods, or commas.

# Ex: If the input is: Listen, Mr. Jones, calm down.
# the output is: 21

# Try this yourself! if you are stuck, the solution is commented on line 25
# to uncomment, highlight the code and press Ctrl + k + u (only works for visual studio code)

"""
text = input()

characters = 0
for i in text:
    if i != "," and i != "." and i != " ":
        characters += 1
print(characters)
"""






# #Solution
# user_text = input()

# count = 0

# for i in user_text:
#     if(i != ' ' and i != '.' and i != ','):
#         count += 1

# print(count)



#for/while loop problem - (Hint use both)
# Write a program that takes in a line of text as input, and outputs that line of text in reverse.
# The program repeats, ending when the user enters "Quit", "quit", or "q" for the line of text.

# Ex: If the input is:

# Hello there
# Hey
# quit

# then the output is:

# ereht olleH
# yeH

#Try this yourself! if you are stuck, the solution is commented on line 35
#to uncomment, highlight the code and press Ctrl + k + u (only works for visual studio code)


"""text = input()

while text != "Quit" and text != "quit" and text != "q":
    rev = list(reversed(text))
    for i in rev:
        print(i, end="")
    print()
    text = input()

"""
"""
test = range(1, 20)
num = 0
for i in test:
    if i % 2 == 0:
        print(i)
        num += 1
print("We have " + str(num) + " even numbers!")
"""


    # #Solution
    # user_text = input()

    # while(user_text != 'Quit' and user_text != 'quit' and user_text != 'q'):
    #     rev = list(reversed(user_text))
    #     for i in rev:
    #         print(i, end="")
    #     print()
    #     user_text = input()





# Write a program that calculates the factorial of an integer.
# Your program should have two variables one to store the inputted number
# and one to calculate the factorial
# Your program should also have a loop that lets you continue to input numbers after the first one
# Your program should continue to run until n is inputted signaling the end of the loop


# Example output:
#  Please enter an integer: 4
#  The factorial is: 24
#  Go again? (y or n): y
#  Please enter an integer: 5
#  The factorial is: 120
#  Go again? (y or n): n
#  Thanks for using factorial calculator!


# Good luck
# First 2 lines below

"""
import math
user_input = int(input('Please enter an integer: '))
go_again = 'Y'

while go_again != 'N':
    #result = 1
    #for i in range(1, user_input + 1):
        #result = result * i

    print("The factorial is: " + str(math.sqrt(user_input)))
    new_input = input("Go again? (y or n): ")
    if new_input.upper() == "N":
        go_again = 'N'
    elif new_input.upper() != 'Y' and new_input.upper() != "N":
        print("Did not input (y or n) ")
        new_input = input("Go again? (y or n): ")
    else:
        user_input = int(input('Please enter an integer: '))

print("Thanks for using factorial calculator! ")
"""

"""
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hey there!")
        print(f"I am {self.name}")


user_input = input("Enter Name: ")
person1 = Person(user_input)
person1.talk()

"""
"""
def phone_number(test_number):
    number = {
        "1": "one ",
        "2": "two ",
        "3": "three ",
        "4": "four ",
        "5": "five ",
        "6": 'six ',
        "7": "seven ",
        "8": "eight ",
        "9": "nine ",
        "0": "zero "
    }

    new = ""
    for i in test_number:
        new += number.get(i, "!")
    return new


user_input = input("Phone: ")
print(phone_number(user_input))
"""
"""
class Dice:
    def __init__(self, roll1, roll2):
        self.roll1 = roll1
        self.roll2 = roll2

    def """

