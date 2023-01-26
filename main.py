"""age = 1
price = 19.05
first_name = "Joe"
is_online = True"""
"""
print(age)

#this prints hello console window

print("Hello console window")

print(age + price)

get_name = input("What is your name? ")

print("Hi " + get_name)

birth_year = input("Enter your birth year? ")
age = 2022 - int(birth_year)
get_age = str(age)
print("So i can steal it... now I know your age guy you're: " + get_age)
stupid_response = input("")
print(stupid_response + " + ratio")
#print(birth_year)
#print("Sorry I'm stealing it?.!" + stupid_response + " See this response is stupid")


first = input("Number 1: ")
second = input("Number 2: ")
sum = int(first) + int(second)
print(sum)
"""
"""
course = 'all upper case test'
print(course.replace('upper', 'lower'))

test = "This will split to a list"
print(test.split())

#+ -
x = 10
x += 10

y = 2 >= 2
price = 25
if price > 30 and price <= 15:
    
print(not price > 30)

print("Hello, welcome to the age calculator.")
age = input("Please input your birthyear: ")
age = 2022 - int(age)

if age > 70:
    print("Wow! you're " + str(age) + " Not much longer now, old fuck")
elif age < 70 and age >= 55 and age != 69:
    print("Pretty good age " + str(age) + " there's still time left")
elif age < 55 and age >= 40:
    print("ok pretty good age " + str(age) + " nice")
elif age < 40 and age >= 25:
    print("ok pretty good age " + str(age) + " lots of time left")
else:
    print("There's some time left at " + str(age) + " for sure")
"""



go_again = 'Y'
new = 'Y'
while go_again == new:
    weight = int(input("Weight: "))
    weight2 = input("(K)g or (L)bs: ")
    if int(weight) > 0:
        if weight2.upper() == "K":
            convert = weight * 2.2046
            print("Weight in (L)bs: " + str(convert))
        elif weight2.upper() == "L":
            convert = weight * 0.4535
            print("Weight in (K)gs: " + str(convert))
        else:
            print("Did not input K or L")

    new = input("Go again? (y or n): ")
    if new.upper() == 'Y':
        new = 'Y'

print("Thanks for using weight calculator! ")

