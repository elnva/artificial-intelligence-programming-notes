# Exercise 2.5 — sine of a list of numbers (README Step 11.2)
# TODO:
# - read space-separated numbers in one input() line
# - parse them with list(map(float, s.split()))
# - print math.sin of each one
# Expected: one output line per number you typed.
import math
numbers = list(map(float, input("Input a list of numbers: ").split()))
for number in numbers:
    print(math.sin(number))
