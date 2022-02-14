# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


import json


def handle_user_choice(user_choise: str, bank: dict):
    if user_choise == "1":
        update_grocery(bank)
    elif user_choise == "2":
        print(bank.items())
    elif user_choise == "3":
        bank = counting(bank)
    return bank


def update_grocery(bank: dict):
    new = input("Please enter your spend name end the value like this <name,value>:")
    name = new.split(",")[0]
    value = new.split(",")[1]
    bank[name] = int(value)
    return bank


def your_choice():
    choice = input("pls enter your choice \n1.add product"""
                   "2.print"
                   "\n3.print income")
    return choice


def counting(spending: dict):
    value = spending.values()
    total = sum(value)
    print(total)
    return total


def enteracount():
    holder1 = input("please enter your name")
    holder1 += ".txt"
    import os.path
    if os.path.isfile(holder1):
        with open(holder1) as f:
            se = f.read(-1)
            re = {se}
            print(re)


def updateacount(spend: dict):
    filename = input()
    filename += ".txt"
    print(filename)
    with open(filename, "a") as f:
        f.write(str(spend.items()))
        f.write("\n")
        dre = open(filename)
        print(dre.read(-1),"k3efnmd")


def main():
    spend = {}
    while True:
        hello = input("1.to apdate grocry print \n"
                      "2.to save the list")
        if hello == "1":
            user_choise = your_choice()
            spend = handle_user_choice(user_choise, spend)
        if hello == "2":
            holder = input("1.if you wont to create list or update \n "
                           "2.print")
            if holder == "1":
                updateacount(spend)
            if holder == "2":
                enteracount()


if __name__ == '__main__':
    main()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
