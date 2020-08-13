class Campo(object):
    __constants = {
        'vacuo': 9E9,
    }

    def __init__(self, load, position, constant=None):

        self.load = load
        self.position = self
        if constant is not None:
            constant = Campo.__constants['vacuo']
        else:
            constant = Campo.__constants[constant]
