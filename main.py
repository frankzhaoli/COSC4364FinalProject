import BezierCurve
import warnings
warnings.simplefilter("ignore", UserWarning)
from tkinter import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk,Image
from tkinter import filedialog


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("3-D Cubic Spline")
        self.minsize(1500, 750)
        self.matplotcanvas()
        #self.imagecanvas()

        #btn = Button(self, text="Choose File", command=self.filex)
        #btn.pack(side=BOTTOM)

    def filex(self):
        files = filedialog.askopenfilenames()

    def matplotcanvas(self):
        list_x, list_y, list_z=BezierCurve.getsmoothpath()
        new_x, new_y, new_z, updated_size=BezierCurve.getsplineandradius()

        #first graph
        fig=Figure(figsize=(5,5),dpi=100,edgecolor='r',facecolor='g')
        fig.suptitle("Smooth Path Values")
        ax = Axes3D(fig)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        graph=FigureCanvasTkAgg(fig,self)
        graph.draw()
        ax.plot(list_x, list_y, list_z, color="b")
        graph.get_tk_widget().pack(padx=50,side=LEFT)

        #second graph
        fig=Figure(figsize=(5,5),dpi=100,edgecolor='r',facecolor='g')
        fig.suptitle("Bezier Curve Spline")
        ax = Axes3D(fig)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        graph=FigureCanvasTkAgg(fig,self)
        graph.draw()
        ax.plot(new_x, new_y, new_z, color="m")
        graph.get_tk_widget().pack(padx=50,side=LEFT)

        #third graph
        fig=Figure(figsize=(5,5),dpi=100,edgecolor='r',facecolor='g')
        fig.suptitle("Scattered Spline Points with Corridor Radius")
        ax = Axes3D(fig)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        graph=FigureCanvasTkAgg(fig,self)
        graph.draw()
        ax.scatter(new_x, new_y, new_z, s=updated_size, marker="o", color="r")
        graph.get_tk_widget().pack(padx=50,side=LEFT)

    def imagecanvas(self):
        # Create a canvas
        canvas = Canvas(self, width=400, height=300)
        canvas.pack(side=LEFT)
        im = Image.open('test.png')
        canvas.image = ImageTk.PhotoImage(im)
        canvas.create_image(0, 0, image=canvas.image, anchor='nw')

if __name__ ==  '__main__':
    window=Window()

    window.mainloop()



