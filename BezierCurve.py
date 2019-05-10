import csv
import matplotlib.pyplot as plt
import math
import time
from mpl_toolkits.mplot3d import Axes3D

#OPTIONS
#change this for different bezier curves
#"linear", "quadratic", "cubic"
bezier_type="cubic"
#change this for more or less sampling between control points
sample_rate=50
#val to end list loop
endval=0

#Bezier Curves Functions
#linear Bezier curves
def linearBezier(p0, p1, t):
    bez_val=((1-t)*p0)+(t*p1)
    return bez_val

#quadratic Bezier curves
def quadraticBezier(p0, p1, p2, t):
    bez_val=(math.pow((1-t), 2)*p0)+(2*(1-t)*t*p1)+(math.pow(t, 2)*p2)
    return bez_val

#cubic Bezier curves
def cubicBezier(p0, p1, p2, p3, t):
    bez_val=(math.pow((1-t), 3)*p0)+(3*math.pow(1-t, 2)*t*p1)+(3*(1-t)*math.pow(t, 2)*p2)+(math.pow(t, 3)*p3)
    return bez_val

#lists to store original points
list_x = []
list_y = []
list_z = []

#lists to store interpolated points
new_x=[]
new_y=[]
new_z=[]

#list to store radius values
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
        size.append(s)

#sectioning for testing
# list_x=list_x[0:200]
# list_y=list_y[0:200]
# list_z=list_z[0:200]

if bezier_type=="linear":
    endval=1
elif bezier_type=="quadratic":
    endval=2
elif bezier_type=="cubic":
    endval=3

#timing spline calculation
start=time.time()
#looping through all available points
for i in range(0, len(list_x)-endval, endval):
    #bezier curves
    if bezier_type=="linear":
        x1 = list_x[i]
        x2 = list_x[i + 1]

        y1 = list_y[i]
        y2 = list_y[i + 1]

        z1 = list_z[i]
        z2 = list_z[i + 1]

        for u in range(0, sample_rate):
            t = u / sample_rate

            xval = linearBezier(x1, x2, t)
            yval = linearBezier(y1, y2, t)
            zval = linearBezier(z1, z2, t)
            new_x.append(xval)
            new_y.append(yval)
            new_z.append(zval)

    elif bezier_type=="quadratic":
        x1 = list_x[i]
        x2 = list_x[i + 1]
        x3 = list_x[i + 2]

        y1 = list_y[i]
        y2 = list_y[i + 1]
        y3 = list_y[i + 2]

        z1 = list_z[i]
        z2 = list_z[i + 1]
        z3 = list_z[i + 2]

        for u in range(0, sample_rate):
            t = u / sample_rate

            xval = quadraticBezier(x1, x2, x3, t)
            yval = quadraticBezier(y1, y2, y3, t)
            zval = quadraticBezier(z1, z2, z3, t)
            new_x.append(xval)
            new_y.append(yval)
            new_z.append(zval)

    elif bezier_type=="cubic":
        x1 = list_x[i]
        x2 = list_x[i + 1]
        x3 = list_x[i + 2]
        x4 = list_x[i + 3]

        y1 = list_y[i]
        y2 = list_y[i + 1]
        y3 = list_y[i + 2]
        y4 = list_y[i + 3]

        z1 = list_z[i]
        z2 = list_z[i + 1]
        z3 = list_z[i + 2]
        z4 = list_z[i + 3]

        for u in range(0, sample_rate):
            t = u / sample_rate

            xval = cubicBezier(x1, x2, x3, x4, t)
            yval = cubicBezier(y1, y2, y3, y4, t)
            zval = cubicBezier(z1, z2, z3, z4, t)
            new_x.append(xval)
            new_y.append(yval)
            new_z.append(zval)
end=time.time()
print("Time (milliseconds) for spline calculation: %f" % ((end-start)*1000.0))

list_x=[x+5 for x in list_x]
list_y=[x+5 for x in list_y]
list_z=[x+5 for x in list_z]

#draw smooth path values
fig = plt.figure()
fig.suptitle("Smooth Path Values")
ax = Axes3D(fig)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.plot(list_x, list_y, list_z, color="b")

#shift spline for visibility
# new_x=[x+10 for x in new_x]
# new_y=[x+10 for x in new_y]
# new_z=[x+10 for x in new_z]

#draw spline
fig = plt.figure()
fig.suptitle("Bezier Curve Spline")
ax = Axes3D(fig)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.plot(new_x, new_y, new_z, color="m")

updated_size=[]
step_val=round(len(new_x)/len(size))

new_size_len=len(new_x)

for i in range(len(size)):
    size[i]=size[i]*25

    for j in range(step_val):
        updated_size.append(size[i])

#scatter points with size
fig = plt.figure()
fig.suptitle("Scattered Spline Points with Corridor Radius")
ax = Axes3D(fig)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.scatter(new_x, new_y, new_z, s=updated_size, marker="o", color="r")

#uncomment to show each individual
#plt.show()

#GUI functions, return required info
def getsmoothpath():
    return list_x, list_y, list_z

def getsplineandradius():
    return new_x, new_y, new_z, updated_size

#testing bezier functions
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
# plt.plot(x, y)
# plt.show()