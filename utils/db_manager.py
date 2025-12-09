import sqlite3
from utils.helpers import imprimir_error
from config import BD_NAME, TABLE_NAME

# Abre una conexión a la base de datos definida en BD_NAME
def conectar_db():
    return sqlite3.connect(BD_NAME)

# Crea la tabla si no existe. Se asegura que siempre se tenga una estructura mínima
def inicializar_db():
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute(f'''
                       CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT NOT NULL,
                            descripcion TEXT,
                            cantidad INTEGER NOT NULL,
                            precio REAL NOT NULL,
                            categoria TEXT
                       )
                       ''')
        conexion.commit()

    except sqlite3.Error as e:
        imprimir_error(f"Error al iniciar la base de datos. {e}")
        
    finally:
        conexion.close()

# Inserta un nuevo producto en la tabla        
def registrar_producto(nombre, descripcion, cantidad, precio, categoria):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute(f'''
                       INSERT INTO {TABLE_NAME} (nombre, descripcion, cantidad, precio, categoria)
                       VALUES (?, ?, ?, ?, ?)''', (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        return True
    
    except sqlite3.Error as e:
        imprimir_error(f"Error al registrar producto. {e}")
        return False
    
    finally:
        conexion.close()

# Devuelve todos los productos almacenados
def consultar_productos():
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        productos = cursor.fetchall()
        return productos
       
    except sqlite3.Error as e:
        imprimir_error(f"La base de datos no existe o la tabla '{TABLE_NAME}' aún no fue creada. {e}")
        return []
    
    finally:
        conexion.close()

# Actualiza un producto por su ID y devuelve True si se modificó alguna fila
def actualizar_producto_id(id_producto, nombre, descripcion, cantidad, precio, categoria):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute(f"UPDATE {TABLE_NAME} SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ? WHERE id = ?", 
                       (nombre, descripcion, cantidad, precio, categoria, id_producto))
        if cursor.rowcount > 0:
            conexion.commit()
            return True
        return False
        
    except sqlite3.Error as e:
        imprimir_error(f"Error al actualizar. {e}")
        return False
    
    finally:
        conexion.close()

# Elimina un producto por ID y devuelve True si realmente se borró    
def eliminar_producto_id(id_producto):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = ?", (id_producto,))
        if cursor.rowcount > 0:
            conexion.commit()
            return True
        return False
    
    except sqlite3.Error as e:
        imprimir_error(f"Error al eliminar. {e}")
        return False
        
    finally:
        conexion.close()

# Busca y devuelve un solo producto. Retorna None si no existe
def buscar_producto_id(id_producto):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()
        return producto
        
    except sqlite3.Error as e:
        imprimir_error(f"Error al buscar. {e}")
        return None
    
    finally:
        conexion.close()

# Devuelve los productos cuya cantidad es menor o igual al límite indicado
def reporte_bajo_stock(limite):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE cantidad <= ?", (limite,))
        productos_bajo_stock = cursor.fetchall()
        return productos_bajo_stock
        
    except sqlite3.Error as e:
        imprimir_error(f"Error al realizar reporte. {e}")
        return []
    
    finally:
        conexion.close()