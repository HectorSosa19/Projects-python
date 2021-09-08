#Hector Jose Sosa Castro Matricula:2019-7889
import marshal
import os
from datetime import datetime

def limpiar():
    os.system('cls')


def agregar():
    registro = dict()
    print('Registrar compra')
    registro['Nombre'] = input('Nombre de la persona: ').strip()
    registro['Apellido'] = input('Apellido de la persona: ').strip()
    registro['Fecha'] = str(datetime.now())
    registro['Cedula'] = input('Cedula de la persona: ').strip()
    registro['Telefono'] = input('Telefono de la persona: ').strip()
    registro['Articulo'] = input('Articulo de la persona: ').strip()
    registro['Valor'] = input('Valor de la persona: ').strip()
    registro['Dinero'] = input('Dinero entregado de la persona: ').strip()

    registros.append(registro)
    del (registro)
    print('Datos Agregados.')
    return


def mostrar():

    for registro in registros:
        print('Registro:', registros.index(registro) + 1)
        print(registro['Fecha'])
        print(registro['Nombre'], registro['Apellido'])
        print('Cedula:', registro['Cedula'], 'Telefono:', registro['Telefono'])
        print('Articulo:', registro['Articulo'], 'Valor:', registro['Valor'],
              'Dinero Entregado:', registro['Dinero'])
        


def Visualizar(registro):
    print('Nombre:', registro['Nombre'])
    print('Apellido:', registro['Apellido'])
    print('Fecha:', registro['Fecha'])
    print('Cedula:', registro['Cedula'])
    print('Telefono:', registro['Telefono'])
    print('Articulo:', registro['Articulo'])
    print('Valor:', registro['Valor'])
    print('Dinero Entregado:', registro['Dinero'])
   


def modificar():
    print("Modificar articulo de venta")
    mostrar()
    try:
        r = int(
            input('Escriba el numero de registro que desee modificar: ').strip()) - 1
    except:
        print("Error a modificar la lista de venta")

    if r > len(registros) - 1 or r < 0:
        print("No existe")
        return

    limpiar()
    cosa = True
    while (cosa):

        Visualizar(registros[r])
        l = input('Escriba el campo que desee modificar: ').capitalize().strip()

        if l == 'Fecha':
            print('No es muy recomendale modificar las fechas')
            if not input('Esta seguro que desea hacer? [S/s] ').lower() == 's':
                continue
        if l == 'Dinero entregado':
            l = 'Dinero'

        if not l in registros[r]:
            print('Registro no existente')
            return

        registros[r][l] = input('Digite el reemplazo: ')
        print('Dato modificado')

        if input('Desea seguir modifincado? [S/s]').lower().strip() == 's':
            limpiar()
        else:
            cosa = False


def eliminar():
    
    print('Eliminar registro')
    mostrar()
    try:
        r = int(
            input('Escriba el numero de registro que desee modificar: ').strip()) - 1
    except:
        print('Ha ocurrido un error')

    if r > len(registros) - 1 or r < 0:
        print('Registro no existe')
        return

    registros.pop(r)
    print('Registro eliminado')


def menu():
    limpiar()
    
    print('''
Bienvenido a mi lista de compra y venta. 
1- Registrar en la lista de venta
2- Editar la lista de venta
3- Eliminar una lista de venta
X- Salir
    ''')
    r = input("Elige una opcion:")

    if r == '1':
        limpiar()
        agregar()
        input()
        limpiar()
        menu()
    elif r == '2':
        limpiar()
        modificar()
        input()
        limpiar()
        menu()
    elif r == '3':
        limpiar()
        eliminar()
        input()
        limpiar()
        menu()
    elif r == "x":
        pass
    else:
        print('Opcion no existente elija otra')
        input()
        limpiar()
        menu()


if not os.path.exists('C:/Datos/'):
    os.mkdir('C:/Datos/')

if os.path.exists('C:/Datos/datos.bin'):
    with open('C:/Datos/datos.bin', 'rb') as f:
        registros = marshal.load(f)
else:
    registros = list()

menu()

if input('Presione [S/s] para guardar cambios: ').lower().strip() == 's':
    with open('C:/Datos/datos.bin', 'wb') as f:
        marshal.dump(registros, f)
        print('Guardado satisfactoriamente')
        input()