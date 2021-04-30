import re

#findall

string="""Su luna de miel fue un largo escalofrío. Rubia, angelical y tímida, el carácter duro de su marido heló sus soñadas niñerías de novia. Lo quería mucho, sin embargo, a veces con un ligero estremecimiento cuando volviendo de noche juntos por la calle, echaba una furtiva mirada a la alta estatura de Jordán, mudo desde hacía una hora. Él, por su parte, la amaba profundamente, sin darlo a conocer.
         Durante tres meses —se habían casado en abril— vivieron una dicha especial. Sin duda hubiera ella deseado menos severidad en ese rígido cielo de amor, más expansiva e incauta ternura; pero el impasible semblante de su marido la contenía siempre.
         La casa en que vivían influía un poco en sus estremecimientos. La blancura del patio silencioso —frisos, columnas y estatuas de mármol— producía una otoñal impresión de palacio encantado. Dentro, el brillo glacial del estuco, sin el más leve rasguño en las altas paredes, afirmaba aquella sensación de desapacible frío. Al cruzar de una pieza a otra, los pasos hallaban eco en toda la casa, como si un largo abandono hubiera sensibilizado su resonancia."""

pattern="[a-zA-Z]*ado"

res=re.findall(pattern,string)

for match in res:
    print(match)

print(len(res))

#Split

text="La mejor academia de codigo es MagicKode"

lista=re.split("[Aa]cademia", text)
print(lista)

#Replace

text_2=input("Ingresa ti mensaje: ")

pattern_2="[Ff][Uu]*[Cc][Kk]"
res=re.sub(pattern_2,"F**k" ,text_2 )

print(res)
