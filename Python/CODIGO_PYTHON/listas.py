mi_lista = [1, 2, 3, 4, 5]
for elemento in mi_lista:
    print(elemento)
print(', '.join(map(str, mi_lista)))
    
## El método join() es un método de las cadenas en Python que se utiliza para unir elementos de una secuencia 
# (como una lista o tupla) en una sola cadena, utilizando la cadena en la que se llama el método como separador.

## Otro ejemplo 
mi_lista = ["perro", "gato", "ratón"]
separador = ", "
cadena_unida = separador.join(mi_lista)
print(cadena_unida)