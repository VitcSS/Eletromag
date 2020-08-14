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

        new_point_load = int(input('Digite a carga em coloumbs: '))
        new_point_x = int(input('\nDigite a posição da carga no eixo X em metros: '))
        new_point_y = int(input('\nDigite a posição da carga no eixo Y em metros: '))

        new_load = Carga(new_point_load, (new_point_x, new_point_y))
        campo.add_load(new_load)

        continue_program = input('\nDeseja adicionar outra carga? (y, n) ')
        if continue_program == 'n':
            break

    # all_vectors = VetorPool()

    # TODO: Calcular os vetores

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


    window.mainloop()

    ExhibitVector
