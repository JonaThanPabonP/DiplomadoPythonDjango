

song = '''Te voy a enseñar 
Que debes bailar 
Como baila el sapito 
Dando brinquitos 

Tú debes buscar 
Con quién brincarás 
Y aunque tú estés solito 
Tu debes brincar 

Para abajo, para abajo 
Giras y giras siempre para abajo 

Más abajo, más abajo 
Si ya estás listo podemos comenzar 

Vas para adelante 
Más un poco más 
Vas para adelante 
Y luego vas pa’tras 
Ahora para un lado 
Para el otro ya 
Das un brinco alto 
Y vuelves a empezar'''

song = song.replace("\n\n", " ")
song = song.replace("\n", " ")
song = song.replace(",", "")
song = song.replace("!", "")
song = song.replace(".", "")

print('La cancion tiene {} palabras.'.format(len(song.split(" "))))