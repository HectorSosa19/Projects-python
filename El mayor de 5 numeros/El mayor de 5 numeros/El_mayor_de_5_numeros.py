n1=int(input("Ingresa el primer numero:"))
n2=int(input("Ingresa el segundo numero:"))
n3=int(input("Ingresa el tercer numero:"))
n4=int(input("Ingresa el cuarto numero:"))
n5=int(input("Ingresa el quinto numero:"))

if n2<n1>n3>n4>n5:
    print("El primer numero",n1,"es el mayor")
elif n1<n2>n3>n4>n5:
    print("El segundo numero",n2,"es el mayor")
elif n1<n3>n2>n4>n5:
    print("El tercer numero",n3,"es el mayor")
elif n1<n4>n2>n3>n5:
    print("El cuarto numero",n4,"es el mayor")
elif n1<n5>n2>n3>n4:
    print("El quinto numero",n5,"es el mayor")