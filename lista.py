class Nodo:
    def __init__(self):
        self.palabra = None # todo nulo
        self.numero = 0
        self.siguiente = None # nodo nulo


class Lista:
    def __init__(self):#metodo inicial
        self.raiz = Nodo()#la raiz se crea con un nodo

    def insertar(self, nodo):
        if self.raiz.palabra == None:# si en la raiz de la palabra es nulo
            self.raiz = nodo# la raiz crea un nuevo nodo 
        else:
            aux = self.raiz # aux recorre cada elemento en la lista palabra/numero
            while True:
                if aux.siguiente == None: #si auxiliar siguiente esta vacio
                    aux.siguiente = nodo # aux siguiente sera el nuevo nodo
                    break
                else:
                    aux = aux.siguiente # de lo contrario las recorre

    def listee(self):
        aux = self.raiz
        if aux.palabra == None: # verifica si a lista esta vacia
            print("Lista vacia")
        else:
            print(aux.palabra) #sino esta vacia imprime los datos del nodo
            print(aux.numero)
            while aux.siguiente != None: #los imprime mientras haya algo diferente de nulo
                aux = aux.siguiente
                print(aux.palabra)
                print(aux.nombre)

    def eliminar(self):
        aux = self.raiz
        aux2 = self.raiz
        if aux.palabra == None: #si esta vacia no hay nada para eliminar
            print("No hay elementos que se puedan eliminar")
        else:
            elemento = input("Escribe el nombre a eliminar: ")#para buscar mediante el nombre
            if aux.palabra == elemento: #si la palabra es igual al elemento buscado
                if aux.siguiente == None:
                    self.raiz = Nodo()
                else:
                    self.raiz = aux.siguiente
            else:
                t = True
                while aux.siguiente != None and t:
                    aux = aux.siguiente
                    if aux.palabra == elemento:
                        aux2.siguiente = aux.siguiente
                        aux = None
                        t = False
                        break
                    aux2 = aux2.siguiente
                if t == True:
                    print("Nombre no encontrado")

    #def modificar(self):



class Principal:
    lista = Lista()
    while True:
        print("***Menu ***")
        print("1.- Insertar elementos")
        print("2.- Consultar elementos")
        print("3.- Eliminar elementos")
        print("4.- Modificar elementos")
        print("5.- Salir")
        try:
            opcion = int(input("Elige tu opcion: "))
            if opcion == 1:
                nodo = Nodo()
                nodo.palabra = input("Escribe cualquier palabra: ")
                nodo.numero = int(input("Escribe cualquier numero: "))
                lista.insertar(nodo)
            elif opcion == 2:
                lista.listee()
            elif opcion == 3:
                lista.eliminar()
                print("Elemento eliminado")
            elif opcion == 4:
               # lista.eliminar()
               # lista.insertar(nodo)
            elif opcion == 5:
                break
        except Exception as e:
            print("Ocurrio un error")
            print(e)