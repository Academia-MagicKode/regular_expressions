import re

texto="El canal de Magickode es Genial!"

pattern="[Mm]agic[Kk]ode"

print("buscando el patron ",pattern, " en el texto : ",texto)

if re.search(pattern,texto):
    print("Match Encontrado")
else:
    print("Match NO encontrado")

#Match objects

match=re.search(pattern,texto)

print(match.re)
print(match.string)
print(match.group())

texto_2="El precio de nuestra suscripcion es de solo  15usd mensuales "
pattern2=r"\d"

if re.search(pattern2,texto_2):
    print("contiene numeros")
else:
    print("No contien numros")

print("---------ARTISTAS------------------------------")

artistas=r"The Beatles|Aerosmith|Queen"
request="Play Aerosmith"

if re.search(artistas,request):
    print("Buena Eleccion")
else:
    print("Debes revisar tus gustos musicales!")