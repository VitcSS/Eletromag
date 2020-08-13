from campo import *
from graphs import *

if __name__ == '__main__':

    campo = CampoVetorial()

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
                    glicerina')

    print('Você pode adicionar o número de cargas pontuais que desejar.\n')
    print('Comece com a sua primeira carga:\n')

    while True:

        new_point_load = input('Digite a carga em coloumbs: ')
        new_point_x = input('\nDigite a posição da carga no eixo X: ')
        new_point_y = input('\nDigite a posição da carga no eixo Y ')

        new_load = Carga(new_point_load, (new_point_x, new_point_y))
        campo.add_load(new_load)

        continue_program = input('\nDeseja adicionar outra carga? (y, n) ')
        if continue_program == 'n':
            break
