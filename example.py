import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window)
canvas.pack()

canvas.create_line(0, 0, 200, 100, arrow=tk.LAST)

window.mainloop()
 
