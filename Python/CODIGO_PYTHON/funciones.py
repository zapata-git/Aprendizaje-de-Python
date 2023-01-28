
# print("Mensaje especial")
# print("Estoy a prendiendo a usar funciones")
# print("Mensaje especial")
# print("Estoy a prendiendo a usar funciones")

##Funciones sin argumentos 

def imprimir_mensaje():
    print("Mensaje especial")
    print("Estoy a prendiendo a usar funciones")


## nuestra primera funcion en python 

# def imprimir_cositas(texto):
#     mensaje = "Mensaje especial,  "+ texto
#     return mensaje

# print(imprimir_cositas("🚵‍♀️🚴‍♂️🚴‍♂️🚵‍♀️🚵‍♀️🚴‍♂️🚴‍♂️🚴‍♀️🚴‍♀️🚲🚲"))
# imprimir_mensaje()1

def conversacion(opcion):
    print('Elegiste la opcion: ' + str(opcion))
    print('Hola')
    print('Cómo estás')
    print('Adiós')

opcion = int(input('Ingrese una opción (1, 2, 3): '))

if opcion == 1:
    conversacion(opcion)

elif opcion == 2:
    conversacion(opcion)

elif opcion == 3:
    conversacion(opcion)

else:
    print('Escribe una opción correcta.')
