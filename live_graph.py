import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import itertools

style.use('fivethirtyeight')

fig = plt.figure(1, (10, 10))
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    graph_data = open('cpu_temp.csv', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(float(y))
    ax1.clear()
    # plt.clf()
    # xs, ys = zip(*sorted(zip(xs, ys)))
    ax1.scatter(xs, ys)
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=10000)
plt.show()
