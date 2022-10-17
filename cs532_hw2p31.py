from matplotlib import pyplot as plt
import numpy as np
import itertools


def main():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    xs = [1, 1, 0, 0.5]
    ys = [1, 0, 1, 0.5]
    zs = [0, 1, 1, 0.5]

    cons = itertools.product(np.arange(4), np.arange(4))

    for i0, i1 in cons:
        ax.plot([xs[i0], xs[i1]],
                [ys[i0], ys[i1]],
                [zs[i0], zs[i1]])

    plt.show()


if __name__ == '__main__':
    main()
