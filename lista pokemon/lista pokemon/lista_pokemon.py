import os 
import pickle
from pathlib import Path 
import pickle
import webbrowser


pokemones=[]

if os.path.getsize("pokemon2.bin") > 0:      
    with open("pokemon2.txt", "rb") as fp:
        unpickler = pickle.Unpickler(fp)
        pokemones = unpickler.load()
    with open("pokemon2.txt", "rb") as fp:   
        b = pickle.load(pokemones)

def limpiar():
    os.system('cls')

class listado():
    nombre=""
    color=""
    fechanacimiento=""
    tipo=""
    ataque=""

def menu():
    limpiar()
    
    print("Bienvenido a mi lista pokemon")
    print("1-Agregar pokemon")
    print("2-Editar pokemon")
    print("3-Eliminar pokemon")
    print("4-Exportar pokemon")
    print("5-Guardar")
    print("6-Mostrar lista")
    op=input("Ingrese una opcion:")
    if op=='1':
        agregar()
        input()
        menu()
    elif op=='2':
        modificar()
        input()
        menu()
    elif op =='3':
        eliminar()
        input()
    elif op=='4':
        exportar()
        input()
        menu()
    elif op=='5':
        guardar()
    elif op == '6':
        limpiar()
        mostrar()
        input("Pulsa Enter para continuar")
        menu()
    
    else:
        print("Debe seleccionar una opcion")
def agregar():
    limpiar()
    p=listado()
    
    p.nombre=input("Ingresa el nombre del pokemon:")
    p.color=input("Ingrese el color del pokemon:")
    p.fechanacimiento=input("Ingrese la fecha de nacimiento:")
    p.tipo=input("Ingresa el tipo del pokemon:")
    p.ataque=input("Ingresa el ataque del pokemon:")
    pokemones.append(p)
    print("Datos Agregados")

def mostrar():
   
   for p in pokemones:
    print("Lista pokemon",pokemones.index(p) + 1)
    print("Nombre:",p.nombre)
    print("Color:",p.color)
    print("Fecha de Nacimiento:",p.fechanacimiento)
    print("Tipo:",p.tipo)
    print("Ataque:",p.ataque)

def modificar():
    
    mostrar()
    for p in pokemones:
        it=int(input("Ingrese el numero de lista que quiere modificar:"))-1
        pokemones.remove(pokemones[it])
        agregar()
        menu()
    
def eliminar():
    
    limpiar()
    mostrar()
    for p in pokemones:
        it=int(input("Ingrese el numero que desea eliminar:"))-1
        pokemones.remove(pokemones[it])
    menu()
def guardar():
    with open("pokemon2.txt", "wb") as fp: 
        pickle.dump(pokemones, fp)   
    print("Datos Guardados")

    input()
    menu()
def exportar():
    
    mostrar()
    for p in pokemones:
        it=int(input("Ingrese el numero que desea exportar:"))-1
        pokemones.append(pokemones[it])
        datos=pickle.dumps(pokemones)
        h=open("pokemon2.html","wb")
        h.write(datos)
        h.close()
        webbrowser.open_new_tab('pokemon2.html')
        print("Pokemon exportado")
        menu()
menu()