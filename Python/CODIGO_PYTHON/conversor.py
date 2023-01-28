# def conversor(tipo_pesos, valor_dolar):




# #Input del usuario
# pesoscol = input("¿Cuantos pesos colombianos tienes ?")
# pesoscol = float(pesoscol)
# #Declaracion de valores
# valor_dolar = 3679
# valor_euro = 4383
# valor_cake = 58800
# valor_btc = 136134100
# #Calculo valor dolar
# dolares= pesoscol / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# #Calculo Valor Euro
# euros= pesoscol / valor_euro
# euros = round(euros, 2)
# euros = str(euros)
# #Calculo Cantidad de CAKE
# cakes = pesoscol / valor_cake
# cakes = round(cakes, 4)
# cakes = str(cakes)
# #Calculo Bitcoin
# btcs = pesoscol / valor_btc
# btcs = round(btcs, 9)
# btcs = str(btcs)
# #Prints
# print("Tienes $"+ dolares + " dolares")
# print("Tienes $"+ euros + " Euros")
# print("Tienes: " + cakes + " CAKE")
# print("Tienes: " + btcs + " Bitcoins")


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