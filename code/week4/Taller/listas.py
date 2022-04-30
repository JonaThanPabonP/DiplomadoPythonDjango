lista = [1, 3, 11, 12, 44, 8, 9, 10, 23, 9, 0, 213, 99, 98]

print(f"La lista tiene {len(lista)} valores.")

par = 0
for num in lista:
    if num%2 == 0 and num!=0:
        par += 1
print(f"La lista tiene {par} números pares")

mult3 = 0
for num in lista:
    if num%3 == 0 and num!=0:
        mult3 += 1
print(f"La lista tiene {mult3} números múltiplos de 3.")

lis_asc = sorted(lista)
print(f"La lista ordenada de forma ascendente tiene ubicado el valor {lis_asc[5]} en posición 5.")

lis_des = sorted(lista, reverse=True)
print(f"La lista ordenada de forma descendente tiene ubicado el valor {lis_des[5]} en posición 5.")

sub = []
for num in lista:
    if num in range(3,50):
        sub.append(num)
print(f"Los valores en el rango de 3 a 50 son {sub}")
