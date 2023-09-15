import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def cau1():
    def a():
        x, y, z = sp.symbols("x y z")

        pt1 = sp.Eq(x + 2*y + z, 0)
        pt2 = sp.Eq(2*x - y + z, 0)
        pt3 = sp.Eq(2*x + y, 0)

        return sp.solve((pt1, pt2, pt3), (x, y, z))

    def b():
        x, y, z, t = sp.symbols("x y z t")

        pt1 = sp.Eq(2*x + y + z + t, 1)
        pt2 = sp.Eq(x + 2*y + z + t, 1)
        pt3 = sp.Eq(x + y + 2*z + 2*t, 1)
        pt4 = sp.Eq(x + y+ z + 2*t, 1)

        return sp.solve((pt1, pt2, pt3, pt4), (x, y, z, t))

    print("a. ", a())
    print("b. ", b())

#Ham in ra do thi cua phuong trinh y = ax + b
def plot2D(a, b, c, color="red"):
    if (b != 0):
        x_arr = np.arange(-20, 21)
        y = lambda x: (c - a*x)/b
        y_arr = list(map(y, x_arr))
        plt.plot(y_arr, x_arr, color=color, label=f"{a}x + {b}y = {c}")

    else:
        if (a != 0):
            plt.axvline(x = c/a, label=f"x = {c/a}")
        else:
            print(f"Cannot plot {a}x + {b}y = {c}")

def cau2():
    #a
    plot2D(1, 2, 3, "purple")
    plot2D(2, 4, 12)
    plt.grid()
    plt.legend()
    plt.show()

    #b
    plot2D(21, 9, 13)
    plot2D(2004, 52200167, 26)
    plt.grid()
    plt.legend()
    plt.show()

    #c
    plot2D(1, 2, 4)
    plot2D(0, 0, 4, "blue")
    plt.grid()
    plt.legend()
    plt.show()

def plot3D(ax, a, b, c, d):
    x_arr = np.arange(-10, 11)
    y_arr = np.arange(-10, 11)
    z = lambda x, y: (d - a*x - b*y)/c
    X, Y = np.meshgrid(x_arr, y_arr)
    Z = z(X, Y)

    ax.plot_surface(X, Y, Z)

def cau3():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    plot3D(ax, 1, 2, 3, 4)
    plot3D(ax, 1, 4, 12, 32)
    plt.show()

cau3()