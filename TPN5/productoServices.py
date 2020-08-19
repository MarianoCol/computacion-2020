from repositorios import Repositorios

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
