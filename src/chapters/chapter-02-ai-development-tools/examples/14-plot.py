# Example 2.14 — single sine curve (README Step 12.1)
# TODO:
# - import numpy as np and matplotlib.pyplot as plt
# - x = np.linspace(0, 2*np.pi, 100), y = np.sin(x)
# - plot it, set a title and x/y axis labels, show the figure
# Expected: a window with one sine wave, titled and labelled.
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()