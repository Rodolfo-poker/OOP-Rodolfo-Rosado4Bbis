#Lab 11. Exception handling OOP
#A store needs to deduct products from its inventory. The system must prevent invalid operations and communicate errors appropriately, without terminating execution unexpectedly

#Custom Exceptions

class ErrorInventario(Exception):
    pass

class ProductoNoEncontrado(ErrorInventario):
    pass

class CantidadInvalida(ErrorInventario):
    pass

class StockInsuficiente(ErrorInventario):
    pass

#Clase producto

class Producto:
    def __init__(self, codigo, stock):
        self.codigo = codigo
        self.stock = stock
        
    def retirar(self, cantidad):
        pass #replace
    
        #STEP 1: Validate that the quantity is greater than zero.
        if cantidad < 0:
            print("Ingrese un número superior a cero.")
            return
        
        #STEP 2: Validate that there is suffcient stock.
        if cantidad > self.stock:
            print("Stock insuficiente")
            return
        
        #STEP 3: Deduct the quantity from the stock.
        self.stock -= cantidad
        
#Clase inventario
class Inventario:
    def __init__(self):
        self.productos = {
            "P01": Producto("P01",5),
            "P02": Producto("P02",10),
            "P03": Producto("P03",15),
        }
    
    def retirar(self, codigo, cantidad):
        pass #replace
    
        #STEP 4: Verify that the product exists.
        if codigo not in self.productos:
            print("Producto no encontrado")
            return
        
        #STEP 5: Delegate the discount to the Product class.
        producto = self.productos[codigo]
        producto.retirar(cantidad)            
        
#Programa principal
def main():
    inventario = Inventario()
    codigo = input("Código del producto: ")
    try:
        cantidad = int(input("Cantidad a retirar: "))
        inventario.retirar(codigo, cantidad)
        
        print(
            "Retiro realizado. Stock restante:",
            inventario.productos[codigo].stock
        )
    except ValueError:
        print("La cantidad debe ser un número entero.")
    except ErrorInventario as error:
        print(f"No se pudo realizar la operación: {error}")

if __name__ == "__main__":
    main()