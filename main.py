from campo import *
from graphs import *

if __name__ == '__main__':

    print('Bem vindo ao simulador de campo vetorial!\n')
    print('Primeiramente, defina o meio em que seu campo vetorial se situa.\n\
    Digite alguma das próximas opções ou, caso deseje utilizar o vácuo, aperte ENTER\n')

    medium = input('\tvacuo,\n\
\tar,\n\
\tagua,\n\
\tborracha,\n\
\tenxofre,\n\
\tquartzo,\n\
\tvidro,\n\
\tmarmore,\n\
\tetanol,\n\
\tmetanol,\n\
\tglicerina\n')

    try:
        campo = CampoVetorial(medium)
    except KeyError:
        print('Essa não é uma opção, utilizando o vacuo como meio\n')
        campo = CampoVetorial('vacuo')

    print(f'Valor da constante: {CampoVetorial.get_constant()}\n')

    print('Você pode adicionar o número de cargas pontuais que desejar.\n')
    print('Lembre-se, o desenho representa apenas as setas de campos em que 0 < X < 500 e 0 < Y < 500, sendo as unidades em metros.\n')
    print('Comece com a sua primeira carga:\n')

    while True:

        new_point_load = float(input('Digite a carga em coloumbs: '))
        new_point_x = float(input('\nDigite a posição da carga no eixo X em metros: '))
        new_point_y = float(input('\nDigite a posição da carga no eixo Y em metros: '))

        new_load = Carga(new_point_load, (new_point_x, new_point_y))
        campo.add_load(new_load)

        continue_program = input('\nDeseja adicionar outra carga? (y, n) ')

        if continue_program == 'n':
            break

    print('Cargas no campo:\n')

    for carga in CampoVetorial.get_all_loads():
        print(f'Carga: {carga.load}, {carga.position}\n')

    window = tk.Tk()

    canvas = tk.Canvas(window, width=600, height=600)

    Label(window, text = 'Simulação Campos',
          font =('Verdana', 30)).pack(side = BOTTOM)

    for carga in CampoVetorial.get_all_loads():
        DrawCarga.drawPoint(carga, canvas)

    vector_pool = VetorPool()

    # 4y espaços vezes 4x espaços vetores -> y: 100, 200, 300, 400
    # Pontos utilizados no espaço
    p1 = Point(100, 100)
    p2 = Point(100, 200)
    p3 = Point(100, 300)
    p4 = Point(100, 400)
    p5 = Point(200, 100)
    p6 = Point(200, 200)
    p7 = Point(200, 300)
    p8 = Point(200, 400)
    p9 = Point(300, 100)
    p10 = Point(300, 200)
    p11 = Point(300, 300)
    p12 = Point(300, 400)
    p13 = Point(400, 100)
    p14 = Point(400, 200)
    p15 = Point(400, 300)
    p16 = Point(400, 400)

    points = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]

    for point in points:
        new_vector = CampoVetorial.calculate_in_point(point)
        vector_pool.add_vector(new_vector)

    print('Vetores no espaço:\n')
    print('Cada vetor é expresso da forma (xi, xf), (yi, yf) em que xi e xf são valores arbitrários\n')
    print('Cada representação de campo utiliza uma unidade de texto para cada 1N/C\n')
    for vector in vector_pool.vectors:
        print(f'Vetor: {vector}')

    ExhibitVector.exhibit_all(vector_pool, canvas)


    canvas.pack()
    window.mainloop()
