from producto import Producto
from producto_electronico import ProductoElectronico
from marca import Marca

# Producto normal
producto1 = Producto("Arroz", 2.50, 10)

print("Producto normal:")
print("Nombre:", producto1.get_nombre())
print("Precio:", producto1.get_precio())
print("Cantidad:", producto1.get_cantidad())

print("--------------------")

# Marca
marca1 = Marca("Samsung")

# Producto electrónico
producto2 = ProductoElectronico("Televisor", 500, 5, 2, marca1)

print("Producto electrónico:")
print("Nombre:", producto2.get_nombre())
print("Precio:", producto2.get_precio())
print("Cantidad:", producto2.get_cantidad())
print("Garantía:", producto2.get_garantia(), "años")
print("Marca:", producto2.get_marca().get_nombre())