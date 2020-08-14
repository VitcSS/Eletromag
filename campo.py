import math

class Vetor(object):
    """
        Classe representando um vetor de força elétrica
    """
    def __init__(self, init_p, end_p, module = None):
        self.xi , self.yi = init_p
        self.xf , self.yf = end_p
        self.x = self.xf - self.xi
        self.y = self.yf - self.yi
        if module == None:
            self.module = math.fabs(math.sqrt((self.x**2) + (self.y**2)))
        else:
            self.module = module

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
    """
        Classe responsável por armazenar um objeto contendo informações de uma carga pontual
        Váriaveis armazenadas: Carga em coloumbs, posição em um campo cartesiano em metros do poto (0,0)
    """

    def __init__(self, load, position):

        self.load = load
        self.position = position #  Tupla de valores (X, Y)

class CampoVetorial:
    """
        Objeto Singleton, armazenando os campos vetoriais especificos
        Definição de constantes
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
    def calculate_in_point(vetor):
        # vetor = CampoVetorial.calculate_in_point(x)
        for input in CampoVetorial.get_all_loads():
            xi, yi = input.position
            distance = math.sqrt((vetor.xi - xi)**2  + (vetor.yi - yi)**2)
            CampoVet += (input.constant*input.load)/(distance)**2
            CampoX = CampoVet*(vetor.x-xi)/(distance)**2
            CampoY = CampoVet*(vetor.y-yi)/(distance)**2
        output = Vetor((vetor.xi, vetor.yi),(CampoX,CampoY), CampoVet)
        return output
