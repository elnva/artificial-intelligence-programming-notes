# Example 2.15 — sine and cosine on one plot (README Step 12.2)
# TODO:
# - x from -π to π (np.linspace)
# - plot sine in blue with "s" markers, cosine in red with "o" markers
# - add a legend, show the figure
# Expected: two curves, distinct colors/markers, legend visible.

# Import NumPy for arrays and math functions like pi, sin, and cos.
import numpy as np
# Import Matplotlib's plotting interface.
import matplotlib.pyplot as plt

# Create 256 evenly spaced x-values from -π to π.
x = np.linspace(-np.pi, np.pi, 256)

# Calculate the sine value for each x-value.
y = np.sin(x)
# Plot sine using blue square markers.
plt.plot(x, y, "bs")

# Calculate the cosine value for each x-value.
y = np.cos(x)
# Plot cosine using red circle markers.
plt.plot(x, y, "ro")

# Add a legend labeling the sine and cosine plots.
plt.legend(["sin(x)", "cos(x)"])
# Display the plot window.
plt.show()