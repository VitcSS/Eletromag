from campo import *
from graphs import *

if __name__ == '__main__':

    print('Bem vindo ao simulador de campo vetorial!\n')
    print('Primeiramente, defina o meio em que seu campo vetorial se situa.\n\
    Digite alguma das próximas opções ou, caso deseje utilizar o vácuo, aperte ENTER\n')

    medium = input('vacuo,\
                    ar,\
                    agua,\
                    borracha,\
                    enxofre,\
                    quartzo,\
                    vidro,\
                    marmore,\
                    etanol,\
                    metanol,\
                    glicerina\n')

    campo = CampoVetorial(medium)

    print('Você pode adicionar o número de cargas pontuais que desejar.\n')
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

    # TODO: Calcular os vetores

    window = tk.Tk()
    window.minsize(1200, 600)

    canvas = tk.Canvas(window)

    Label(window, text = 'Simulação Campos',
          font =('Verdana', 30)).pack(side = BOTTOM)

    vector_pool = VetorPool()

    p1 = Point(10, 10)
    p2 = Point(400, 400)

    points = [p1, p2]

    for point in points:
        new_vector = CampoVetorial.calculate_in_point(point)
        vector_pool.add_vector(new_vector)
    # vector_pool.add_vector(Vetor((10,10), (30,40)))
    # vector_pool.add_vector(Vetor((60,10), (200,489)))
    # vector_pool.add_vector(Vetor((10,90), (10,40)))

    for vector in vector_pool.vectors:
        
        print(vector)


    ExhibitVector.exhibit_all(vector_pool, canvas)


    canvas.pack()
    window.mainloop()

    # ExhibitVector
