#Hector Jose Sosa Castro ,Matricula:2019-7889
def leer_frase():
  global n
  n=(input("Introduzca una frase:"))
leer_frase()

def contar_letras():
    cont = 0
    for i in n :
        if(i.isalpha()):
            cont+=1
            print("Esta frase contiene ",cont,"Caracteres")
contar_letras()
            
