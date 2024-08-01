largo = int(input("ingrese el largo:"))
             
ancho = int(input("ingrese el ancho:"))

area = ancho * largo
perimetro = largo * 2 + ancho*2
 
tuple = (area, perimetro)
 
print(f"la area y el perimetroes es de:{tuple}")