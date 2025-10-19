import matplotlib.pyplot as plt
import numpy as np

# Data
players = np.array(["Surya", "Abhisek", "Shubhman", "Tilak"])
scores = np.array([3, 4, 1, 80])

# Create pie chart
plt.pie(scores, labels=players, autopct="%1.1f%%", startangle=90)

# Add title
plt.title("Player Score Percentage")

# Show chart
plt.show()
