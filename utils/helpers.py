import os
from colorama import Fore, Back, Style, init
init(autoreset = True)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else clear)
    
def imprimir_titulo(txt):
    print(f"\n{Style.BRIGHT}---------- {txt.upper()} ----------{Style.RESET_ALL}")
    
def imprimir_error(txt):
    print(f"{Back.RED} Error: {txt}{Style.RESET_ALL}")
    
def imprimir_exito(txt):
    print(f"{Back.GREEN}{txt}{Style.RESET_ALL}")
        
def validar_string(prompt):
    while True:
        dato = input(f"{prompt}: ").strip()
        if dato:
            return dato
        imprimir_error("El campo no puede estar vacío.")

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
            