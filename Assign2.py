"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
ok1 = input("input a number ")
ok1 = float(ok1)
ok2 = input("input another number ")
ok2 = float(ok2)
question = input("is one of those values the hypotenuse of a right triangle? yes or no: ")

if question == "yes":
    ok3 = ok1 ** 2
    ok3 = float(ok3)
    ok4 = ok2 ** 2
    ok4 = float(ok4)
    if ok1 > ok2:
        ok5 = ok3 - ok4
        ok5 = float(ok5)
        ok6 = math.sqrt(ok5)
        print(f"the missing side is: {ok6}")
    if ok2 > ok1:
        ok5 = ok4 - ok3
        ok5 = float(ok5)
        ok6 = math.sqrt(ok5)
        print(f"the missing side is: {ok6}")