# Exercise 2.6 — three curves on one plot (README Step 12.3)
# TODO:
# - pick an x range with np.linspace
# - plot y = 3x + 4, y = 2x² + 1, y = x³ + 9 on the same axes
# - three different colors, add a legend, show the figure
# Expected: three distinct curves with a legend.
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 100, 100)

plt.title("Linspace")
plt.xlabel("x")
plt.ylabel("sin(x)")

y = (3 * x) + 4
plt.plot(x, y, label="y = 3x + 4")

y = (2 * (x ** 2)) + 1
plt.plot(x, y, label="y = 2x² + 1")

y = (x ** 3) + 9
plt.plot(x, y, label="y = x³ + 9")

plt.title("Three curves")
plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()