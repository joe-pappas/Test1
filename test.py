def greet_user(first_name):
    print(f"Hi {first_name}!")
    print("How are we feeling today? ")


def main_menu():
    print("1. Calculate highways ")
    print("2. Calculate factorial ")
    print("3. Money Converter")
    print("4. File Reader")
    print("9. Print Main Menu")
    print("0. Exit")


def highway_calculator():
    highway_number = int(input("Enter highway number: "))
    direction = ''
    interstate = 0

    if highway_number % 2 == 0:  # get highway direction
        direction = "east/west"
    else:
        direction = "north/south"

    if highway_number >= 1000 or highway_number < 0:  # check if the highway number is between 0 and 1000 to start
        print("This is not a highway number: " + str(
            highway_number))  # print an error saying this is not a highway number
    elif 1 <= highway_number < 100:  # indicate if its a primary highway
        print("I-" + str(highway_number) + " is primary, going " + direction)  # print out result
    else:
        interstate = highway_number % 100  # check if highway number has a remainder after divided by 100
        print("I-" + str(highway_number) + " is auxiliary, serving I-" + str(interstate) + ", going " + direction)


def money_converter():
    money = float(input("Amount: "))
    money2 = input("(U) sd or (M) p: ")
    if float(money) > 0:
        if money2.upper() == "U":
            convert = money * 19.13
            new = round(convert, 2)
            print("Dollars in pesos: " + str(new))
        elif money2.upper() == "M":
            convert = money * .052
            new = round(convert, 2)
            print("Pesos in Dollars: " + str(new))
        else:
            print("Did not input U or M")


def file_reader():
    f = open("test3.txt", "r")
    print(f.read())
    print()

    text = input()
    rev = list(reversed(text))

    new = open("test4.txt", "a")
    for i in rev:
        new.write(i)
    print()
    new = open("test4.txt", "r")
    print(new.read())


user_input = input("Who's logging in: ")
greet_user(user_input)
main_menu()
print("")
loop_input = "N"
while loop_input == "N":
    get_menu_option = int(input("Please select an option: "))

    if get_menu_option == 1:
        highway_calculator()
    elif get_menu_option == 3:
        money_converter()
    elif get_menu_option == 4:
        file_reader()
    elif get_menu_option == 9:
        main_menu()
    elif get_menu_option == 0:
        loop_input = "Y"
    else:
        print("Did not type a valid number!")
        main_menu()
    print("")


