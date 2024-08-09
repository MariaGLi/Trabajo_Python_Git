import json
from os import system
import datetime


with open("informes.json", encoding="utf-8") as archivo:
    info=json.load(archivo)

with open("venta.json", encoding="utf-8") as pventa:
    venta=json.load(pventa)

with open("compra.json", encoding="utf-8") as pcompra:
    compra=json.load(pcompra)

sel=0
bool1=True
while sel!= 4:
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
        nempleado=input(str("Ingrese el nombre del empleado."))
        booleano=True
        while booleano==True:
            system("cls")
            print("==========================\n1).Panadería\n2).Pasteleria\n3).Bebidas\n4).Promociones\n5).Salir\n==========================")
            inicio2=int(input("Seleccione la opción deseada."))
            if inicio2==1:
                system ("cls")
                print("----------Panadería----------")
                for i in info["Panaderia"]:
                    print(i, "Precio:",info["Panaderia"][i])

                comp=input(str("Ingrese el nombre del pan que desea llevar: "))
                cont=0
                for g in info["Panaderia"]:
                    cont=cont+1
                    if comp == g:
                        cant=int(input("¿Cuánto pan vas a comprar? "))
                        prepan=cant*info["Panaderia"][g]
                        nombre=str(input("Nombre del comprador: "))
                        direc=str(input("Direccion del comprador: "))
                        fecha=str(datetime.datetime.now())

                        venta[0]["Personas"].append({
                            "Fecha":fecha,
                            "Nombre":nombre,
                            "Direccion":direc,
                            "Empleado":nempleado,
                            "Producto":[
                                {
                                    "NombreP":g,
                                    "Cantidad":cant,
                                    "PrecioP":prepan
                                }
                            ]
                        })
                        with open("venta.json", "w") as file:
                            json.dump(venta,file)
                        
                        input("Producto añadido al carrito, presione Enter para continuar")
                    
                    elif cont < 11:
                        system("cls")

                    else:
                        print("Producto no existente, procura escribir el nombre del producto correctamente")
                        input("Presiona Enter para continuar")
                
            elif inicio2==2:
                system("cls")
                print("----------Pasteleria----------")
                for i in info["Pasteleria"]:
                    print(i, "Precio:",info["Pasteleria"][i])

                comp=input(str("Ingrese el nombre del ponque que desea llevar: "))
                cont=0
                for g in info["Pasteleria"]:
                    cont=cont+1
                    if comp == g:
                        cant=int(input("¿Cuántos ponques desea comprar? "))
                        prepan=cant*info["Pasteleria"][g]
                        nombre=str(input("Nombre del comprador: "))
                        direc=str(input("Direccion del comprador: "))
                        fecha=str(datetime.datetime.now())

                        venta[0]["Personas"].append({
                            "Fecha":fecha,
                            "Nombre":nombre,
                            "Direccion":direc,
                            "Empleado":nempleado,
                            "Producto":[
                                {
                                    "NombreP":g,
                                    "Cantidad":cant,
                                    "PrecioP":prepan
                                }
                            ]
                        })
                        with open("venta.json", "w") as file:
                            json.dump(venta,file)
                        input("Producto añadido al carrito, presione Enter para continuar")
                    
                    elif cont < 11:
                        system("cls")

                    else:
                        print("Producto no existente, procura escribir el nombre del producto correctamente")
                        input("Presiona Enter para continuar")
            
            elif inicio2==3:
                system("cls")
                print("----------Bebidas----------")
                for i in info["Bebidas"]:
                    print(i, "Precio:",info["Bebidas"][i])

                comp=input(str("Ingrese el nombre de la bebida que desea llevar: "))
                cont=0
                for g in info["Bebidas"]:
                    cont=cont+1
                    if comp == g:
                        cant=int(input("¿Cuántos ponques desea comprar? "))
                        prepan=cant*info["Bebidas"][g]
                        nombre=str(input("Nombre del comprador: "))
                        direc=str(input("Direccion del comprador: "))
                        fecha=str(datetime.datetime.now())

                        venta[0]["Personas"].append({
                            "Fecha":fecha,
                            "Nombre":nombre,
                            "Direccion":direc,
                            "Empleado":nempleado,
                            "Producto":[
                                {
                                    "NombreP":g,
                                    "Cantidad":cant,
                                    "PrecioP":prepan
                                }
                            ]
                        })
                        with open("venta.json", "w") as file:
                            json.dump(venta,file)
                        input("Producto añadido al carrito, presione Enter para continuar")
                    
                    elif cont < 11:
                        system("cls")

                    else:
                        print("Producto no existente, procura escribir el nombre del producto correctamente")
                        input("Presiona Enter para continuar")
            
            elif inicio2==4:
                system("cls")
                print("----------Apartado de Promociones----------")
                for i in info["Apartado de promociones"]:
                    print(i, "Precio:",info["Apartado de promociones"][i])

                comp=input(str("Ingrese el nombre del Apartado de Promociones: "))
                cont=0
                for g in info["Apartado de promociones"]:
                    cont=cont+1
                    if comp == g:
                        cant=int(input("¿Cuántos Apartado de Promociones desea llevar? "))
                        prepan=cant*info["Apartado de promociones"][g]
                        nombre=str(input("Nombre del comprador: "))
                        direc=str(input("Direccion del comprador: "))
                        fecha=str(datetime.datetime.now())

                        venta[0]["Personas"].append({
                            "Fecha":fecha,
                            "Nombre":nombre,
                            "Direccion":direc,
                            "Empleado":nempleado,
                            "Producto":[
                                {
                                    "NombreP":g,
                                    "Cantidad":cant,
                                    "PrecioP":prepan
                                }
                            ]
                        })
                        with open("venta.json", "w") as file:
                            json.dump(venta,file)
                        input("Producto añadido al carrito, presione Enter para continuar")
                    
                    elif cont < 11:
                        system("cls")

                    else:
                        print("Producto no existente, procura escribir el nombre del producto correctamente")
                        input("Presiona Enter para continuar")
            
            elif inicio2==5:
                system("cls")
                print("------Saliendo------")
                input("Presione Enter para continuar")
                booleano=False

    if inicio==2:
        booleano=True
        while booleano==True:
            system("cls")
            print("1).Comprar\n2).Salir")
            inicio3=input(str("Ingrese un numero para ir a la opcion deseada: "))
            if inicio3=="1":
                nprov=str(input("Nombre del proovedor al que se le comprara: "))
                numprov=int(input("Numero del proovedor al que desea comprar: "))
                nproduc=str(input("Que producto desea comprar: "))
                cantprod=int(input("Cantidad del producto que desea comprar: "))
                pproduc=int(input("Precio del producto que desea comprar: "))
                total=pproduc*cantprod
                Fecha=str(datetime.datetime.now())

                compra[0]["Personas"].append(
                    {
                        "Fecha": Fecha,
                        "Nombre":nprov,
                        "Numero":numprov,
                        "Producto":nproduc,
                        "Cantidad":cantprod,
                        "Precio Unitario":pproduc,
                        "Precio Total":total
                    }
                )
                with open("compra.json", "w") as comp:
                    json.dump(compra,comp)

            elif inicio3==2:
                system("cls")
                print("Saliendo...")
                input("Presione Enter para continuar")
                booleano=False

    if inicio==3:
        bool=True
        while bool==True:
            system("cls")
            print("1).Registros ventas\n 2).Registros Compras\n 3).Salir")         
            inicio4=input(str("Ingrese un numero para ir a la opcion deseada: "))

            if inicio4==1:
                system("cls")
                for i in venta[0]["Personas"]:
                    print("----------Ventas----------")
                    print("Fecha de compra: ",i["Fecha"],"\nDireccion: ",i["Nombre"],"\nEmpleado: ",i["Empleado"],"\nProducto: ",i["Producto"][0]["NombreP"],"\nCantidad: ",i["Producto"][0]["Cantidad"],"\nPrecio Venta : ",i["Producto"][0]["PrecioP"])
                    print("---------------------------------------------")

                input("Presione Enter para continuar")    

            elif inicio4==2:
                system("cls")
                for i in compra[0]["Personas"]:
                    print("------------------------Compras------------------------")
                    print("Fecha de compra: ",i["Fecha"],"\nNombre del proovedor: ",i["Nombre"],"\nProducto: ",i["Producto"],"\nCantidad: ",i["Cantidad"],"\nPrecio Total: ",i["Precio Total"])
                    print("---------------------------------------------")

                input("Presione Enter para continuar")

            elif inicio4==3:
                system("cls")
                print("======Saliendo======")
                input("Presione Enter para continuar")

    else:
        print("El programa se ha cerrado.")
        input("Presione enter para finalizar.")
    bool1=False