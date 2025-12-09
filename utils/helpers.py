import os
from colorama import Fore, Back, Style, init
init(autoreset = True)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else clear)
    
def imprimir_titulo(txt):
    print(f"\n{Style.BRIGHT}---------- {txt.upper()} ----------{Style.RESET_ALL}")
    
def imprimir_error(txt):
    print(f"{Back.RED} [Error] {txt}{Style.RESET_ALL}")
    
def imprimir_exito(txt):
    print(f"{Back.GREEN}{txt}{Style.RESET_ALL}")
        
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

def validar_float(prompt):
    while True:
        try:
            dato = float(input(f"{prompt}: "))
            if dato >= 0:
                return dato
            imprimir_error("El número debe ser positivo.")
        except ValueError:
            imprimir_error("El campo debe ser un número válido.")
            
def validar_int(prompt):
    while True:
        try:
            dato = int(input(f"{prompt}: "))
            if dato >= 0:
                return dato
            imprimir_error("El número debe ser positivo.")
        except ValueError:
            imprimir_error("El campo debe ser un número válido.")
            
def pedir_actualizacion(nombre_campo, valor_actual, validador, mensaje):
    if(nombre_campo == "Precio"):
        print(f"{nombre_campo} actual: ${valor_actual:.2f}")
    print(f"{nombre_campo} actual: {valor_actual}")
    
    opcion = input("¿Desea modificarlo? (S/N): ").strip().lower()

    while opcion not in ("s", "n"):
        print("Opción inválida. Ingrese S o N.")
        opcion = input("¿Desea modificarlo? (S/N): ").strip().lower()

    if opcion == "s":
        return validador(mensaje)
    
    return valor_actual