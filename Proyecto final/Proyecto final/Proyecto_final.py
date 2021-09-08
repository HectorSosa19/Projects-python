import os
import sys
from string import Template
import matplotlib.pyplot as plt 
import urllib.request
from urllib.request import urlopen 
import json
import webbrowser
import requests
import marshal

upath = os.environ['USERPROFILE'] + '/Desktop/'
spath = 'C:/Proyecto_final'
lista = []

if not os.path.exists(spath):
    os.mkdir(spath)

if os.path.exists(spath + '/proyecto1.bin'):
    with open(spath + '/proyecto1.bin', 'rb') as f:
     lista = marshal.load(f)



def limpiar():
    os.system('cls')

class documento:
    cedula = ""
    nombre=""
    apellidos=""
    diadenacimiento=""
    sexo = ""
    nacionalidad=""
    estado=""
    telefono=""
    correo=""
    provincia=""
    lat=""
    lon=""
    zodiacosigno=""

def menu():
    
    limpiar()
    print("Bienvenido a mi lista de casos")
    print("1-Agregar un caso de COVID-19")
    print("2-Modificar un caso de COVID-19")
    print("3-Eliminar un caso de COVID-19")
    print("4-Exportar un caso de COVID-19 a HTML")
    print("5-Mostrar cantidad de casos de COVID-19")
    print("6-Exportar casos de COVID-19 en un mapa")
    print("7-Mandar una alerta a Telegram de los casos")
    print("8-Guardar casos de COVID-19")
    print("9-Estadistica Mistica")
    op=input("Ingrese una opcion de la lista:")
    if op=="1":
        agregar()
    elif op=="2":
        modificar()
    elif op=="3":
        eliminar()
    elif op=='4':
        exportarhtml()
    elif op =="5":
        mostrar()
        input("Pulse enter para volver")
        menu()
    elif op=="6":

        exportarmapa()
        input()
    elif op=="7":
        telegram()
    elif op=="8":
        guardar()
    elif op=="9":
        estadisticas()
        input()
        menu()
    else:
        print("Opcion no existente")
        menu()
def agregar():
    
    
    limpiar() 
    h=documento()

    
    h.cedula=input("Ingrese su cedula:")

    
    h.sexo=input("Ingrese su sexo[Masculino/Femenino]:")

    
    h.nacionalidad=input("Ingrese su nacionalidad:")

    
    h.estado=input("Ingrese su estado[Enfermo/Recuperado]:")
 
    
    h.telefono=input("Ingresa tu numero telefonico:")

    
    h.correo=input("Ingresa tu correo electronico:")

   
    h.provincia=input("Ingresa la provincia:")

    h.lat=input("Ingresa la latitud:")

    h.lon=input("Ingresa la longitud:")
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = "http://173.249.49.169:88/api/test/consulta/"+h.cedula
    headers={'User-Agent':user_agent,} 
    request = urllib.request.Request(url,None, headers)
    datos = urllib.request.urlopen(request)

    usuario = json.loads(datos.read())

    mes1 = usuario['FechaNacimiento'][5]
    mes2 = usuario['FechaNacimiento'][6]
    dia1 = usuario['FechaNacimiento'][8]
    dia2 = usuario['FechaNacimiento'][9]
    fecha1=usuario['FechaNacimiento'][0]
    fecha2=usuario['FechaNacimiento'][1]
    fecha3=usuario['FechaNacimiento'][2]
    fecha4=usuario['FechaNacimiento'][3]
                
    mes_nacimiento = mes1+ mes2
    día_nacimiento = dia1 + dia2
    fecha_nacimiento = fecha1 + fecha2 +fecha3+ fecha4  

    dia = int(día_nacimiento)
    mes = int(mes_nacimiento)
    fecha = int(fecha_nacimiento)

    signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
    fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

    mes=mes-1
    if dia>fechas[mes]:
        mes=mes+1
    if mes==12:
        mes=0

    h.nombre = usuario['Nombres']
    h.apellido = "Apellido: " + usuario['Apellido1'] + "  " + usuario['Apellido2']
    h.diadenacimiento = "Fecha de Nacimiento: " + str(dia) + "-" + str(mes_nacimiento) + "-" + str(fecha)
    h.zodiacosigno = signo[mes]
    lista.append(h)
   
 
    print("Datos Agregados")


    requests.post('https://api.telegram.org/bot983733661:AAGe5bkK7cMlvtiqsM_vAc40l4kx7F-U2qI/sendMessage',
    data={'chat_id': '-494424834', 'text': 'Se ha reportado un nuevo caso del COVID-19'})

    volver=input("Desea volver a ingresar datos[S/N]:")
    if volver.lower()=="s":
        agregar()
    elif volver.lower()=="n":
        menu()    
    else:
        input("Opcion no valida sera enviado al menu(Presione enter)")
        menu()
def mostrar():

   limpiar()
   for h in lista:
    print("Registro de COVID-19",lista.index(h) + 1)
    print("Cedula:",h.cedula)
    print("Nombre:",h.nombre)
    print("Apellido:",h.apellido)
    print("Dia de Nacimiento",h.diadenacimiento)
    print(h.zodiacosigno)
    print("Sexo:",h.sexo) 
    print("Nacionalidad:",h.nacionalidad)
    print("Estado:",h.estado)
    print("Telefono:",h.telefono)
    print("Correo:",h.correo)
    print("Provincia:",h.provincia)
    print("Latitud:",h.lat)
    print("Longitud",h.lon)
    
