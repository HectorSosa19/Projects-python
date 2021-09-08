from urllib.request import urlopen
import json
global tpm
def programa():
    
   signos=["Capricornio","Acuario","Piscis","Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario"]
   fecha=[20,19,20,20,21,21,22,22,22,22,22,21]
   cedula=input("Digite su Cedula Dominicana:")
   url="http://173.249.49.169:88/api/test/consulta/"+cedula
   datos=urlopen(url)
   persona = json.loads(datos.read())
   if "Nombres" in persona:
    print("El Nombre es:",persona["Nombres"])
    print("El Apellido es:",persona["Apellido1"],persona["Apellido2"])
    print("La fecha de nacimiento es:",persona["FechaNacimiento"]) 
    mes1=persona["FechaNacimiento"]
    mes2=persona["FechaNacimiento"]
    dia1=persona["FechaNacimiento"]
    dia2=persona["FechaNacimiento"]

   dia=int(input("Ingresa el dia en que naciste:"))
   mes=int(input("Ingresa el mes que naciste en numero :"))

   signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
   fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

   mes=mes-1
   if dia>fechas[mes]:
    mes=mes+1
   if mes==12:
    mes=0
   print ("Tu signo es: " + signo[mes])
   continuar()
    

def continuar():
    tmp = input("Desea continuar con otro s o n:") 
    if tmp=="s":
      programa()
    elif tmp=="n":
         return False
    else:
     print("Favor de elegir S o N en minuscula")
     continuar()
programa()
 