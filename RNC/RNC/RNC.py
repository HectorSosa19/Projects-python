from urllib.request import urlopen
import json
def programa():
   rnc=input("Introduzca el RNC:")
   url=" http://adamix.net/gastosrd/api.php?act=GetContribuyentes&rnc="+rnc
   datos=urlopen(url)
   leer=json.loads(datos.read())
   if "RGE_RUC" in leer:
    print("Su nombre es:",leer["RGE_RUC"])
    print("Su categoria es:",leer["CATEGORIA"])
    print("Su regimen de pago es:",leer["REGIMEN_PAGOS"])
    print("Su estatus es:",leer["ESTATUS"])
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
 

