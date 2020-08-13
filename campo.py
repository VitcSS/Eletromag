class Campo(object):
    __constants = {
        'vacuo': 9E9,
        'ar': 8.995E9
    }

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
        'ar': 8.995E9
    }

    def __new__(cls):
        if CampoVetorial.__instance is None:
            CampoVetorial.__instance = object.__new__(cls)
        return CampoVetorial.__instance
