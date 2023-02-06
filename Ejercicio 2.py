# Añadir una clase Pedido que tiene como atributos:
#     - lista de productos
#     - lista de cantidades
# Añade las siguiente funcionalidad:
#     - total_pedido: muestra el precio final del pedido
#     - mostrar_productos: muestra los productos del pedido

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre (self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio (self, valor):
        self.__precio = valor

    def total(self, unidades):
        return self.precio * unidades

    def __str__(self):
        return 'Codigo: ' + str(self.__codigo) + ', nombre: ' + self.__nombre + ', precio: ' + str(self.__precio)

class Preciso:
    def __init__(self, producto, cantidades):
        self.__producto = producto
        self.__cantidades = cantidades

    def total(self):
        total = 0

        for (p,c) in zip(self.__producto, self.__cantidades):
            total = total + p.total(c)

        return total

    def mostrar_total(self):
        for (p, c) in zip(self.__producto, self.__cantidades):
            print(p.nombre, "Cantidad " + str(c))

p1 = Producto(1, "Producto 1", 5)
p2 = Producto(2, "Producto 2", 10)
p3 = Producto(3, "Producto 3", 20)

print("El total del primer producto es: " + str(p1.total(5)) + "€")
print("El total del segundo producto es: " + str(p2.total(5)) + "€")
print("El total del tercer producto es: " + str(p3.total(7)) + "€")

producto = [p1, p2, p3]
cantidades = [5, 10, 20]

precio = Preciso(producto, cantidades)

print("Total pedido: " + str(precio.total()))

precio.mostrar_total()