def modificar():
   

    mostrar()
    for h in lista:
        it=int(input("Ingrese el caso que quiere modificar:"))-1
        lista.remove(lista[it])
        agregar()
def eliminar():


    limpiar()
    mostrar()
    for h in lista:
        it=int(input("Ingrese el numero que desea eliminar:"))-1
        lista.remove(lista[it])
    menu()
def file_get_contents(filename):
    if os.path.exists(filename):
        fp=open(filename,"r")
        content=fp.read()
        fp.close()
        return content
def exportarmapa():
    

    base=file_get_contents("mapa.html") 
    final=[]
    for h in lista:
        tmp="""L.marker(["""+h.lat+""","""+h.lon+"""])
        .addTo(map)
        .bindPopup('"""+h.nombre+"""');"""
        final.append(tmp)
        webbrowser.open_new_tab('reporte.html')
        sep=""
        tmp=sep.join(final)
        base =base.replace("{MARCADORES}",tmp)
        f=open("reporte.html","w")
        f.write(base)
        f.close()
        print("Archivo exportado")
        menu()
def exportarhtml():
    

    limpiar()
    for h in lista:
        mostrar()
        caso=open("total.html",'w')
        mensaje="""
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <title>Reporte</title>
        <style>
         body {
            background: url(https://lh3.googleusercontent.com/proxy/8ZWMeJlbnB3HA03S4QGpffBJMEZiIIA38Zj7DcajchSLDgMuIBJJzzCGcqZTEQWnVgtXakPNp5vevtJvXuuzuN00Eue3bUo8mj476DxikNhrsBpCepJ0GBDH);
            background-size: 75%;
        }
        </style>
        </head>
        <body>
        </tr
        <td>""""Cedula:"+h.cedula+"""</td>
        <br/>
        <br/>
        <td>""""Nombre:"+h.nombre+"""</td>
        <br/>
        <br/>
        <td>"""+h.apellido+"""</td>
        <br/>
        <br/>
        <td>"""+h.diadenacimiento+"""</td>
        <br/>
        <br/>
        <td>""""Signo Zodiacal:"+h.zodiacosigno+"""</td>
        <br/>
        <br/>
        <td>""""Sexo:"+h.sexo+"""</td>
        <br/>
        <br/>
        <td>""""Nacionalidad:"+h.nacionalidad+"""</td>
        <br/>
        <br/>
        <td>""""Estado:"+h.estado+"""</td>
        <br/>
        <br/>
        <td>""""Telefono:"+h.telefono+"""</td>
        <br/>
        <br/>
        <td>""""Correo:"+h.correo+"""</td>
        <br/>
        <br/>
        <td>""""Provincia:"+h.provincia+"""</td>
        <br/>
        <br/>
        <td>""""Latitud:"+h.lat+"""</td>
        <br/>
        <br/>
        <td>""""Longitud:"+h.lon+"""</td>
        </body>
        </html>
        """
        caso.write(mensaje)
        caso.close()
        webbrowser.open_new_tab('total.html')

      
        menu()
def guardar():

    
    with open(spath + '/proyecto1.bin', 'wb') as f:
        marshal.dump(lista, f)  
    print("Datos Guardados")
    input()
    menu()
def telegram():

    mostrar()
    for h in lista:
        requests.post('https://api.telegram.org/bot983733661:AAGe5bkK7cMlvtiqsM_vAc40l4kx7F-U2qI/sendMessage',
        data={'chat_id': '-494424834', 'text': 'Se ha reportado un total de:'+(str(lista.count(h)+1))+"-casos registrado"})
        print("Se ha enviado el total de caso registrados a telegram")
        menu()
def estadisticas():
        for h in lista:
         aries=h.zodiacosigno.count('aries')
         tauro=h.zodiacosigno.count('tauro')
         geminis=h.zodiacosigno.count('geminis')
         cancer=h.zodiacosigno.count('cancer')
         leo=h.zodiacosigno.count('leo')
         virgo=h.zodiacosigno.count('virgo')
         libra=h.zodiacosigno.count('libra')
         escorpio=h.zodiacosigno.count('escorpio')
         sagitario=h.zodiacosigno.count('sagitario')
         capricornio=h.zodiacosigno.count('capricornio')
         acuario=h.zodiacosigno.count('acuario')
         piscis=h.zodiacosigno.count('piscis')
         fig=plt.figure()
         ax=fig.add_subplot(111)
         programas=['Aries', 'Tauro',' Géminis', 'Cáncer', 'Leo', 'Virgo', 'Libra', 'Escorpio', 'Sagitario', 'Capricornio', 'Acuario', 'Piscis']
         estadisticas=[aries, tauro, geminis, cancer, leo, virgo, libra, escorpio, sagitario, capricornio, acuario, piscis]
         grafica=range(1,len(estadisticas)+1)
         ax.bar(grafica,estadisticas,width=0.1,color="Blue")
         ax.set_xticks(grafica)
         ax.set_xticklabels(programas)
         ax.set_ylabel('Estadistica de casos')
         plt.show()
         input("Presiona enter para volver al menu")
         menu()
menu()







