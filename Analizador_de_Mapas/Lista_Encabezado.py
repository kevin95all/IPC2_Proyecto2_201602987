from Nodo_Encabezado import NodoEncabezado


class ListaEncabezado:

    def __init__(self, tipo):
        self.primero = None
        self.ultimo = None
        self.tipo = tipo
        self.size = 0

    def insertar_nodo_encabezado(self, nuevo):
        self.size += 1
        if self.primero is None:  # -----> Es el primer nodo insertado
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            # -----> Insercion en ORDEN
            # -----> Verificamos si el nuevo nodo es menor que el primero
            if nuevo.id < self.primero.id:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            # -----> Verificamos si el nuevo es mayor que el ultimo
            elif nuevo.id > self.ultimo.id:
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            else:
                # -----> Sino, recorremos la lista para buscar donde acomodarnos, entre el primero y el ultimo
                tmp: NodoEncabezado = self.primero
                while tmp is not None:
                    if nuevo.id < tmp.id:
                        nuevo.siguiente = tmp
                        nuevo.anterior = tmp.anterior
                        tmp.anterior.siguiente = nuevo
                        tmp.anterior = nuevo
                        break
                    elif nuevo.id > tmp.id:
                        tmp = tmp.siguiente
                    else:
                        break

    def mostrar_encabezados(self):
        tmp = self.primero
        while tmp is not None:
            print('Encabezado', self.tipo, tmp.id)
            tmp = tmp.siguiente

    def get_encabezado(self, posicion) -> NodoEncabezado:  # -----> Esta funcion debe retornar un nodo cabecera
        tmp = self.primero
        while tmp is not None:
            if posicion == tmp.id:
                return tmp
            tmp = tmp.siguiente
