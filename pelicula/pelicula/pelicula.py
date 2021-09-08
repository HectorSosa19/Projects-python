import jinja2
import requests
import json

ruta=jinja2.Environment(jinja2.FileSystemLoader("Pelicula/platilla_pelicula"))
plantilla=ruta.get_template("Pelicula/platilla_pelicula")

pelicula=input("Elige una pelicula")

peticion=request.get("http://omdbapi.com/?i={pelicula.lower()}tt3896198&apikey=296057d")
contenidoJson=json.loads(peticion.text)

nombre=contenidoJson["Title"]
genero=contenidoJson["Genero"]
sipnosis=contenidoJson["Plot"]
genero=contenidoJson["Director"]
genero=contenidoJson["Actors"]
poster=contenidoJson["Poster"]

datos_peliculas={"Nombre":nombre,"Genero":genero,"Sipnosis":sipnosis,"Director":director,"Protagonista":protagonistas,"Poster":poster}

html=plantilla.render(datos_peliculas)
file=open({nombre}.html,"w")
file.write(html)


