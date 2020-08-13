class Campo(object):
    __constants = {
        'vacuo': 9E9,
        'ar': 8.995E9
    }

    def __init__(self, load, position, constant=None):

        self.load = load
        self.position = position #  Tupla de valores (X, Y)
        if constant is not None:
            constant = Campo.__constants['vacuo']
        else:
            constant = Campo.__constants[constant]
