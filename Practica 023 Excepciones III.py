# crearé un ejemplo de una calculadora que intente hallar la raíz cuadrada de un número negativo

import math

def calcula_raiz(num1):
    if num1<0:
        raise ValueError ("El número no puede ser negativo") # creo la excepción
    else:
        return math.sqrt(num1)

op1=(int(input("Introduce un número: ")))

try: # encierro la excepción
    print(calcula_raiz(op1))
except ValueError as ErrorDeNumeroNegativo: # con as le doy un alias a la excepción
    print (ErrorDeNumeroNegativo)
print("Programa terminado")
