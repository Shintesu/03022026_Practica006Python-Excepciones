# EXCEPCIONES III lanzamiento de excepciones y raise

def evalua_edad(edad):

    if edad<0:  # se coloca el condicional if es menor que 0
        raise TypeError("No se permiten edades negativas")
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres un adulto"
    elif edad<65:
        return "Eres casi un adulto mayor"
    elif edad<100:
        return "Eres un adulto mayor, cuídate..."
    
print(evalua_edad(-18))

