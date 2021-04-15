import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


initial_state = [0.1,0,0]

sigma = 10.
rho = 28.
beta = 8./3.

start_time = 0
end_time = 100
time_points = np.linspace(start_time, end_time, end_time*100)

def lorenz_system(current_state):
    x,y,z = current_state
    
    dt = 0.01
    dx = (sigma * (y-x))*dt
    dy = (x * (rho - z) - y)*dt
    dz = (x * y - beta * z)*dt
    initial_state[0] = initial_state[0] + dx 
    initial_state[1] = initial_state[1] + dy 
    initial_state[2] = initial_state[2] + dz

    plt.plot(initial_state[0], initial_state[1], initial_state[2])
    plt.show()

for i in range(100):
    lorenz_system(initial_state)

values = []

def plot_lorenz(xyz, n):
    x = xyz[:, 0]
    y = xyz[:, 1]
    z = xyz[:, 2]
    return x,y,z

def get_chunks(full_list, size):
    size = max(1, size)
    chunks = [full_list[0:i] for i in range(1, len(full_list) + 1, size)]
    return chunks

#chunks = get_chunks(time_points, size=20)
#points = [odeint(lorenz_system, initial_state, chunk) for chunk in chunks]

def exit():
    for n, point in enumerate(points):
        x,y,z = plot_lorenz(point, n) 
        fig = plt.figure(figsize=(12, 9))
        ax = fig.gca(projection='3d')
        ax.xaxis.set_pane_color((1,1,1,1))
        ax.yaxis.set_pane_color((1,1,1,1))
        ax.zaxis.set_pane_color((1,1,1,1))
        ax.plot(x, y, z, color='g', alpha=0.7, linewidth=0.7)
        ax.set_xlim((-30,30))
        ax.set_ylim((-30,30))
        ax.set_zlim((0,50))
        ax.set_title('Lorenz system attractor')
        plt.show()    
