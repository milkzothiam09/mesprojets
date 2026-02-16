import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

points = [
    (0,0,0), (1,0,0), (0,1,0), (0,0,1),
    (1,1,0), (1,0,1), (0,1,1), (1,1,1)
]

edges = [
    (0,1),(0,2),(0,3),
    (7,4),(7,5),(7,6),
    (1,4),(1,5),
    (2,4),(2,6),
    (3,5),(3,6)
]

for x,y,z in points:
    ax.scatter(x,y,z, s=80, color="cyan")

for i,j in edges:
    ax.plot(*zip(points[i], points[j]), color="black")

ax.set_axis_off()

def rotate(angle):
    ax.view_init(elev=30, azim=angle)

ani = FuncAnimation(fig, rotate, frames=360, interval=50)

plt.show()
