num = int(input("Digite un numero: "))

if ((2** (num - 1)) % num) == 1 or num == 2:
 print("Es primo")
else:
 print("No es primo")