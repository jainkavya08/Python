import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Surya", "Abhisek", "Shubhman", "Tilak"])
y1 = np.array([3, 4, 1, 80])
y2 = np.array([10, 20, 15, 40])

plt.plot(x, y1, label="Match 1", marker='o')
plt.plot(x, y2, label="Match 2", marker='s')

plt.title("Player Scores Comparison")
plt.xlabel("Players")
plt.ylabel("Scores")
plt.legend()  # shows labels for each line
plt.show()