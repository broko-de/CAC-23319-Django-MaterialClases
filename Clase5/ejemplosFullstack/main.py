from encapsulamiento.cliente import Cliente
from herencia.producto import Producto
from herencia.subclase import Alimento, Adorno, Libro

from polimorfismo.persona import Persona
from polimorfismo.subclases import Programador, Contador

from abstractas.abstracta import Animal
from abstractas.subclases import Perro, Gato

from herenciamultiple.spideruno import SpiderUno
from herenciamultiple.spiderdos import SpiderDos
from herenciamultiple.spiderverse import SpiderVerse


def main():
    

    #### ENCAPSULAMIENTO #####
    # cliente_uno = Cliente()

    # print(cliente_uno)
    # cliente_uno.nombre = 'Roberto'
    # print(cliente_uno.nombre)
    # cliente_uno.email = 'rbas@asd.com'
    # print(cliente_uno)

    ###### HERENCIA #######
    # p1 = Producto('1','Escritorio','una descripcion',6500)
    # ad1 = Adorno('2','Cuadro pintura','Obra de arte',3300)
    # l1 = Libro('3','Harry Potter','Descripcion libro',2000,'IN123','J K Rowling')
    # al1 = Alimento('4','Galletas surtido','Galletas',150,'Bagley','Un distribuidor')

    # print(p1)
    # print(ad1)
    # print(l1)
    # print(al1)

    ##### HERENCIA MULTIPLE ######
    # sv = SpiderVerse()
    # sv.bailar()
    # sv.mis_villanos()
    # sv.hablar()

    
    ###### POLIMORFISMO #######

    # persona = Persona('Fede')
    # print(persona)

    # programador = Programador('Juan')
    # print(programador)
    # programador.trabajar()

    # contador = Contador('Felipe')
    # print(contador)
    # contador.trabajar()

    # trabajadores = [programador,contador]

    # for t in trabajadores:
    #     t.trabajar()

    ###### CLASE ABSTACTA #######

    # animal = Animal() ERROR
    # perro = Perro()
    # perro.mover()
    # perro.emitir_sonido()

    # gato = Gato()
    # gato.mover()
    # gato.emitir_sonido()

    pass
   
    
if __name__ == "__main__":
    main()