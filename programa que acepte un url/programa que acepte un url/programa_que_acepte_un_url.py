import re 
from urllib.request import urlopen

def imagenes(url):

 total_img=0
 pagina = urlopen(url).readlines()

 for codigo in pagina:

  lector = re.findall('<img.*?>',srt(codigo))
  total_img+=len(lector)

 print('{0}total de imagenes:{1}'.format(url,total_img))

imagenes(input("Ingresa tu pagina:"))