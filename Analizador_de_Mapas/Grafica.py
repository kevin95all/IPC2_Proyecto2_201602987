from Matriz_Dispersa import MatrizDispersa


class Grafica:

    def __init__(self):
        self.nombre = ''
        self.ubicacion = ''
        self.matriz = MatrizDispersa(0)

    def insertar_mapa(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        with open(self.ubicacion) as archivo:
            f = 0
            c = 0
            lineas = archivo.readlines()
            for linea in lineas:
                columnas = linea
                f += 1
                for col in columnas:
                    if col != '\n':
                        c += 1
                        self.matriz.insert(f, c, col)
                c = 0
                self.matriz.graficar_neato(self.nombre)
