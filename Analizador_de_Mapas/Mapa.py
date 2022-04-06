from Grafica import Grafica


class Mapa:

    def __init__(self):
        self.nombre = ''
        self.ubicacion = ''
        self.posicion = 0
        self.lista_ciudades = []
        self.grafica = Grafica()

    def generar_mapa(self, nombre, posicion, lista_ciudades):
        self.nombre = nombre
        self.posicion = posicion
        self.lista_ciudades = lista_ciudades
        ciudad = self.lista_ciudades[self.posicion]

        with open('archivos_creados/mapa.txt', mode='w') as TXT:
            for fila in ciudad:
                TXT.write(fila + '\n')

        self.ubicacion = 'archivos_creados/mapa.txt'
        self.grafica.insertar_mapa(self.nombre, self.ubicacion)
