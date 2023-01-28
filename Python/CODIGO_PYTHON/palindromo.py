def es_palindromo(palabra):
    palabra = palabra.replace(' ','').lower()

    if palabra[::] == palabra [::-1]:
        return True
    else:
        return False


def run():
    palabra = input('Ingrese una plabra o frase:  ')
    if es_palindromo(palabra):
        print(palabra + '  es palindromo')
    else:
        print(palabra+'No es palindroma')


if __name__ == "__main__":
        run()






    