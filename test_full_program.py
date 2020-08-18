from campo import *
from graphs import *
import sys


# Definição campo
campo = CampoVetorial('agua')
print(f'Constante: {CampoVetorial.get_constant()}\n')

# Definição primeira carga
# Modelo
# new_load = Carga(new_point_load, (new_point_x, new_point_y))
# campo.add_load(new_load)

new_load = Carga(0.2, (0, 50))
campo.add_load(new_load)

new_load = Carga(0.5, (350, 350))
campo.add_load(new_load)

print('Cargas no campo:\n')

for carga in CampoVetorial.get_all_loads():
    print(f'Carga: {carga.load}, {carga.position}\n')

# 4y espaços vezes 4x espaços vetores -> y: 100, 200, 300, 400
# Pontos utilizados no espaço
p1 = Point(100, 50)
p2 = Point(125, 75)
p3 = Point(150, 100)
p4 = Point(175, 125)
p5 = Point(200, 150)
p6 = Point(225, 175)
p7 = Point(250, 200)
p8 = Point(275, 225)
p9 = Point(300, 250)
p10 = Point(325, 275)
p11 = Point(350, 300)
p12 = Point(375, 325)
p13 = Point(400, 350)
p14 = Point(425, 375)
p15 = Point(450, 400)
p16 = Point(475, 0)

points = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]

# Vetores
vector_pool = VetorPool()
for point in points:
    new_vector = CampoVetorial.calculate_in_point(point)
    vector_pool.add_vector(new_vector)

print('Vetores no espaço:\n')
for vector in vector_pool.vectors:
    print(f'Vetor: {vector}')


# Tkinter

window = tk.Tk()
window.maxsize(800, 800)
canvas = tk.Canvas(window, width=500, height=500)

# Desenho cargas
for carga in CampoVetorial.get_all_loads():
    DrawCarga.drawPoint(carga, canvas)

canvas.pack()

try:
    if sys.argv[1] == 'single':
        canvas.create_line(10, 10, 150, 150, arrow=tk.LAST, fill='blue', width=2)
        canvas.create_line(50, 100, 600, 300, arrow=tk.LAST, fill='red', width=4)
        canvas.create_line(20, 15, 270, 300, arrow=tk.LAST, fill='green', width=8)
except IndexError:
    ExhibitVector.exhibit_all(vector_pool, canvas)

canvas.create_line(vector.xi, vector.xf, vector.yi, vector.yf, arrow=tk.LAST, fill='blue')
window.mainloop()
