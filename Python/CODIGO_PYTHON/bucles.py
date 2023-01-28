
# for i in range(10):
#      resultado = 2**i
#      if (resultado < 1000):
#       print(resultado)


def run():
     LIMITE = 1000
     
     contador = 0
     potencia_2 = 2**contador
     while potencia_2 < LIMITE:
          print("2 elevado a "+ str(contador) + "es igual a:" +str(potencia_2))
          contador = contador + 1
          potencia_2 = 2**contador


if __name__ == '__main__':
     run()
