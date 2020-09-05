from repositorios import Repositorios
import operator

class ProductoService():
    pass

    def add_producto(self, producto):
        lKey = -1
        for key in Repositorios.productosList:
            lKey = key
        lKey = lKey + 1
        Repositorios.productosList[lKey] = producto.__dict__
        return lKey

    def delete_producto(self, key):
        lastkey = len(Repositorios.productosList)
        if key > lastkey:
            raise ValueError
        del Repositorios.productosList[key]

    def get_productosList(self):
        return Repositorios.productosList

    def insertion_sort_precio(self, diccionario, tipoOrden):
        if tipoOrden == "ascendente":
            for i in range(1, len(diccionario)):
                #guarda el precio de la primera iteracion
                valorPrecio = diccionario[i]['_precio']
                #entra en el bucle si encuentra un precio mas grande que se encuentre en un indice anterior
                while i > 0 and diccionario[i-1]['_precio'] > valorPrecio:
                    #intercambia las posiciones 
                    diccionario[i], diccionario[i-1] = diccionario[i-1], diccionario[i]
                    i = i-1
            return diccionario
        #Realiza el mismo proceso pero a la inversa
        for i in range(1, len(diccionario)):
            valorPrecio = diccionario[i]['_precio']
            #Entra en el bucle cuando encuentra un precio menor en una posicion posterior
            while i > 0 and diccionario[i-1]['_precio'] < valorPrecio:
                diccionario[i], diccionario[i-1] = diccionario[i-1], diccionario[i]
                i = i-1
        return diccionario

    def busquedaBinaria(self, diccionario, precioBuscado):
        self.insertion_sort_precio(diccionario, "ascendente")
        primerElemento = 0
        ultimoElemnto = len(Repositorios.productosList) - 1
        bandera = False

        while primerElemento <= ultimoElemnto and not bandera:
            mitadArray = (primerElemento + ultimoElemnto) // 2
            if Repositorios.productosList[mitadArray]['_precio'] == precioBuscado:
                bandera = True
                return Repositorios.productosList[mitadArray]
            else:
                if precioBuscado < Repositorios.productosList[mitadArray]['_precio']:
                    ultimoElemnto = mitadArray - 1
                else:
                    primerElemento = mitadArray + 1

        return True