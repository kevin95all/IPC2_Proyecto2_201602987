class Mapa:

    def __init__(self):
        self.posicion = 0
        self.lista_ciudades = []

    def generar_mapa(self, posicion, lista_ciudades):
        self.posicion = posicion
        self.lista_ciudades = lista_ciudades
        ciudad = self.lista_ciudades[self.posicion]

        with open('archivos_creados/mapa.txt', mode='w') as TXT:
            for fila in ciudad:
                TXT.write(fila + '\n')
