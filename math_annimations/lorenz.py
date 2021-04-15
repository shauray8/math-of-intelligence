import numpy as np
import matplotlib.pyplot as plt
import os, glob
import IPython.display as IPdisplay, matplotlib.font_manager as fm
from scipy.integrate import odeint
from mpl_toolkits.mplot3d.axes3d import Axes3D
from PIL import Image


initial_state = [0.1,0,0]

sigma = 10.
rho = 28.
beta = 8./3.

start_time = 0
end_time = 100
time_points = np.linspace(start_time, end_time, end_time*100)

def lorenz_system(current_state, t):
    x,y,z = current_state

    dx_dt = sigma * (y-x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z

    return [dx_dt, dy_dt, dz_dt]

values = []

def plot_lorenz(xyz, n):
    #fig = plt.figure(figsize=(12, 9))
    #ax = fig.gca(projection='3d')
    #ax.xaxis.set_pane_color((1,1,1,1))
    #ax.yaxis.set_pane_color((1,1,1,1))
    #ax.zaxis.set_pane_color((1,1,1,1))
    #x = xyz[:, 0]
    #y = xyz[:, 1]
    #z = xyz[:, 2]
    #ax.plot(x, y, z, color='g', alpha=0.7, linewidth=0.7)
    #ax.set_xlim((-30,30))
    #ax.set_ylim((-30,30))
    #ax.set_zlim((0,50))
    #ax.set_title('Lorenz system attractor')
    values.append(tuple(x,y,z))

def get_chunks(full_list, size):
    size = max(1, size)
    chunks = [full_list[0:i] for i in range(1, len(full_list) + 1, size)]
    return chunks

chunks = get_chunks(time_points, size=20)
points = [odeint(lorenz_system, initial_state, chunk) for chunk in chunks]
for n, point in enumerate(points):
    plot_lorenz(point, n)


print(values)

