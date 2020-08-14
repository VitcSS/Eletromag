import tkinter as tk
from tkinter import *
from campo import *

class ExhibitVector:
    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def exhibit(vector, canvas):
        canvas.create_line(vector.xi, vector.xf, vector.yi, vector.yf, arrow=tk.LAST, fill='blue')

    @staticmethod
    def exhibit_all(vectorPool, canvas):
        for vector in vectorPool.vectors:
            ExhibitVector.exhibit(vector, canvas)

if __name__ == '__main__':
    window = tk.Tk()
    window.minsize(1200, 600)

    canvas = tk.Canvas(window)
    canvas.pack()

    Label(window, text = 'Simulação Campos',
          font =('Verdana', 30)).pack(side = BOTTOM)

    vector_pool = VetorPool()
    vector_pool.add_vector(Vetor((10,10), (30,40)))
    vector_pool.add_vector(Vetor((60,10), (200,489)))
    vector_pool.add_vector(Vetor((10,90), (10,40)))


    ExhibitVector.exhibit_all(vector_pool, canvas)

    canvas.create_line(10, 10, 200, 100, arrow=tk.LAST, fill='blue')
    canvas.create_line(50, 50, 100, 50, arrow=tk.LAST, fill='red')

    window.mainloop()
