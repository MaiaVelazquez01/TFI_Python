from utils.helpers import *
from utils import db_manager
import sys

# Muestra uno o varios productos en formato detallado
# Recibe una lista de productos
def mostrar_productos(productos):
    if not productos:
        print("No se encontraron productos.")
        return
    
    for producto in productos:
        print(f"ID: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Descripción: {producto[2]}")
        print(f"Cantidad: {producto[3]}")
        print(f"Precio: ${producto[4]:.2f}")
        print(f"Categoria: {producto[5]}")
        print("-" * 30)
 
# Menú: Registro de un nuevo producto
# Cada campo se valida antes de enviarse a la BD     
def menu_registrar_producto():
    imprimir_titulo("Registrar producto")
    nombre = validar_string("Ingrese nombre del producto")
    descripcion = input("Ingrese descripcion del producto (opcional): ").strip().capitalize()
    cantidad = validar_int("Ingrese cantidad")
    precio = validar_float("Ingrese precio unitario")
    categoria = validar_string("Ingrese la categoría del producto")

    if db_manager.registrar_producto(nombre, descripcion, cantidad, precio, categoria):
        imprimir_exito("Producto registrado exitosamente!")

# Menú: Consulta general de productos       
def menu_consultar_productos():
    imprimir_titulo("Consultar productos")
    productos = db_manager.consultar_productos()
    mostrar_productos(productos)

# Menú: Actualización de un producto por ID
# Usa pedir_actualizacion() para evitar repetir lógica
def menu_actualizar_producto():
    imprimir_titulo("Actualizar producto")
    id_producto = validar_int("Ingrese el ID del producto que quiera modificar")
    producto = db_manager.buscar_producto_id(id_producto)
    
    if not producto:
        imprimir_error("Producto no encontrado.")
        return
    
    print(f"Producto encontrado! Editando: {producto[1]}")
    print("Ingrese S/N si desea modificar el campo")
        
    nuevo_nombre = pedir_actualizacion("Nombre", producto[1], validar_string, "Ingrese el nuevo nombre")
    nueva_descripcion = pedir_actualizacion("Descripción", producto[2], validar_string, "Ingrese la nueva descripción")
    nueva_cantidad = pedir_actualizacion("Cantidad", producto[3], validar_int, "Ingrese nueva cantidad")
    nuevo_precio = pedir_actualizacion("Precio", producto[4], validar_float, "Ingrese nuevo precio")
    nueva_categoria = pedir_actualizacion("Categoría", producto[5], validar_string, "Ingrese nueva categoría")
       
    if db_manager.actualizar_producto_id(id_producto, nuevo_nombre, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_categoria):
        imprimir_exito("Producto actualizado con éxito!") 
    else:
        imprimir_error("No se puedo actualizar.")

# Menú: Eliminación de un producto
# Incluye confirmación antes de eliminar
def menu_eliminar_producto():
    imprimir_titulo("Eliminar producto")
    menu_consultar_productos()
    
    id_producto = validar_int("ID del producto a eliminar")
    
    confirmacion = input(f"¿Seguro desea eliminar el producto con ID {id_producto}? S/N: ").strip().lower()
    if confirmacion == "s":
        if db_manager.eliminar_producto_id(id_producto):
            imprimir_exito("Producto eliminado con éxito.")
        else:
            imprimir_error(f"No se encontró producto con ID {id_producto}.")

# Menú: Búsqueda de un producto por ID
def menu_buscar_producto():
    imprimir_titulo("Búsqueda de producto")
    
    id_producto = validar_int("Ingrese el ID del producto que desea buscar")
    producto = db_manager.buscar_producto_id(id_producto)
    if(producto):
        mostrar_productos([producto])
    else:
        imprimir_error("Opción inválida.")
 
# Menú: Reporte de productos con stock bajo
# len(productos) permite informar cuántos cumplen el criterio       
def menu_reporte():
    imprimir_titulo("Reporte de bajo stock")
    
    limite = validar_int("Ingrese el límite de cantidad para el reporte")
    productos = db_manager.reporte_bajo_stock(limite)
    if productos:
        imprimir_exito(f"Se encontraron {len(productos)} productos con stock <= {limite}")
        mostrar_productos(productos)
    else:
        imprimir_exito("Todos los productos superan ese límite de stock.")

# Punto de entrada principal del programa
# Muestra el menú y controla el flujo del sistema        
def main():
    db_manager.inicializar_db()
    
    while True:
        print("\n" + "="*30)
        print("   GESTIÓN DE INVENTARIO")
        print("="*30)
        print("1. Registrar producto")
        print("2. Consultar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte Bajo Stock")
        print("7. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            menu_registrar_producto()
        elif opcion == '2':
            menu_consultar_productos()
        elif opcion == '3':
            menu_actualizar_producto()
        elif opcion == '4':
            menu_eliminar_producto()
        elif opcion == '5':
            menu_buscar_producto()
        elif opcion == '6':
            menu_reporte()
        elif opcion == '7':
            print("Saliendo")
            sys.exit()
        else:
            imprimir_error("No se ha ingresado una opción válida. Intente nuevamente.")

if __name__ == "__main__":
    main()