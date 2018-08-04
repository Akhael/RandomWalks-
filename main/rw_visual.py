import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    rw = RandomWalk(100)
    rw.fill_walk()

    # sets the dimensions for the plot 
    plt.figure(figsize=(5, 5))
    plt.plot(rw.x_values, rw.y_values,lw=1, )
    # plot the first and last points /// Green = start /// Red = End
    plt.scatter(0, 0, c='green', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=50)
    # remove the axes
    plt.axis('off')
    plt.show()

    # exit loop 
    stop = input('Stop (y/n): ')
    if stop == 'y':
        break
    else:
        continue