def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
    
    # texto = input("Escribe un texto: ")
    # for letra in texto:
    #     if letra == 'o':
    #      break
    #     print (letra)
    
    texto = input("Escribe un texto: ")
    num_letras = len(texto.replace(" ", "").replace(",", "").replace("!", ""))
    while num_letras < 5:
        print(texto)
        break
    else:
        print(" El texto esta muy largo")

if __name__ == '__main__':
    run()
