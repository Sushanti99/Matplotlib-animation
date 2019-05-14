import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Circle((5, -5), 0.5, fc='b')
t=0.5

def init():
    patch.center = (5, 5)
    ax.add_patch(patch)
    return patch,

def animate(i):
    ax.add_patch(plt.Circle((5,5),t+0.2,color='b'))
    return patch,

anim = animation.FuncAnimation(fig, 
                               animate, 
                               init_func=init, 
                               frames=90, 
                               interval=600,
                               blit=True)

plt.show()
plt.rcParams['animation.ffmpeg_path'] ='C:\\ffmpeg\\bin\\ffmpeg.exe'
FFwriter=animation.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
anim.save('expand.mp4', writer=FFwriter)