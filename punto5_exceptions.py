def anagrama(lista_palabras):
    lista_anagramas = []
    for palabra1 in lista_palabras:
        for palabra2 in lista_palabras:
            if palabra1 != palabra2 and sorted(palabra1) == sorted(palabra2):
                lista_anagramas.append(palabra1)
                lista_anagramas.append(palabra2)
    return lista_anagramas

if __name__ == "__main__":            
    lista_palabras = []
    while True:
        palabra = input("Ingrese una palabra cualquiera (Vacío para terminar): ")
        if palabra == "":
            break
        try:
            if not palabra.isalpha():
                raise ValueError("Por favor, ingrese solo palabras (sin números o caracteres especiales)")
            lista_palabras.append(palabra)
        except ValueError as e:
            print(e)
    
    anagramas = anagrama(lista_palabras)
    if anagramas:
        print("Las palabras que son anagramas entre sí son:", anagramas)
    else:
        print("No hay anagramas en la lista de palabras.")
