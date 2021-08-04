
from Entregable import Entregable

def count_elements(elements):
    entregados = 0
    for i in elements:
        if i.isEntregado() == True:
            print('{0} esta entregado.'.format(i.get_Titulo() ) )
            entregados = entregados + 1
    return entregados

def max_counter(elements):

    for i in elements:
        if i.isEntregado() == True:
            print('{0} esta entregado.'.format(i.get_Titulo() ) )
            entregados = entregados + 1
    return entregados

if __name__ == '__main__':

    lst_series = []
    lst_videojuegos = []

    #Series
    stars   = Entregable('Serie','stars',4,False,'sci/fi','Darwin')
    unit    = Entregable('Serie','unit',3,False,'sci/fi','Darwin')
    wars    = Entregable('Serie','wars',2,False,'sci/fi','Darwin')
    defcon  = Entregable('Serie','defcon',1,False,'sci/fi','Darwin')
    altered = Entregable('Serie','altered',5,False,'sci/fi','Darwin')

    lst_series.extend([stars, unit, wars, defcon, altered])

    #Videojuegos

    cs     = Entregable('Videojuego', 'cs',20,False,'shooter','valve')
    aoe    = Entregable('Videojuego', 'aoe',50,False,'shooter','bliz')
    sc     = Entregable('Videojuego', 'sc',60,False,'shooter','bliz')
    hots   = Entregable('Videojuego', 'hots',10,False,'shooter','bliz')
    ow     = Entregable('Videojuego', 'ow',12,False,'shooter','bliz')

    lst_videojuegos.extend([cs, aoe, sc, hots, ow])


    stars.entregar()
    defcon.entregar()
    aoe.entregar()
    ow.entregar()

    entregados = 0
    entregados += count_elements(lst_series)
    entregados += count_elements(lst_videojuegos)

    print('El numero de Series y Videojuegos entregados es: {0}'.format(entregados))

