from abstractas.abstracta import Animal

class Gato(Animal):

    def mover(self):
        print('El gato se mueve')

    def emitir_sonido(self):
        super().emitir_sonido()
        print('Miauu! Miauuu!')


class Perro(Animal):

    def mover(self):
        print('El perro se mueve')

    def emitir_sonido(self):
        super().emitir_sonido()
        print('Guauuu! Guauuu!')

