class NodoEncabezado:

    def __init__(self, posicion):
        self.id: int = posicion  # -----> Posicion de fila o columna
        self.siguiente = None
        self.anterior = None
        self.acceso = None
