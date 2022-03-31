from xml.dom import minidom
from Mapa import Mapa


class Operaciones:

    def __init__(self):
        self.ruta_xml = ''
        self.nombres = []
        self.lista_ciudades = []
        self.ciudad = []
        self.fila = ''
        self.lista_unidades_militares = []
        self.unida_militar = []
        self.lista_robots = []
        self.robot = []
        self.mapa_txt = Mapa()

    def leer_xml(self, ruta):
        self.ruta_xml = ruta
        xml = minidom.parse(self.ruta_xml)
        ciudades = xml.getElementsByTagName('ciudad')
        robots = xml.getElementsByTagName('robot')

        for i in ciudades:
            nombre = i.getElementsByTagName('nombre')[0]
            self.nombres.append(nombre.firstChild.data)
            lista_filas = i.getElementsByTagName('fila')
            lista_unidades_militares = i.getElementsByTagName('unidadMilitar')

            for fila in lista_filas:
                self.fila = fila.firstChild.data
                self.ciudad.append(self.fila.replace('"', ''))
                self.fila = ''
            self.lista_ciudades.append(self.ciudad)
            self.ciudad = []

            for unidad in lista_unidades_militares:
                fila = unidad.getAttribute('fila')
                columna = unidad.getAttribute('columna')
                valor = unidad.firstChild.data
                self.unida_militar.append(fila)
                self.unida_militar.append(columna)
                self.unida_militar.append(valor)
                self.lista_unidades_militares.append(self.unida_militar)
                self.unida_militar = []

        for i in robots:
            tipo = i.getAttribute('tipo')
            capacidad = i.getAttribute('capacidad')
            nombre = i.firstChild.data
            self.robot.append(tipo)
            self.robot.append(capacidad)
            self.robot.append(nombre)
            self.lista_robots.append(self.robot)
            self.robot = []

    def mostrar_ciudades(self):
        posicion = 1
        total_de_ciudades = len(self.lista_ciudades)

        for nombre in self.nombres:
            print(f'{posicion}) {nombre}')
            posicion = posicion + 1

        print('                                    ')
        codigo = input('--> Seleccione una ciudad: ')

        if int(codigo) <= total_de_ciudades:
            p = int(codigo) - 1
            self.mapa_txt.generar_mapa(p, self.lista_ciudades)
        else:
            print('                    ')
            print('--> Opción no valida')
