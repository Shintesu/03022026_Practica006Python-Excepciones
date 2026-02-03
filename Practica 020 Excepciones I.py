def suma(num1, num2):
    return num1+num2
def resta(num1, num2):
    return num1-num2
def multiplica(num1, num2):
    return num1*num2
def divide(num1,num2):      
    try:
        return num1/num2  # num1=8, num2=0 // se debe hacer una captura o control de excepción
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return("Operación errónea")

while True: # se crea un bucle infinito para que nos vuelva a pedir el valor erróneo
    try: # se comienza el uso de try y except antes y después de las líneas que generan el problema
        op1=(int(input("Introduce el primer numero: ")))

        op2=(int(input("Introduce el segundo numero: ")))   
        break 

    except ValueError:
        print("Los valores introducidos no son correctos, intentalo de nuevo")
    
operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")
if operacion=="suma":
    print(suma(op1,op2))
elif operacion=="resta":
    print(resta(op1,op2))
elif operacion=="multiplica":
    print(multiplica(op1,op2))
elif operacion=="divide":
    print(divide(op1,op2))
else:
    print ("Operacion no contemplada")

print("Operacion ejecutada. Continuacion de ejecucion del programa. ")
