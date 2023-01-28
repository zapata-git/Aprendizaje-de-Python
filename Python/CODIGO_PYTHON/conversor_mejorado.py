# def suma(a,b):
#     print("se suman dos numeros")
#     resultados = a+b
#     return resultados

# sumatoria = suma(1,4)
# print(sumatoria)
def convertir(tipo_moneda, dolares):
    pesos = float(input('¿Cuántos ' + tipo_moneda + ' desea cambiar? '))
    return round(pesos / dolares, 2)

menu = """
Bienvenido al conversor de monedas. 🤔

1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos

Elija una opción: """

opcion = int(input(menu))

# Coloque los precios a valores recientes
if opcion == 1:
    print('Su cantidad de dolares es: $' + str(convertir('colombianos', 3715.50)))

elif opcion == 2:
    print('Su cantidad de dolares es: $' + str(convertir("argentinos", 70.50)))

elif opcion == 3:
    print('Su cantidad de dolares es: $' + str(convertir('mexicanos', 22.66)))

else:
    print('Ingrese una opción válida, por favor.')