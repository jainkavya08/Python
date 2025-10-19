import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array(["Surya", "Abhisek", "Shubhman", "Tilak"])
y = np.array([30, 5, 7, 80])

colors = ['Skyblue', 'orange' , 'green' , 'blue']

fig, ax = plt.subplots()

ax.set_facecolor('pink')

ax.grid(True, which='both', color='black', linestyle='--',linewidth=0.7)
ax.set_axisbelow(True)

bars = plt.bar(x, y, color=colors, width=0.5 )

plt.title("Player to Score Ratio", color='purple')
plt.xlabel("Players" , color= 'Red')
plt.ylabel("Scores", color = 'Red')

for bar in bars :
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2 , height / 2, str(height),
             ha = 'center' , va = 'bottom', color = 'red', fontsize = 12)

plt.show()
