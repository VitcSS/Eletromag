import tkinter as tk
from tkinter import *

if __name__ == '__main__':
    window = tk.Tk()
    window.minsize(1200, 600)

    canvas = tk.Canvas(window)
    canvas.pack()

    Label(window, text = 'Simulação Campos',
          font =('Verdana', 30)).pack(side = BOTTOM)

    canvas.create_line(10, 10, 200, 100, arrow=tk.LAST, fill='blue')
    canvas.create_line(50, 50, 100, 50, arrow=tk.LAST, fill='red')

    window.mainloop()
