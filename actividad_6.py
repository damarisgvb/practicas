numeros = [23, 45, 12, 67, 8, 90, 4, 1, 78, 33, 56, 7, 19]
#doble de numero
for num  in numeros:
    print(f"el doble de : {num} es {num*2}")

#par e impar
    if num % 2 == 0:
        print(num, "es par")
    else:
       print("es impar")

#orden de numero
numeros.sort()
print("aca se ordena", numeros)

#elimar un numero
usuario = int(input("que numero necesita eliminar?"))
numeros.remove(usuario)

print(f"eliminar un elemento especifico {numeros}")

#max, min, sum,
maximo = max(numeros)
print(f"el numeros maximos son: {maximo}")

minimo = min(numeros)
print(f"el numeros minimos son: {minimo}")

suma = maximo + minimo
print(f"la suma es de: {suma}")
 

    


    
