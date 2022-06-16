# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def esBisiesto(año):
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        return '¡Felicidades! El año es bisiesto'
    else:
        return 'Lo lamento, el año no es bisiesto.'
        
print(esBisiesto(int(input('Introduce un año '))))