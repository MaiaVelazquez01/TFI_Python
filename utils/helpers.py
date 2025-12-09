import os
from colorama import Fore, Back, Style, init
init(autoreset = True)

# Limpia la pantalla según el sistema operativo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Imprime un título destacado en pantalla    
def imprimir_titulo(txt):
    print(f"\n{Style.BRIGHT}---------- {txt.upper()} ----------{Style.RESET_ALL}")

# Muestra un mensaje de error con fondo rojo    
def imprimir_error(txt):
    print(f"{Back.RED} [Error] {txt}{Style.RESET_ALL}")
 
# Muestra un mensaje de éxito con fondo verde   
def imprimir_exito(txt):
    print(f"{Back.GREEN}{txt}{Style.RESET_ALL}")

# Valida que el usuario ingrese un string no vacío y solo con letras        
def validar_string(prompt):
    while True:
        dato = input(f"{prompt}: ").strip().capitalize()
        if not dato:
            imprimir_error("El campo no puede estar vacío.")
            continue
        if not dato.replace(" ", "").isalpha():
            imprimir_error("Campo con caracteres inválidos.")
            continue
        return dato

# Valida que el usuario ingrese un número decimal positivo
def validar_float(prompt):
    while True:
        try:
            dato = float(input(f"{prompt}: "))
            if dato >= 0:
                return dato
            imprimir_error("El número debe ser positivo.")
        except ValueError:
            imprimir_error("El campo debe ser un número válido.")

# Valida que el usuario ingrese un entero positivo            
def validar_int(prompt):
    while True:
        try:
            dato = int(input(f"{prompt}: "))
            if dato >= 0:
                return dato
            imprimir_error("El número debe ser positivo.")
        except ValueError:
            imprimir_error("El campo debe ser un número válido.")

# Pregunta si un campo debe actualizarse y aplica el validador si corresponde            
def pedir_actualizacion(nombre_campo, valor_actual, validador, mensaje):
    if(nombre_campo == "Precio"):
        print(f"{nombre_campo} actual: ${valor_actual:.2f}")
    else:
        print(f"{nombre_campo} actual: {valor_actual}")
    
    opcion = input("¿Desea modificarlo? (S/N): ").strip().lower()

    while opcion not in ("s", "n"):
        print("Opción inválida. Ingrese S o N.")
        opcion = input("¿Desea modificarlo? (S/N): ").strip().lower()

    if opcion == "s":
        return validador(mensaje)
    
    return valor_actual