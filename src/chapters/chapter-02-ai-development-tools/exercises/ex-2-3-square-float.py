# Exercise 2.3 — square a float from the keyboard (README Step 10.4)
# TODO:
# - same as examples/11-input2.py, but convert the input with float() instead of int()
# - print "The square of <x> is <y>"
# Expected: entering 1.5 prints 2.25.
x = float(input("Input a number: "))
y = x ** 2
print("The square of " + str(x) + " is " + str(y))
