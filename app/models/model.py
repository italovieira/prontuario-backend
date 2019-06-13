class Model:
    def __init__(self, args):
            for key in args:
                setattr(self, key, args[key])
