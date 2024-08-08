import json
from os import system

with open("pan.json", encoding="utf-8") as archivo:
    info =json.load(archivo)

sel=0
while sel!=4:
    system("cls")
    print("------------------- BIENVENIDO AL MENÚ -------------------\n")
    print("""
    1. Ventas
    2. Compras
    3. Generación de informes
    4. Salir
    """)
    inicio=int(input("Digita el numero de lo primero que deseas hacer:\n"))

    if inicio==1:
        Ventas = int(input("\n"))
    input("Para continuar presione enter.")

    if inicio==2:
        Compras = int(input("\n"))
    input("Para continuar presione enter.")

    if inicio==3:
        Infromes = int(input("\n"))
    input("Para continuar presione enter.")

else:
    print("El programa se ha cerrado.")
    input("Presione enter para finalizar.")