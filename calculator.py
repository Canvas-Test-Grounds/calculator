import math
import random

# introduction message
print("Welcome to the Cow Q L8 tor!")
print("---------------")
print("menu:")
print("A for addition \nB for subtraction \nC for multiplication \nD for division")


# Start of loop
while True:
# prompting the user on what to use,
    program = str.upper(input("Which calculator would you like to use?\n"))
# After prompting the user, these variables will be used to determine the program.
    add = str.upper("a")
    minus = str.upper("b")
    multi = str.upper("c")
    div = str.upper("d")


# if program for "add"
    if program == add:
        num1 = int(input("input your first number: "))
        num2 = int(input("input your second number to add: "))
        total = (num1 + num2)
        print("Your total number is: ", total)
        print("============================")
        print("Would you like to redo the calculations?")
        redo = str.upper(input("Please type r or R if you would like to redo the calculations\n"))

        if redo == str.upper("r"):
            continue
        
        else:
            if redo != str.upper("r"):
                break


# if program for subtraction
    if program == minus:
        num1 = int(input("input your first number: "))
        num2 = int(input("input your second number to subtract: "))
        total = (num1 - num2)
        print("Your total number is: ", total)
        print("============================")
        print("Would you like to redo the calculations?")
        redo = str.upper(input("Please type r or R if you would like to redo the calculations\n"))

        if redo == str.upper("r"):
            continue

        else:
            if redo != str.upper("r"):
                break


# if program for multiplication
    if program == multi:
        num1 = int(input("input your first number: "))
        num2 = int(input("input your second number to multiply: "))
        total = (num1 * num2)
        print("Your total number is: ", total)
        print("============================")
        print("Would you like to redo the calculations?")
        redo = str.upper(input("Please type r or R if you would like to redo the calculations\n"))

        if redo == str.upper("r"):
            continue

        else:
            if redo != str.upper("r"):
                break

# if program for division
    if program == div:
        num1 = int(input("input your first number: "))
        num2 = int(input("input your second number to divide: "))
        total = (num1 / num2)
        print("Your total number is: ", int(total))
        print("============================")
        print("Would you like to redo the calculations?")
        redo = str.upper(input("Please type r or R if you would like to redo the calculations\n"))

        if redo == str.upper("r"):
            continue

        else:
            if redo != str.upper("r"):
                break


