import numpy as np
import tkinter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
import random
from PIL import Image

if __name__=="__main__":
    #GUI
    #window=tkinter.Tk(className="2D Cubic Spline")
    #window.mainloop()

    #size=15
    #matrix=np.zeros((size, size), dtype=float)

    input_file=open("input.txt")
    x=[]
    y=[]
    for line in input_file:
        point=line.split(",")
        x.append(int(point[0]))
        y.append(int(point[1]))
        #matrix[size-x][size-y]=1

    new_y=y[0]+(8-x[0])/(x[1]-x[0])*(y[1]-y[0])
    # print(new_y)
    x.append(8)
    y.append(new_y)

    #plt.scatter(x, y)
    #plt.show()
    input_file.close()

    list_x=[]
    list_y=[]
    list_z=[]
    size=[]

    with open("smooth_path.csv", newline="") as csv_file:
        path=csv.reader(csv_file, delimiter=" ")

        for row in path:
            row=row[0].split(",")
            x=float(row[0])
            y=float(row[1])
            z=float(row[2])
            list_x.append(x)
            list_y.append(y)
            list_z.append(z)

    with open("Gcorridor.csv", newline="") as csv_file:
        corridor=csv.reader(csv_file, delimiter=" ")

        for row in corridor:
            row=row[0].split(",")
            num=int(row[0])
            s=float(row[1])
            size.append(s)

    fig=plt.figure()
    ax=Axes3D(fig)

    list_x=list(list_x)
    list_y=list(list_y)
    list_z=list(list_z)

    ax.scatter(list_x, list_y, list_z, s=size, marker="o")
    plt.show()

    i=0
    arr=np.zeros((256, 256), dtype=np.uint8)

    with open("MRcolorData1.txt", newline="") as csv_file:
        colordata=csv.reader(csv_file, delimiter=" ")

        for row in colordata:

            row=row[0].split(",")
            num=int(row[0])
            x=int(row[1])
            y=int(row[2])
            intensity=int(row[3])

            arr[x][y]=intensity

            i+=1

            if num==50:
               break

        # im=Image.new("L", (144, 144))
        # pix=im.load()
        # for x in range(144):
        #     for y in range(144):
        #         pix[x,y]=0

        # im.save("test.png", "PNG")
        print(arr)
        img=Image.fromarray(arr, "L")
        img.show()
        img.save("test.png")

# import numpy as np
# import matplotlib.pyplot as plt
#
# # generate some data
# ax = np.arange(-9, 10)
# X, Y = np.meshgrid(ax, ax)
# print(X)
# Z = X ** 2 + Y ** 2
#
# # normalize the data and convert to uint8 (grayscale conventions)
# zNorm = (Z - Z.min()) / (Z.max() - Z.min()) * 255
# zNormUint8 = zNorm.astype(np.uint8)
#
# # plot result
# plt.figure()
# plt.imshow(zNormUint8)
# plt.show()