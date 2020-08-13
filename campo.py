import math

class Vetor(object):
    def __init__(self, position):
        self.x , self.y = position
        self.module = math.fabs(math.sqrt((self.x**2) + (self.y**2)))

class VetorPool:
    def __init__(self, vectors=set()):
        """
            Instanciação de um objeto que armazenará todos os vetores calculados
            Podem ser passados como um set na criação , ex: vect_pool = VetorPool({vect1, vect2})
            Pode ser passado instaciado e adicionado os vetores posteriormente, ex: vect_pool = VetorPool()
            vect_pool.add_vector(vetor)
        """
        self.vectors = vectors

    def add_vector(self, vector):
        self.vectors.add(vector)


class Carga(object):

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

    __camps = set()

    def __new__(cls, constant=None):
        if CampoVetorial.__instance is None:
            CampoVetorial.__instance = object.__new__(cls)
        return CampoVetorial.__instance

    def __init__(self, constant = None):
        if constant is not None:
            self.constant = CampoVetorial.__constants[constant]
        else:
            self.constant = CampoVetorial.__constants['vacuo']

    def add_load(cls, camp):
        cls.__camps.add(camp)

    @classmethod
    def get_all_loads(cls):
        return cls.__camps

    @classmethod
    def get_constant(cls):
        campo = cls.__instance
        return campo.constant

    @staticmethod
    def calculate_in_point(loads):
        # vetor = CampoVetorial.calculate_in_point(x)
        pass
