kilogramo = float (input("ingrese su peso en kilogramo:"))
print(f"su peso es de: {kilogramo}") #aca nombre un varieable, que lo domine como kilogramo.
#luego coloque "float" que significa que pido un numero flotante cuando el sistema pida el peso,podremos poner un numero con "punto"
# luego el "input" que significa que significa que los datos proximos que coloque, apareceran en la pantalla
#el print signica imprimir, digamos la linea 1... estamos pidiendo un dato, y la linea 2 estamos impriendo casi lo mismo que la primer linea, estamos confirmando. 

estatura = float (input("ingrese su estatura:")) #aca tambien hicimos los mismo, nombramos una variable, que en este caso puse "estatura", ya que es un numero con punto, se debe ultilizar "float"que significa numero flotante, y luego colocamos input, que significa que los proximos datos aparecen en la pantalla, apareceran lo que pusimos entre comillas.
print(f"su estatura es de: {estatura}")#el print estamos imprimiendo, digamos confirmando el dato que coloco el usuario o la persona, luego entre comillas, ponemos el texto completo, y que aparecera en la pantalla. y entre llave colocamos la variable, que aparece la confimacion del usuario su estatura.


imc = kilogramo/(estatura*estatura) #aca pusimos un variable que seria IMC que seria igual al resultado de kilogramos divido, a la multiplicacion por estatura por estatura.
print(f"su imc es: {imc}") #luego implimimos el resultado del anterior, y aparecera en la pantalla.



if imc < 18.5:              #aca lo que hice fue que 18 era menor al imc era bajo peso y apararecera en la pantalla

    print(f"bajo peso")

elif 18.5 <= imc < 25:
    print(f"peso normal")  # si 18,5 era menor o iguaal a imc fuese mayor era peso normal


elif 25 <= imc < 30:     
    print(f"sobrepeso")


elif imc >= 30:
    print(f"obecidad")





