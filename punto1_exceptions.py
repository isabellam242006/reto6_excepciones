def suma(a,b) -> float:
    return a + b
def resta(a,b) -> float:
    return a-b
def multiplicación(a,b) -> float:
    return (a*b)

#El primer caso de excepción se maneja con un error de división por cero, en este punto se crea la excepción
def división(a,b) -> float:
    if b == 0:
        raise ZeroDivisionError("No es posible dividir por cero")
    return(a/b)

# El segundo error que se maneja es el de valor, es decir cuando se ingresa cualquier valor que no sea un número
while True:
    try:
        a = float(input("Ingrese un número cualquiera: "))
        b = float(input("Ingrese otro número: "))
        break
    except ValueError:
        print("Solo ingresar números")

#En esta parte se maneja el ingreso de los signos, para que únicamente se ingreesen los que están ahí
signo = str(input("Ingrese el signo de la operación que desea realizar: "))
assert signo in ["+", "-", "*", "/"], "Signo inválido"

match signo:
        case "+":
            print("La suma de " + str(a) + " y " + str(b) + " es " + str(suma(a,b)))
        case "-":
            print("La resta de " + str(a) + " y " + str(b) + " es " + str(resta(a,b)))
        case "*":
            print("La multiplicación de " + str(a) + " y " + str(b) + " es " + str(multiplicación(a,b)))
        case "/":
            try:
                print("La división de " + str(a) + " y " + str(b) + " es " + str(división(a,b)))
            except ZeroDivisionError:
                print("Cannot divide by zero")
        case _:
            print("""Ingresa un signo de suma(+), multiplicación(*), resta(-) o división(/)""")