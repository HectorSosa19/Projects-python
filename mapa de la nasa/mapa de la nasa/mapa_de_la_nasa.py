import os 
import webbrowser
import marshal 
final=[] 
meteoritos=[]


def limpiar():
    os.system('cls')

def file_get_contents(filename):
    if os.path.exists(filename):
        fp=open(filename,"r")
        content=fp.read()
        fp.close()
        return content
class meteorito:
    nombre=""
    fecha=""
    tipo=""
    pais=""
    lat=""
    lon=""
    comentario=""
def modificar():
    if len(meteoritos) == 0:
        print('Sin registros...')
        return
    limpiar()
    mostrar()

    try:
        op = int(input('Elija el registro a modificar: ')) - 1
    except ValueError:
        print('Opcion no valida...')
        return

    if 0 <= op < len(meteoritos):
        mostrarRegistro(meteoritos[op])
    else:
        print('Fuera de los limites...')
        return

    des = True

    while des:
        opt = input('''
[ A ] Modificar un solo campo 
[ B ] Modificar todo el registro 
[ C ] Cancelar Modificacion
''').upper().strip()

        print()  # Espaciado

        if opt == 'A':

            des2 = True
            while des2:
                l = input(
                    'Escriba el campo que desee modificar: ').capitalize().strip()

                if not l in meteoritos[op]:
                    print('Registro no existente')
                    input()
                else:
                    meteoritos[op][l] = input(l + ': ')
                    des2 = False

            des = False

        elif opt == 'B':
            result = capturarMeteorito(meteoritos[op])
            if not result == 0:
                meteoritos[op] = result
                des = False
        elif opt == 'C':
            print('Modificacion cancelada...')
        else:
            print('Opcion no valida')
            input()
            limpiar()
            mostrarRegistro(meteoritos[op])

    print('Dato modificado...')


def borrar():
    if len(meteoritos) == 0:
        print('Sin registros...')
        return
    limpiar()
    mostrar()

    try:
        op = int(input('Elija el registro a modificar: ')) - 1
    except ValueError:
        print('Opcion no valida...')
        return

    if 0 <= op < len(meteoritos):
        mostrarRegistro(meteoritos[op])
    else:
        print('Fuera de los limites...')
        return

    des = True
    while des:
        limpiar()
        mostrarRegistro(meteoritos[op])

        opt = input(
            'Seguro que desea eliminar este registro [S/N]').upper().strip()

        if opt == 'S':
            meteoritos.pop(op)
            print('Reagistro eliminado...')
            des = False
        elif opt == 'N':
            print('Eliminacion cancelada...')
            des = False
        else:
            print('Elija una opcion valida')
            input()
def mostrar():
    for m in meteoritos:
     print("Registro",meteoritos.index(m) + 1)
     print("Nombre:",m.nombre)
     print("Fecha:",m.fecha)
     print("Tipo:",m.tipo)
     print("Pais:",m.pais)
     print("Latitud:",m.lat)
     print("Longitud:",m.lon)
     print("Comentario",m.comentario)
     print()
def mostrarRegistro(m):
    limpiar()
    print("Nombre:",m.nombre)
    print("Fecha:",m.fecha)
    print("Tipo:",m.tipo)
    print("Pais:",m.pais)
    print("Latitud:",m.lat)
    print("Longitud:",m.lon)
    print("Comentario",m.comentario)
    print()
def menu():
    print("1-Agregar Meteorito")
    print("2-Mostrar Meteorito")
    print("3-Vamos a modificar los meteoritos")
    print("4-Vamos a borrar los meteoritos")
    print("5-Exportar")
    print("6-Guardar pagina")
    op=input("Digite una opcion:")
    if op=="1":
        limpiar()
        m=capturarMeteorito()
        menu()
        
    if op=="2":
        limpiar()
        mostrar()
        menu()
    elif op=="3":
        modificar()
    elif op=="4":
        limpiar()
        eliminar()
    elif op=="5":
        limpiar()
        exportar()
        print("Archivo exportado")
        menu()
    elif op=="6":
       guardar()
def capturarMeteorito():
      print("Vamos a digitar los datos")
      m=meteorito()
      m.nombre=input("Digite el nombre:")
      m.fecha=input("Digite la fecha:")
      m.tipo=input("Digite el tipo:")
      m.pais=input("Digite el pais:")
      m.lat=input("Digite la latitud:")
      m.lon=input("Digite la longitud:")
      m.comentario=input("Digite un comentario:")
      meteoritos.append(m)
      print("Datos agregados")
   
def eliminar():
    if len(meteoritos) == 0:
        print("No hay registros")
        menu()
        return 
    limpiar
    mostrar()
        
    try:
        op = int(input("Elija el numero de registro que quiere modificar: ")) - 1
    except ValueError:
        print("Esta opcion no existe")
        menu()
        return
        

    if 0 <= op < len(meteoritos):
        mostrarRegistro(meteoritos[op])
    else:
        print("Imposible detectar")
        limpiar()
        menu()
        
        return
        
    des = True
    while des:
        limpiar()
        mostrarRegistro(meteoritos[op])

        opt = input("Seguro que quieres eliminar este registro[S/N]:").upper().strip()

        if opt == 'S':
            meteoritos.pop(op)
            print("Registro eliminado")
            des = False
            menu()
        elif opt == "N":
            print("Cancelando eliminacion")
            des = False
        else:
            print("Esta opcion no existe,elija otra")
            input()
def exportar():
    base=file_get_contents("mapa1.html") 
    final=[]
    for m in meteoritos:
        tmp="""L.marker(["""+m.lat+""","""+m.lon+"""])
        .addTo(map)
        .bindPopup('"""+m.nombre+"""');"""
        final.append(tmp)
        webbrowser.open_new_tab('reporte.html')
        sep=""
        tmp=sep.join(final)
        base =base.replace("{MARCADORES}",tmp)
        f=open("reporte.html","w")
        f.write(base)
        f.close()
def guardar():
        if not os.path.exists('C:/Datos/'):
            os.mkdir('C:/Datos/')

        if os.path.exists('C:/Datos/datos.bin'):
          with open('C:/Datos/datos.bin', 'rb') as f:
             meteoritos = marshal.load(f)
        else:
          meteoritos = list()
menu()
if input('Presione [S/s] para guardar cambios: ').lower().strip() == 's':
    with open('C:/Datos/datos.bin', 'wb') as f:
        marshal.dump(meteoritos, f)
        print('Guardado satisfactoriamente')
        input()