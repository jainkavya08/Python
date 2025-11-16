import matplotlib.pyplot as plt

# X and Y coordinates of multiple points
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 15]

# Plot multiple points with lines and markers
plt.plot(x, y, marker='o', color='blue', linestyle='-')

# Add title and labels
plt.title("Plotting Multiple Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display graph
plt.show()
