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

    canvas = tk.Canvas(window, width=800, height=800)

    Label(window, text = 'Simulação Campos',
          font =('Verdana', 30)).pack(side = BOTTOM)

    Label(window, text = 'Positivo: Azul, Negativo: Vermelho',
          font =('Verdana', 15)).pack(side = BOTTOM)

    for carga in CampoVetorial.get_all_loads():
        DrawCarga.drawPoint(carga, canvas)

    vector_pool = VetorPool()

    # 4y espaços vezes 4x espaços vetores -> y: 100, 200, 300, 400
    # Pontos utilizados no espaço
    p1 = Point(100, 100)
    p2 = Point(100, 200)
    p3 = Point(100, 300)
    p4 = Point(100, 400)
    p5 = Point(100, 500)
    p6 = Point(100, 600)
    p7 = Point(100, 700)
    p8 = Point(200, 100)
    p9 = Point(200, 200)
    p10 = Point(200, 300)
    p11 = Point(200, 400)
    p12 = Point(200, 500)
    p13 = Point(200, 600)
    p14 = Point(200, 700)
    p15 = Point(300, 100)
    p16 = Point(300, 200)
    p17 = Point(300, 300)
    p18 = Point(300, 400)
    p19 = Point(300, 500)
    p20 = Point(300, 600)
    p21 = Point(300, 700)
    p22 = Point(400, 100)
    p23 = Point(400, 200)
    p24 = Point(400, 300)
    p25 = Point(400, 400)
    p26 = Point(400, 500)
    p27 = Point(400, 600)
    p28 = Point(400, 700)
    p29 = Point(500, 100)
    p30 = Point(500, 200)
    p31 = Point(500, 300)
    p32 = Point(500, 400)
    p33 = Point(500, 500)
    p34 = Point(500, 600)
    p35 = Point(500, 700)
    p36 = Point(600, 100)
    p37 = Point(600, 200)
    p38 = Point(600, 300)
    p39 = Point(600, 400)
    p40 = Point(600, 500)
    p41 = Point(600, 600)
    p42 = Point(600, 700)
    p43 = Point(700, 100)
    p44 = Point(700, 200)
    p45 = Point(700, 300)
    p46 = Point(700, 400)
    p47 = Point(700, 500)
    p48 = Point(700, 600)
    p49 = Point(700, 700)



    points = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41, p42, p43, p44, p45, p46, p47, p48, p49]

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
