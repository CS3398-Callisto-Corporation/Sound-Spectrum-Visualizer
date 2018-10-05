"""
author: Allen Van

GUI represenation of a time domain.

"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(0, 5), ylim=(-5, 5))
line, = ax.plot([], [], lw=5)
plt.title('Time Domain')
plt.xlabel('Time(Sec)')
plt.ylabel('Signal Amnplitude(m)')

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 5, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

def animate2(i):
    x = np.linspace(0, 5, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
           frames=100, interval=20, blit=True)

anim = animation.FuncAnimation(fig, animate2, init_func=init,
           frames=200, interval=20, blit=True)

plt.show()
