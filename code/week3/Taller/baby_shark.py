shark_song = """Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!

Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!

Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!

Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!

Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!

Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt!

Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away!

Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last!

It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end!"""

shark_song = shark_song.replace("\n\n", " ")
shark_song = shark_song.replace("\n"," ")
shark_song = shark_song.replace(",", "")
shark_song = shark_song.replace("!", "")
print(shark_song.split(" "))
print('La cancion del baby shark tiene {} palabras.'.format(len(shark_song.split(" "))))
print('La palabra shark se repite {} veces y la palabra doo se repite {} veces.'.format(shark_song.count("shark"), shark_song.count("doo")))