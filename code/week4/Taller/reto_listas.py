lista = [1, 3, 11, 12, 44, 8, 9, 10, 23, 9, 0, 213, 99, 98]

primos = []
for num in lista:
    div = 1
    for n in range(2,num):
        if num%n == 0:
            div += 1
    if div == 1 and num != 0:
        primos.append(num)
        

print(primos)