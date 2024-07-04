#aqui la lista de tareas
lista_de_tareas = ["a"]

#la presentacion del programa
print("Hola, bienvenido ")
print("En esta aplicacion podra agregar nuevas tareas, eliminar tareas existentes, y mostrar una lista completa de las tareas actuales")

#las opciones que ofrecemos al usuario para que elija
opcion=int(input("Eliga una opcion :opcion 1 Navegacion hacia las principales funcionalidades de la aplicacion, opcion 2: Gestion de Tareas, 3:Eliminar tarea opcion 4: Mostrar Tarea"))

#Primero pusimos un while para que elija el usuario opciones , y en ese while habia dentro if y elif que serian las opciones
while opcion<5:
    if opcion == 1:
        agregar=input("Que tarea desea agregar?")
        lista_de_tareas.append(agregar)
        eliminar=input("Que tarea desea eliminar?")
        lista_de_tareas.remove(eliminar)
        print(lista_de_tareas)
    elif opcion == 2:
        agregar=input("Que tarea desea agregar?")
        lista_de_tareas.append(agregar)
        print(lista_de_tareas)
    elif opcion == 3:
        eliminar=input("Ingrese el nombre de la tarea que desea eliminar")
        lista_de_tareas.remove(eliminar)
        if eliminar in lista_de_tareas:
            print("su tarea se elimino")
        else:
            print( "Su tarea no esta en la lista")   
    elif opcion == 4:
         print(lista_de_tareas)
         
         if lista_de_tareas:
             for tarea in lista_de_tareas:
                 print("Su lista esta con elementos")
         else:
            print("No posee elementos")
    opcion=int(input("Eliga una opcion :opcion 1 Navegacion hacia las principales funcionalidades de la aplicacion, opcion 2: Gestion de Tareas, 3:Eliminar tarea opcion 4: Mostrar Tarea"))