#!/usr/bin/env python3
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Rysowanie serca
def draw_heart(ax):
    t = np.linspace(0, 2 * np.pi, 100)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
    ax.plot(x, y, 'r-')
    ax.axis('equal')


def main():
    os.system('clear')

    fig, ax = plt.subplots()
    draw_heart(ax)

    # Animacja serca
    ani = FuncAnimation(fig, draw_heart, frames=np.linspace(
        0, 2*np.pi, 128), repeat=True)
    plt.show()


if __name__ == '__main__':
    main()
