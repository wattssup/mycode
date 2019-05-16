#!/usr/bin/env python3
# A program that prompts a user for 2 operators and and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program

calc1 = 0.0
calc2 = 0.0
operation = ""
while (calc1 != "q")
    print("\nWhat is the first Operator? Or, enter q to quit: ")
    calc1 = raw_input()
    if calc1 == "Q":
        break
    calc1 = float(calc1)
    print("\nWhat is the second operator? Or, enter q to quit: ")
