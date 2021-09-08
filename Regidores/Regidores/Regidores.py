import os
import urllib.request
from urllib.request import urlopen
import json
import webbrowser
lista = []

class clsinformaciones:
    cedula = ""
    Partido = ""
    nombre = ""
    dia_nacimiento = ""
    apellidos = ""
    zodiacosigno = ""

def limpiar():
    os.system('cls')

def menu():
    limpiar()
    
    print("Bienvenido a mi lista")
    print("1.- Agregar Candidato.")
    print("2.- Listado de Candidatos.")
    print("3.- Eliminar Candidato.")
    print("4.- Exportar Padron.")
    print("5.- salir.")
    opcion = int(input("Digite la opcion: "))
    if opcion == 1:
        limpiar()
        print("Agregar candidatos")
        contacto = clsinformaciones
        contacto.cedula = input("Ingrese la cedula del candidato: ")
        contacto.Partido = input("Ingresa el nombre del partido politico al que pertenece: ")
        lista.append(contacto)
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        url = "http://173.249.49.169:88/api/test/consulta/"+contacto.cedula
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

        contacto.nombre = usuario['Nombres']
        contacto.apellidos = "Apellido: " + usuario['Apellido1'] + "  " + usuario['Apellido2']
        contacto.dia_nacimiento = "Fecha de Nacimiento: " + str(dia) + "-" + str(mes_nacimiento) + "-" + str(fecha)
        contacto.zodiacosigno = "Tu signo es: " + signo[mes]
    
        menu() 

    elif opcion == 2:
        limpiar()
        print("Listado de candidatos")
        for contacto in lista:
            print(contacto.cedula)
            print(contacto.nombre)
            print(contacto.apellidos)
            print(contacto.Partido)
            print(contacto.zodiacosigno)
        input()    
        menu()
    elif opcion == 3:
        print("Selecione el candidato a eliminar")
        x = 0
        for contacto in lista:
            print(str(x)+" -> "+contacto.nombre)
            x =x+1
        con = int(input('Digite el numero de candidato que desea eliminar: '))
        lista.remove(lista[con])
        menu()
    elif opcion == 4:
        print("Se mostrara sus datos en una pagina")
        carpeta = "c:\\carpeta"
        if os.path.exists(carpeta) == False:
            os.mkdir(carpeta)
        f = open(carpeta+'\\'+'pagina.html','wb')
        mensaje = """<html>
        
        <head><meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>AJAX</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet"  href="http://173.249.49.169:88/api/test/consulta/"+contacto.cedula>
        </head>
        <body><p>Padron Electoral</p>
                <div class="container">
                <div class="section">
                    <button class="btn" id="boton">
                        JSON
                    </button>

                    <table>
                        <thead>
                            <tr>
                                <th>cedula</th>
                                <th>nombre</th>
                                <th>apellidos</th>
                                <th>Partido</th>
                                <th>zodiacosigno</th>
                                
                            </tr>
                            
                        </thead>

                        <tbody id="response">

                        </tbody>
                    </table>
                </div>
            </div>

            <div class="section" id="respuesta"></div>

            <script src="AJAX.js"></script>
        </body>
        </html>"""
        
        print("Cargando")
        f.close()

  

    elif opcion == 5:
        print("Gracias por entrar a mi lista")
    else:
        print("La opcion que ha elegido no es valida")
        input()
        menu()           


menu()