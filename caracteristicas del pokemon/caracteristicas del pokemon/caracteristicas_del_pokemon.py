import requests
import json
while True:
    pokemon = input('escriba el nombre de su pokemon ')
    url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon
    response = requests.get(url)
    if response.status_code == 200:
        contenido = response.content
        resultado = json.loads(contenido)
        print('NOMBRE')
        print(' -', resultado.get('name'))
        print('PESO:')
        print(' -', resultado.get('height'))
        print('HABILIDADES:')
        for habilidad in resultado['abilities']:
            print(' -', habilidad['ability']['name'])
        print('TIPOS:')
        for valor in resultado['types']:
            print(' -', valor['type']['name'])
    else:
        print('ese no es el nombre de un Pokemon')
    duda = input('deseas datos de otro Pokemon? Si o No, escriba el numero de su respuesta ').lower()
    if duda == 'si':
        valor = True
    else:
         print('Gracias por su tiempo')
         break
