import numpy as np
import matplotlib.pyplot as plt

jezyki = ["C", "Java", "Python", "C++", "C#", "Visual Basic", "JavaScript", "PHP", "R", "Groovy", "Bash"]
ranking = [10.38, 11.96, 17.72, 7.56, 3.95, 3.84, 15.20, 1.99, 1.90, 1.84, 3.76]

y_pos = np.arange(len(jezyki))

plt.bar(y_pos, ranking, align="center", alpha=0.5)
plt.xticks(y_pos, jezyki)
plt.ylabel("Popularność(%)")
plt.xlabel("Języki")
plt.title("Użycie języków programowania")

plt.show()