def palindromo(palabra) -> str:
    if not palabra.strip():  # Si la palabra es vacía o solo contiene espacios
        raise ValueError("La palabra no puede ser vacía o solo contener espacios")
    if not palabra.isalpha():  # Si la palabra contiene caracteres no alfabéticos
        raise ValueError("Solo ingresar palabras")
    for letra in range(len(palabra)):  #Recorremos cada letra de la palabra
        if palabra[letra] == palabra[len(palabra)-letra-1]:
            return True
        else:
            return False

while True:
    try:
        palabra = str(input("Ingrese una palabra: "))
        if palindromo(palabra):
            print("La palabra ingresada es palindromo")
        else:
            print("La palabra ingresada no es palindromo")
        break
    except ValueError as e:
        print(e)