my_dictionary = {
    "key" : "value",
    "uno" : 1,
    "hola" : "hello",
    "mundo" : "world"
}

print(my_dictionary.get("uno"))

my_dictionary["nueva_llave"] = "nuevo valor"

print(my_dictionary)

for i in my_dictionary:
    print(i, my_dictionary[i])

for key, value in my_dictionary.items():
    print(key, value)