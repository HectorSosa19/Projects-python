#Hector Jose Sosa Castro,Matricula:2019-7889
nc=int(input("Ingresa 5 numeros para verificar si son capicua: "))
n1=nc // 10000
n2=(nc // 1000) % 10
n3=(nc // 100) % 10
n4=(nc // 10 ) % 10
n5=( nc % 10 )
if n1==n5 and n2==n4 :
 print("Es capicua")
else:
  print("No es capicua")