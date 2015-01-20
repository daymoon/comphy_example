#! ~/anaconda/bin/python
# -*- conding : utf-8 -*-

import numpy as np

c = -0.8 + 0.156j

steps = 100
offset = 1000
L_x = 2.0
L_y = 2.0
grid_x = 1000
grid_y = 1000


def iterative_eq(z):
    return np.add(np.square(z), c)

def make_grid():
    intv_x = L_x / grid_x
    intv_y = L_y / grid_y
    half_L_x = L_x / 2
    half_L_y = L_y / 2
    grid = [[complex(-half_L_x+intv_x*i, half_L_y-intv_y*j) for i in xrange(grid_x)] for j in xrange(grid_y)]
    return np.asarray(grid)

def write_data(z):
    zlist = z.tolist()
    with open("data.dat", "w") as f:
        for i in zlist:
            f.write(" ".join(["1" if j else "0" for j in i]) + "\n")


def main():
    grid = make_grid()

    for step in xrange(steps):
        grid = iterative_eq(grid)

    nan_grid = np.logical_not(np.isnan(grid))
    less_grid = np.less(grid, offset)
    bool_grid = np.logical_or(nan_grid, less_grid)

    write_data(bool_grid)

if __name__ == "__main__":
    main()
