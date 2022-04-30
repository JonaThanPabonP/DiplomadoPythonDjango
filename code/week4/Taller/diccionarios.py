dictionary_example = {
	"gods": "dioses",
	"thank": "gracias",
	"I": "yo",
	"for": "por",
	"my": "mi",
	"soul": "alma",
	"am": "soy",
	"the": "el",
	"owner": "dueño",
	"of": "de",
	"my": "mi",
	"destiny": "destino",
	"captain": "capitan",
	"love": "amor",
	"is": "es",
	"more": "más",
	"powerful": "poderoso",
	"than": "que",
	"fear": "miedo",
	"beautiful": "hermoso",
	"better": "mejor",
	"ugly": "feo",
	"simple": "simple",
	"complex": "complejo",
	"complicated": "complicado",
}

# frase_eng = "I thank gods for my soul"
# frase_eng = "I am the owner of my destiny I am the captain of my soul"
# frase_eng = "love is more powerful than fear"
# frase_eng = "beautiful is better than ugly"
frase_eng = "Simple is better than complex Complex is better than complicated"
frase_splited = frase_eng.split(" ")
frase_esp = []
frase = ""

for word in frase_splited:
    if word.lower() in dictionary_example:
        frase_esp.append(dictionary_example[word.lower()])
    
for i in frase_esp:
	frase = " ".join(frase_esp)

print(frase)