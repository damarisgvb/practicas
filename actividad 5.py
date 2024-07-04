numero = int (input("ingrese un numero:"))
print(f"numero ingreso fue:{numero}")

lista = [1, 2, 3, 4]
print(lista) 

if numero in lista:
 print(f"el numero fue encontrado")
elif numero != lista: 
 print(f"el numero no fue encontrado")
