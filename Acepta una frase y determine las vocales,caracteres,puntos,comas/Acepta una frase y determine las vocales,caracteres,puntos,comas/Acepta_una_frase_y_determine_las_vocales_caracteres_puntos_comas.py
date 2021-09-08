vowels=['a','e','i','o','u']
fs=(input("Escribe alguna frase:"))
print('Cantidad de caracteres:',len(fs))
vocalcounter=0
numeroscounter=0
dotscounter=fs.count('.')
colonscounter=fs.count(',')

for letra in fs :
    for vocal in vowels:
        if vocal==letra:
            vocalcounter+=1
print(f'Cantidad de vocales:{vocalcounter}')
print(f'Cantidad de puntos:{dotscounter}')
print(f'Cantidad de comas:{colonscounter}')

for letra in fs:
    for number in range (0,10):
        if str(number)==letra:
            numeroscounter+=1
print(f'Cantidad de numeros:{numeroscounter}')
