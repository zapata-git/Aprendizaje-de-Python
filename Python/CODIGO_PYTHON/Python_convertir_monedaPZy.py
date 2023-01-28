{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "#Hacer un conversor de monedas \n",
        " Realizar un conversor de distintas monedas en Python (pesos colombianos a dólar, euro, la criptomoneda Cake y Bitcoin)."
      ],
      "metadata": {
        "id": "QkqDaH8ukpY9"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Asigancion de valores "
      ],
      "metadata": {
        "id": "1gojrZ5Hld-c"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def convertir_a_moneda(monto, moneda):\n",
        "  tasa_de_cambio = obtener_tasa_de_cambio(moneda)\n",
        "  return monto / tasa_de_cambio\n",
        "\n",
        "def obtener_tasa_de_cambio(moneda):\n",
        "  if moneda == 'dolar':\n",
        "      return 5000\n",
        "  elif moneda == 'euro':\n",
        "       return 4500\n",
        "  elif moneda == 'cake':\n",
        "       return 4000\n",
        "  elif moneda == 'bitcoint':\n",
        "        return  7000\n",
        "  else:\n",
        "    raise ValueError('Moneda no soportada')\n",
        "\n",
        "# Prueba la función\n",
        "monto = int(input('Ingrese el monto en pesos colombianos que desea convertir: '))\n",
        "moneda = input('Ingrese la moneda a la que desea convertir (dolar, euro , cake, bitcoint): ')\n",
        "\n",
        "print(f'{monto} pesos colombianos son {convertir_a_moneda(monto, moneda):.2f} {moneda}')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K1boPuW0o86H",
        "outputId": "7a45185f-71c4-4f73-f3ad-2fb62330d5b3"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese el monto en pesos colombianos que desea convertir: 175415\n",
            "Ingrese la moneda a la que desea convertir (dolar, euro , cake, bitcoint): bitcoint\n",
            "175415 pesos colombianos son 25.06 bitcoint\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Explicacion de la ultima f string\n",
        "Esta sintaxis se conoce como f-strings y es una forma de incluir variables y expresiones en una cadena de texto. Las f-strings comienzan con f seguido de una cadena de texto, y las variables y expresiones se pueden incluir en la cadena de texto precedidas por { y seguidas por }.\n",
        "\n",
        "En este caso, la f-string incluye tres elementos:\n",
        "\n",
        "    {monto}: esta es la variable monto. Se reemplazará por el valor de la variable.\n",
        "    {convertir_a_moneda(monto, moneda):.2f}: esta es una expresión que llama a la función convertir_a_moneda con dos argumentos: monto y moneda. El resultado de la función se formatea como un número flotante con dos decimales.\n",
        "    {moneda}: esta es la variable moneda. Se reemplazará por el valor de la variable."
      ],
      "metadata": {
        "id": "Z5Gn9uL6wQNL"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Claro, aquí tienes un resumen del código que te mostré:\n",
        "\n",
        "    La función convertir_a_pesos_colombianos convierte un monto dado en una moneda dada a pesos colombianos. Toma dos argumentos: monto y moneda.\n",
        "    La función obtener_tasa_de_cambio obtiene la tasa de cambio actual para una moneda dada. Toma un argumento: moneda.\n",
        "    La función convertir_a_moneda convierte un monto dado en pesos colombianos a una moneda dada. Toma dos argumentos: monto y moneda.\n",
        "\n",
        "Para usar estas funciones, el usuario puede llamarlas y pasarles los argumentos apropiados. Por ejemplo, para convertir 100 dólares estadounidenses a pesos colombianos, el usuario puede llamar a convertir_a_pesos_colombianos(100, 'USD'). Para convertir 100000 pesos colombianos a dólares estadounidenses, el usuario puede llamar a `convert"
      ],
      "metadata": {
        "id": "Qvv1Anlew8RS"
      }
    }
  ]
}