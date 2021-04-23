import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
import numpy as np

from graph import get_connected_components
from draw import draw_infected_points, draw_the_infection_source_point, draw_normal_points


def generate_points(count: int) -> np.array:
    np.random.seed(20210423)
    size = 100
    xs = np.array([])
    ys = np.array([])
    for i in range(count):
        point = np.random.rand(2) * 100
        x, y = point
        xs = np.concatenate((xs.T, [x]))
        ys = np.concatenate((ys.T, [y]))
    return np.array([xs, ys])



fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.set(xlim=(-5, 105), ylim=(-5, 105))

def init():
    return []

def animate(i):
    return draw_progress(i)


# anim = FuncAnimation(fig, animate, 
#                     init_func=init, 
#                     frames=200, 
#                     interval=20,
#                     blit=True)


def draw_progress(i):
    patches = []
    points = generate_points(i)
    infected_point = np.array((50., 50.))
    cc = get_connected_components(np.vstack((points.T, infected_point.T)).T)
    for component in cc:
        if np.any(infected_point == np.array(component)):
            patches += draw_infected_points(component)
            pass
        else:
            patches += draw_normal_points(component)
    patches += draw_the_infection_source_point(infected_point)
    return patches


# writer = FFMpegWriter(fps=15, metadata=dict(artist='Nic B'), bitrate=1800)
# anim.save('animation2.mp4')

draw_progress(80)

plt.show()