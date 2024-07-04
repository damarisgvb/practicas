
def contiene_pares(lista): 
    for numero in lista: 
        if numero % 2 == 0:  #para saber si es par o no debemos dividirlo por 2.
            return True   
    return False
            
 
numeros = [2,1,9] #lista de numeros
res = contiene_pares(numeros)#el contiene pares, le ponemos la lista de numero
 
print(res)
     

