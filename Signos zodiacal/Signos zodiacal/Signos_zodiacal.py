dia=int(input("Ingresa el dia en que naciste:"))
mes=int(input("Introduce el mes que naciste en numero:"))

signos=["Capricornio","Acuario","Piscis","Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario"]
fecha=[20,19,20,20,21,21,22,22,22,22,22,21]

mes=mes-1
if dia>fecha[mes]:
 mes=mes+1
if mes==12:
 mes=0
print("Su signo zodiacal es:",signos[mes])

