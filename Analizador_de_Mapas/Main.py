from tkinter import *
from tkinter import filedialog
from Operaciones import Operaciones


class Main:

    def __init__(self):
        self.ruta = ''
        self.op = ''
        self.salida = False
        self.ciudad_seleccionado = False
        self.operaciones = Operaciones()

    def menu_principal(self):
        while not self.salida:
            print('                                            ')
            print('┌------------- MENU PRINCIPAL -------------┐')
            print('|                                          |')
            print('|          1)   Cargar archivo             |')
            print('|          2)   Seleccionar ciudad         |')
            print('|          3)   Ejecutar misiones          |')
            print('|          4)   Salir                      |')
            print('|                                          |')
            print('└------------------------------------------┘')
            print('                                            ')

            self.op = input('--> Ingrese una opción: ')

            if self.op == '1':
                self.cargar_archivo()

            elif self.op == '2':
                self.seleccionar_ciudad()

            elif self.op == '3':
                self.ejecutar_misiones()

            elif self.op == '4':
                self.salir()

            else:
                print('                    ')
                print('--> Opción no valida')

    def cargar_archivo(self):
        ventana = Tk()
        respaldo = self.ruta
        self.ruta = ''

        self.ruta = filedialog.askopenfilename(
            title='Buscar archivo',
            filetypes=[
                ('Archivos xml', '*.xml'),
                ('Todos los archivos', '*.*')
            ]
        )
        if self.ruta == '':
            self.ruta = respaldo
            print('                              ')
            print('--> No se cargo ningun archivo')
        else:
            self.operaciones.leer_xml(self.ruta)
            print('                             ')
            print('--> Archivo cargado con exito')
        ventana.mainloop()

    def seleccionar_ciudad(self):
        if self.ruta == '':
            print('                                   ')
            print('--> No se ha cargado ningun archivo')
        else:
            print('                             ')
            print('Lista de ciudades disponibles')
            self.ciudad_seleccionado = True

    def ejecutar_misiones(self):
        if self.ruta == '':
            print('                                   ')
            print('--> No se ha cargado ningun archivo')
        else:
            if not self.ciudad_seleccionado:
                print('                                    ')
                print('--> No se ha seleccionado una ciudad')
            else:
                pass

    def salir(self):
        print('                       ')
        print('--> Programa finalizado')
        self.ruta = ''
        self.op = ''
        self.ciudad_seleccionado = False
        self.salida = True


app = Main()
app.menu_principal()
