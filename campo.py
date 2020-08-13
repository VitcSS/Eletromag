import math

class Vetor(object):
    def __init__(self, position):
        self.x , self.y = position
        self.module = math.fabs(math.sqrt((self.x**2) + (self.y**2)))
class Campo(object):

    def __init__(self, load, position):

        self.load = load
        self.position = position #  Tupla de valores (X, Y)

class CampoVetorial:
    """
        Objeto Singleton, armazenando os campos vetoriais especificos
    """
    __instance = None
    __constants = {
        'vacuo': 9E9, 
        'ar': 8.995E9,
        'agua': 0.11E9,
        'borracha': 3E9,
        'enxofre': 2.25E9,
        'quartzo': 1.8E9,
        'vidro': 1.5E9,
        'marmore': 1.125E9,
        'etanol': 0.36E9,
        'metanol:': 0.265E9,
        'glicerina': 0.18E9,


    }

    def __new__(cls):
        if CampoVetorial.__instance is None:
            CampoVetorial.__instance = object.__new__(cls)
        return CampoVetorial.__instance
