import numpy as np
import matplotlib.pyplot as plt

jezyki = ["C", "Java", "Python", "C++", "C#", "Visual Basic", "JavaScript", "PHP", "R", "Groovy"]
ranking = [17.38, 11.96, 11.72, 7.56, 3.95, 3.84, 2.20, 1.99, 1.90, 1.84]

y_pos = np.arange(len(jezyki))

plt.bar(y_pos, ranking, align="center", alpha=0.5)
plt.xticks(y_pos, jezyki)
plt.ylabel("Popularność(%)")
plt.xlabel("Języki")
plt.title("Użycie języków programowania")

plt.show()