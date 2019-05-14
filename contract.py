import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import cv2
fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Circle((5, -5), 2, fc='b')
t=0.5

def init():
    patch.center = (5, 5)
    ax.add_patch(patch)
    return patch,

def animate(i):
    patch.set_radius(2-(i/2))
    return patch,

anim = animation.FuncAnimation(fig, 
                               animate, 
                               init_func=init, 
                               frames=4, 
                               interval=3000,
                               blit=False)
plt.show()

plt.rcParams['animation.ffmpeg_path'] ='C:\\ffmpeg\\bin\\ffmpeg.exe'
FFwriter=animation.FFMpegWriter(fps=6, extra_args=['-vcodec', 'libx264'])
anim.save('contract.mp4', writer=FFwriter)
