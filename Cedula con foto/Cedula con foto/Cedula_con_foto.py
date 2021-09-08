import os 
import sys
from string import Template
from urllib.request import urlopen 
import json

print("identificador de cedula")
cedu= input("digite su cedula:")
url= "http://173.249.49.169:88/api/test/consulta/"+cedu
urlfoto=("http://173.249.49.169:88/api/test/foto/")+cedu
datos=urlopen(url).read()
persona=json.loads(datos)
archivo = open("Template/datoscedula.html")
src = Template(archivo.read())   
nombre=(persona["Nombres"])
apellido=(persona["Apellido1"])
fechan=(persona["FechaNacimiento"])
lugarn=(persona["LugarNacimiento"])
urlfoto="http://173.249.49.169:88/api/test/foto/"+cedu
abrir=urlfoto+cedu
d={'nombre':nombre, 'apellido':apellido, 'fechadenacimiento':fechan, 'lugardenacimiento':lugarn}          
result = src.substitute(d)

archivo2 = open('registro/'+str(nombre)+'.html','w')
archivo2.writelines(result)
print("su archivo fue guardado")

