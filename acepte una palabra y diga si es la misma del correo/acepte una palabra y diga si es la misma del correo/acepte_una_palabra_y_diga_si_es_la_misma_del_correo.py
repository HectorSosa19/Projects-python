#Hector Jose Sosa Castro ,Matricula:2019-7889
import re
 
correo= (input("Ingrese un correo electronico valido: "))
 
if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
	print ("Correo correcto")
else:
	print ("Correo incorrecto")