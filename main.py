import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import numpy as np

#Bezier Curves
def linearBezier(p0, p1, t):
    bez_val=((1-t)*p0)+(t*p1)
    return bez_val

def quadraticBezier(p0, p1, p2, t):
    bez_val=(math.pow((1-t), 2)*p0)+(2*(1-t)*t*p1)+(math.pow(t, 2)*p2)
    return bez_val

def cubicBezier(p0, p1, p2, p3, t):
    bez_val=(math.pow((1-t), 3)*p0)+(3*math.pow(1-t, 2)*t*p1)+(3*(1-t)*math.pow(t, 2)*p2)+(math.pow(t, 3)*p3)
    return bez_val

list_x = []
list_y = []
list_z = []

new_x=[]
new_y=[]
new_z=[]

size=[]

#append x y z coordinates to respective lists
with open("smooth_path.csv", newline="") as csv_file:
    path = csv.reader(csv_file, delimiter=" ")

    for row in path:
        row = row[0].split(",")
        x = float(row[0])
        y = float(row[1])
        z = float(row[2])
        list_x.append(x)
        list_y.append(y)
        list_z.append(z)

#append size to list
with open("Gcorridor.csv", newline="") as csv_file:
    corridor=csv.reader(csv_file, delimiter=" ")

    for row in corridor:
        row=row[0].split(",")
        num=int(row[0])
        s=float(row[1])
        size.append(s*10)

# list_x=list_x[0:20]
# list_y=list_y[0:20]
# list_z=list_z[0:20]

for i in range(0, len(list_x)-2):

    # xval = linearBezier(list_x[i], list_x[i + 1], .5)
    # yval = linearBezier(list_y[i], list_y[i + 1], .5)
    # zval = linearBezier(list_z[i], list_z[i + 1], .5)

    # xval = quadraticBezier(list_x[i], list_x[i + 1], list_x[i+2], .5)
    # yval = quadraticBezier(list_y[i], list_y[i + 1], list_y[i+2], .5)
    # zval = quadraticBezier(list_z[i], list_z[i + 1], list_z[i+2], .5)

    # xval = cubicBezier(list_x[i], list_x[i + 1], list_x[i+2], list_x[i+3], .5)
    # yval = cubicBezier(list_y[i], list_y[i + 1], list_y[i+2], list_y[i+3], .5)
    # zval = cubicBezier(list_z[i], list_z[i + 1], list_z[i+2], list_z[i+3], .5)

    x1=list_x[i]
    x2=list_x[i+1]
    x3=list_x[i+2]

    y1 = list_y[i]
    y2 = list_y[i + 1]
    y3 = list_y[i + 2]

    z1 = list_z[i]
    z2 = list_z[i + 1]
    z3 = list_z[i + 2]

    for u in range(0, 10, 5):
        j=u/10

        xval = quadraticBezier(x1, x2, x3, j)
        yval = quadraticBezier(y1, y2, y3, j)
        zval = quadraticBezier(z1, z2, z3, j)
        new_x.append(xval)
        new_y.append(yval)
        new_z.append(zval)

# list_x=[x+5 for x in list_x]
# list_y=[x+5 for x in list_y]
# list_z=[x-22 for x in list_z]

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(list_x, list_y, list_z, s=size, marker="o")
ax.scatter(new_x, new_y, new_z, s=size, marker="o")
plt.show()

# x=[1, 3, 1]
# y=[1, 3, 5]
#
# for i in range(0, 10):
#     x1=1
#     y1=1
#     x2=3
#     y2=3
#     x3=1
#     y3=5
#
#     # xval = linearBezier(x1, x2, i/10)
#     # yval = linearBezier(y1, y2, i/10)
#
#     xval = quadraticBezier(x1, x2, x3, i/10)
#     yval = quadraticBezier(y1, y2, y3, i/10)
#
#     print(xval)
#
#     x.append(xval)
#     y.append(yval)
#
# # fig = plt.figure()
# # ax = Axes3D(fig)
# # ax.scatter(x, y)
# plt.plot(x, y)
# plt.show()