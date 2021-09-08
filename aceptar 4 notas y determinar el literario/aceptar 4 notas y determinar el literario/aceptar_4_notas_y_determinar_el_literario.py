nota1=int(input("Introduce la primera nota:"))
nota2=int(input("Introduce la segunda nota:"))
nota3=int(input("Introduce la tercera nota:"))
nota4=int(input("Introduce la cuarta nota:"))
promedio=(nota1+nota2+nota3+nota4)/4
if promedio>=90:
    print("A")
elif promedio>=80 :
    print("B")
elif promedio>=70:
    print("C")
elif promedio<=69:
    print("F")
