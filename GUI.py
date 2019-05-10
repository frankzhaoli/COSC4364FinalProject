from tkinter import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk,Image
from tkinter import filedialog
import csv


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("3-D Spline")
        self.minsize(1500, 750)
        self.matplotcanvas()
        self.imagecanvas()






        btn = Button(self, text="Choose File", command=self.filex)
        btn.pack(side=BOTTOM)

    def filex(self):
        files = filedialog.askopenfilenames()

    def matplotcanvas(self):
        #first graph
        fig=Figure(figsize=(5,5),dpi=100,edgecolor='r',facecolor='g')
        ax=fig.add_subplot(111)
        ax = Axes3D(fig)
        graph=FigureCanvasTkAgg(fig,self)
        graph.draw()

        list_x = []
        list_y = []
        list_z = []
        size = []

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



        list_x = list(list_x)
        list_y = list(list_y)
        list_z = list(list_z)

        ax.scatter(list_x, list_y, list_z, s=size, marker="o")


        graph.get_tk_widget().pack(padx=50,side=LEFT)

        #second graph
        f=Figure(figsize=(4,4), dpi=100)
        t = f.add_subplot(111)
        t.plot([1, 2, 3, 4, 5])
        graph1 = FigureCanvasTkAgg(f,self)
        graph1.draw()
        graph1.get_tk_widget().pack(padx=90, side=LEFT)

    def imagecanvas(self):
        # Create a canvas
        canvas = Canvas(self, width=400, height=300)
        canvas.pack(side=LEFT)
        im = Image.open('img_lights.jpg')
        canvas.image = ImageTk.PhotoImage(im)
        canvas.create_image(0, 0, image=canvas.image, anchor='nw')



if __name__ ==  '__main__':
    window=Window()

    window.mainloop()




