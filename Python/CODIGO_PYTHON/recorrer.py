def run():
    # nombre = input("Escribe tu nombre: ")
    # for letra in nombre:
    #     print(letra)
    
    Frase = input ('Escribe una frase: ')
    for caracter in Frase:
       print(caracter.replace(" ", "-").upper())


if __name__ == '__main__':
    run()