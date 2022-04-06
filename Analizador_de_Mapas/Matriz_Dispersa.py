from Nodo_Encabezado import NodoEncabezado
from Lista_Encabezado import ListaEncabezado
import os
import webbrowser


class NodoInterno:  # -----> Nodos ortogonales

    def __init__(self, x, y, caracter):  # -----> El caracter puede ser cualquier valor
        self.caracter = caracter
        self.coordenadaX = x  # -----> Fila
        self.coordenadaY = y  # -----> Columna
        self.arriba = None
        self.abajo = None
        self.derecha = None  # -----> self.siguiente
        self.izquierda = None  # -----> self.anterior


class MatrizDispersa:

    def __init__(self, capa):
        self.capa = capa
        self.filas = ListaEncabezado('fila')  # -----> Encabezados eje X
        self.columnas = ListaEncabezado('columna')  # -----> Encabezados eje Y

    def insert(self, pos_x, pos_y, caracter):
        nuevo = NodoInterno(pos_x, pos_y, caracter)  # -----> Se crea nodo interno
        # -----> Lo primero sera buscar si ya existen los encabezados en la matriz
        nodo_x = self.filas.get_encabezado(pos_x)
        nodo_y = self.columnas.get_encabezado(pos_y)

        if nodo_x is None:  # -----> Comprobamos que el encabezado fila pos_x exista
            # -----> Si nodo_X es nulo, quiere decir que no existe encabezado pos_x, por lo tanto hay que crearlo
            nodo_x = NodoEncabezado(pos_x)
            self.filas.insertar_nodo_encabezado(nodo_x)

        if nodo_y is None:  # -----> Comprobamos que el encabezado columna pos_y exista
            # -----> Si nodo_Y es nulo, quiere decir que no existe encabezado pos_y, por lo tanto hay que crearlo
            nodo_y = NodoEncabezado(pos_y)
            self.columnas.insertar_nodo_encabezado(nodo_y)

        # -----> INSERTAR NUEVO EN FILA
        if nodo_x.acceso is None:  # -----> Comprobamos que el nodo_x no esta apuntando hacia ningun nodoInterno
            nodo_x.acceso = nuevo
        else:
            if nuevo.coordenadaY < nodo_x.acceso.coordenadaY:  # -----> F1 --->  NI 1,1     NI 1,3
                nuevo.derecha = nodo_x.acceso
                nodo_x.acceso.izquierda = nuevo
                nodo_x.acceso = nuevo
            else:
                tmp: NodoInterno = nodo_x.acceso  # -----> nodo_X:F1 --->      NI 1,2; NI 1,3; NI 1,5;
                while tmp is not None:  # -----> NI 1,6
                    if nuevo.coordenadaY < tmp.coordenadaY:
                        nuevo.derecha = tmp
                        nuevo.izquierda = tmp.izquierda
                        tmp.izquierda.derecha = nuevo
                        tmp.izquierda = nuevo
                        break
                    elif nuevo.coordenadaX == tmp.coordenadaX and nuevo.coordenadaY == tmp.coordenadaY:
                        break
                    else:
                        if tmp.derecha is None:
                            tmp.derecha = nuevo
                            nuevo.izquierda = tmp
                            break
                        else:
                            tmp = tmp.derecha
                            #         nodo_Y:        C1    C3      C5      C6
                            # nodo_X:F1 --->      NI 1,2; NI 1,3; NI 1,5; NI 1,6;
                            # nodo_X:F2 --->      NI 2,2; NI 2,3; NI 2,5; NI 2,6;

        # -----> INSERTAR NUEVO EN COLUMNA
        if nodo_y.acceso is None:  # -----> Comprobamos que el nodo_y no esta apuntando hacia ningun nodoCelda
            nodo_y.acceso = nuevo
        else:
            if nuevo.coordenadaX < nodo_y.acceso.coordenadaX:
                nuevo.abajo = nodo_y.acceso
                nodo_y.acceso.arriba = nuevo
                nodo_y.acceso = nuevo
            else:
                # -----> De no cumplirse, debemos movernos de arriba hacia abajo buscando donde posicionar el NUEVO
                tmp2: NodoInterno = nodo_y.acceso
                while tmp2 is not None:
                    if nuevo.coordenadaX < tmp2.coordenadaX:
                        nuevo.abajo = tmp2
                        nuevo.arriba = tmp2.arriba
                        tmp2.arriba.abajo = nuevo
                        tmp2.arriba = nuevo
                        break
                    elif nuevo.coordenadaX == tmp2.coordenadaX and nuevo.coordenadaY == tmp2.coordenadaY:
                        break
                    else:
                        if tmp2.abajo is None:
                            tmp2.abajo = nuevo
                            nuevo.arriba = tmp2
                            break
                        else:
                            tmp2 = tmp2.abajo

    def graficar_neato(self, nombre):
        contenido = '''digraph G{
    node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
    edge[style = "bold"]
    node[label = "capa:''' + str(self.capa) + '''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{}" \nfontname="Arial Black" \nfontsize="25pt" \n
                    \n'''.format('\nMATRIZ DISPERSA')

        # -----> Graficar nodos ENCABEZADO
        # -----> Graficar nodos fila
        pivote = self.filas.primero
        posx = 0
        while pivote is not None:
            contenido += '\n\tnode[label = "F{}" fillcolor="azure3" pos="-1,-{}!" shape=box]x{};'.format(pivote.id,
                                                                                                         posx,
                                                                                                         pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente is not None:
            contenido += '\n\tx{}->x{};'.format(pivote.id, pivote.siguiente.id)
            contenido += '\n\tx{}->x{}[dir=back];'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{};'.format(self.filas.primero.id)

        # -----> Graficar nodos columna
        pivotey = self.columnas.primero
        posy = 0
        while pivotey is not None:
            contenido += '\n\tnode[label = "C{}" fillcolor="azure3" pos = "{},1!" shape=box]y{};'.format(pivotey.id,
                                                                                                         posy,
                                                                                                         pivotey.id)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente is not None:
            contenido += '\n\ty{}->y{};'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=back];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{};'.format(self.columnas.primero.id)

        # -----> Ya con las cabeceras graficadas, lo siguiente es los nodos internos, o nodosCelda
        pivote = self.filas.primero
        posx = 0
        while pivote is not None:
            pivote_celda: NodoInterno = pivote.acceso
            while pivote_celda is not None:
                # -----> Buscamos pos(y)
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey is not None:
                    if pivotey.id == pivote_celda.coordenadaY:
                        break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.caracter == '*':
                    contenido += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format(
                        # -----> pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == ' ':
                    contenido += '\n\tnode[label="*" fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format(
                        # -----> pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'E':
                    contenido += '\n\tnode[label="*" fillcolor="green" pos="{},-{}!" shape=box]i{}_{};'.format(
                        # -----> pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'C':
                    contenido += '\n\tnode[label="*" fillcolor="blue" pos="{},-{}!" shape=box]i{}_{};'.format(
                        # -----> pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'R':
                    contenido += '\n\tnode[label="*" fillcolor="gray" pos="{},-{}!" shape=box]i{}_{};'.format(
                        # -----> pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                else:
                    contenido += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format(
                        # -----> pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                pivote_celda = pivote_celda.derecha

            pivote_celda = pivote.acceso
            while pivote_celda is not None:
                if pivote_celda.derecha is not None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                                                              pivote_celda.derecha.coordenadaX,
                                                              pivote_celda.derecha.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX,
                                                                        pivote_celda.coordenadaY,
                                                                        pivote_celda.derecha.coordenadaX,
                                                                        pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha

            contenido += '\n\tx{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\tx{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX,
                                                             pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1

        pivote = self.columnas.primero
        while pivote is not None:
            pivote_celda: NodoInterno = pivote.acceso
            while pivote_celda is not None:
                if pivote_celda.abajo is not None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                                                              pivote_celda.abajo.coordenadaX,
                                                              pivote_celda.abajo.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX,
                                                                        pivote_celda.coordenadaY,
                                                                        pivote_celda.abajo.coordenadaX,
                                                                        pivote_celda.abajo.coordenadaY)
                pivote_celda = pivote_celda.abajo
            contenido += '\n\ty{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\ty{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX,
                                                             pivote.acceso.coordenadaY)
            pivote = pivote.siguiente

        contenido += '\n}'
        # -----> Se genera DOT y se procede a ecjetuar el comando
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}.pdf".format(nombre)
        os.system("neato -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)

    def graficar_dot(self, nombre):
        # -----> Lo primero es settear los valores que nos preocupan
        grafo = 'digraph T{ \nnode[shape=box fontname="Arial" fillcolor="white" style=filled ]'
        grafo += '\nroot[label = \"capa: ' + str(self.capa) + '\", group=1]\n'
        grafo += '''label = "{}" \nfontname="Arial Black" \nfontsize="15pt" \n
                    \n'''.format('MATRIZ DISPERSA')

        # --- lo siguiente es escribir los nodos encabezados, empezamos con las filas, los nodos tendran el foramto Fn
        x_fila = self.filas.primero
        while x_fila is not None:
            grafo += 'F{}[label="F{}",fillcolor="plum",group=1];\n'.format(x_fila.id, x_fila.id)
            x_fila = x_fila.siguiente

        # -----> Apuntamos los nodos F entre ellos
        x_fila = self.filas.primero
        while x_fila is not None:
            if x_fila.siguiente is not None:
                grafo += 'F{}->F{};\n'.format(x_fila.id, x_fila.siguiente.id)
                grafo += 'F{}->F{};\n'.format(x_fila.siguiente.id, x_fila.id)
            x_fila = x_fila.siguiente

        # -----> Luego de los nodos encabezados fila, seguimos con las columnas, los nodos tendran el foramto Cn
        y_columna = self.columnas.primero
        while y_columna is not None:
            group = int(y_columna.id) + 1
            grafo += 'C{}[label="C{}",fillcolor="powderblue",group={}];\n'.format(y_columna.id, y_columna.id,
                                                                                  str(group))
            y_columna = y_columna.siguiente

        # -----> Apuntamos los nodos C entre ellos
        cont = 0
        y_columna = self.columnas.primero
        while y_columna is not None:
            if y_columna.siguiente is not None:
                grafo += 'C{}->C{}\n'.format(y_columna.id, y_columna.siguiente.id)
                grafo += 'C{}->C{}\n'.format(y_columna.siguiente.id, y_columna.id)
            cont += 1
            y_columna = y_columna.siguiente

        # -----> Luego que hemos escrito todos los nodos encabezado, apuntamos el nodo root hacua ellos
        y_columna = self.columnas.primero
        x_fila = self.filas.primero
        grafo += 'root->F{};\n root->C{};\n'.format(x_fila.id, y_columna.id)
        grafo += '{rank=same;root;'
        cont = 0
        y_columna = self.columnas.primero
        while y_columna is not None:
            grafo += 'C{};'.format(y_columna.id)
            cont += 1
            y_columna = y_columna.siguiente
        grafo += '}\n'
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux is not None:
            cont += 1
            while aux2 is not None:
                if aux2.caracter == '*':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="black"];\n'.format(aux2.coordenadaX,
                                                                                          aux2.coordenadaY,
                                                                                          aux2.caracter,
                                                                                          int(aux2.coordenadaY) + 1)
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux is not None:
                aux2 = aux.acceso
        aux = self.filas.primero
        aux2 = aux.acceso
        while aux is not None:
            rank = '{' + f'rank = same;F{aux.id};'
            cont = 0
            while aux2 is not None:
                if cont == 0:
                    grafo += 'F{}->N{}_{};\n'.format(aux.id, aux2.coordenadaX, aux2.coordenadaY)
                    grafo += 'N{}_{}->F{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux.id)
                    cont += 1
                if aux2.derecha is not None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux2.derecha.coordenadaX,
                                                        aux2.derecha.coordenadaY)
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.derecha.coordenadaX, aux2.derecha.coordenadaY,
                                                        aux2.coordenadaX, aux2.coordenadaY)

                rank += 'N{}_{};'.format(aux2.coordenadaX, aux2.coordenadaY)
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux is not None:
                aux2 = aux.acceso
            grafo += rank + '}\n'
        aux = self.columnas.primero
        aux2 = aux.acceso
        while aux is not None:
            cont = 0
            grafo += ''
            while aux2 is not None:
                if cont == 0:
                    grafo += 'C{}->N{}_{};\n'.format(aux.id, aux2.coordenadaX, aux2.coordenadaY)
                    grafo += 'N{}_{}->C{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux.id)
                    cont += 1
                if aux2.abajo is not None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.abajo.coordenadaX, aux2.abajo.coordenadaY,
                                                        aux2.coordenadaX, aux2.coordenadaY)
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux2.abajo.coordenadaX,
                                                        aux2.abajo.coordenadaY)
                aux2 = aux2.abajo
            aux = aux.siguiente
            if aux is not None:
                aux2 = aux.acceso
        grafo += '}'

        # -----> Luego de crear el contenido del Dot, procedemos a colocarlo en un archivo
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as f:
            f.write(grafo)
        result = "matriz_{}.pdf".format(nombre)
        os.system("dot -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)
