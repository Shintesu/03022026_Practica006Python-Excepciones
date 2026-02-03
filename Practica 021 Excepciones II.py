# EXCEPCIONES II

def divide(): 

    try:
        op1=(float(input("Introduce el primer numero: ")))
        op2=(float(input("Introduce el segundo numero: ")))
        print("La división es: " + str(op1/op2))
    except ValueError:          # excepción del tipo string
        print("Las letras no son números")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

    finally: # en este caso no apluca, pero cuando sí, el finally se ejecuta sí o sí
        print("Calculo finalizado")
    
divide()



# excepciones generales
def divide(): 

    try:
        op1=(float(input("Introduce el primer numero: ")))
        op2=(float(input("Introduce el segundo numero: ")))
        print("La división es: " + str(op1/op2))
    except:
        print("Ha ocurrido un error")
    
divide()




# finally

def divide(): 

    try:
        op1=(float(input("Introduce el primer numero: ")))
        op2=(float(input("Introduce el segundo numero: ")))
        print("La división es: " + str(op1/op2))

    finally: # al usar el try y finally surgen errores, pero el código puede ejecutarse completamente
            print("Calculo finalizado")
        
    divide()