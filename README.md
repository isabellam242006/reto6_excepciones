# Reto 6 - Excepciones
### Add the required exceptions in the Reto 1 code assigments.
**Punto 1**
```python
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
```
**Punto 2**
```python
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
```
**Punto 3**
```python
def numeros_primos(lista):
    for num in lista:
        if num <= 1:
            return False
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
    return True

if __name__ == "__main__":
    lista = []
    lista_primos = []
    while True:
        try:
            numeros = input("Ingrese un número entero cualquiera (Vacío para terminar): ")
            if numeros == "":
                break
            numeros = int(numeros)
            lista.append(numeros)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    
    for num in lista:
        if numeros_primos([num]):
            lista_primos.append(num)
    
    if lista_primos:
        print("Los números primos en la lista son:", lista_primos)
    else:
        print("No hay números primos en la lista dada")
```
**Punto 4**
```python
def mayor_suma(lista):
    if len(lista) < 2:
        raise ValueError("La lista debe contener al menos dos números")
    mayor_suma = lista[0] + lista[1]
    for i in range(1, len(lista)-1):
        siguiente_suma = lista[i] + lista[i+1]     
        if siguiente_suma > mayor_suma:
            mayor_suma = siguiente_suma
    
    return mayor_suma


if __name__ == "__main__":
    lista = []
    while True:
        try:
            numeros = input("Ingrese un número entero cualquiera (Vacío para terminar): ")
            if numeros == "":
                break
            numeros = int(numeros)
            lista.append(numeros)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    
    try:
        print("La mayor suma entre dos números consecutivos es ", mayor_suma(lista))
    except ValueError as e:
        print(e)
```
**Punto 5**
```python
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
```
### In the package Shape identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.

```python
import math

class Punto:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set_x(self, value):
        self._x = value

    def set_y(self, value):
        self._y = value

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


class Line:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def set_start(self, value):
        self._start = value

    def set_end(self, value):
        self._end = value

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def compute_length(self):
        return math.sqrt((self._end.get_x() - self._start.get_x())**2 + (self._end.get_y() - self._start.get_y())**2)


class Shape:
    def __init__(self, is_regular):
        self._is_regular = is_regular
        self._vertices = []
        self._edges = []

    def set_is_regular(self, is_regular):
        self._is_regular = is_regular
    
    def get_is_regular(self):
        return self._is_regular
    
    def add_vertex(self, vertex):
        self._vertices.append(vertex)
    
    def get_vertices(self):
        return self._vertices.copy()
    
    def add_edge(self, edge):
        self._edges.append(edge)
    
    def get_edges(self):
        return self._edges.copy()

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, is_regular):
        super().__init__(is_regular)
        
        #En esta parte coloqué una excepción para que se ingresara únicamente números
        for i in range(3):  
            try:
                x = float(input(f"Introduce la coordenada x del vértice {i+1}: "))
                y = float(input(f"Introduce la coordenada y del vértice {i+1}: "))
            except ValueError:
                raise ValueError("Las coordenadas deben ser números")
            vertex = Punto(x, y)
            self.add_vertex(vertex)
        
        for i in range(3):  
            start = self._vertices[i]
            end = self._vertices[(i+1)%3]
            edge = Line(start, end)
            self.add_edge(edge)
        
    def compute_area(self):
        a = self._edges[0].compute_length()
        b = self._edges[1].compute_length()
        c = self._edges[2].compute_length()
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    
    def compute_perimeter(self):
        perimeter = sum(edge.compute_length() for edge in self._edges)
        return perimeter

#En esta parte añadí la división de división por cero, ya que la parte de calcular los angulos en algunas ocasiones devuelve error por esto
    def compute_inner_angles(self):
        angles = []
        for i in range(3):
            a = self._edges[i].compute_length()
            b = self._edges[(i+1)%3].compute_length()
            c = self._edges[(i+2)%3].compute_length()
            denominator = 2 * b * c
            if denominator == 0:
             raise ValueError("La división por cero no está permitida")
            angle = math.degrees(math.acos((b**2 + c**2 - a**2) / denominator))
            angles.append(angle)
        return angles


class Isosceles(Triangle):
    def __init__(self):
        super().__init__(False)


class Equilateral(Triangle):
    def __init__(self):
        super().__init__(True)


class Scalene(Triangle):
    def __init__(self):
        super().__init__(False)


class TriRectangle(Triangle):
    def __init__(self):
        super().__init__(False)

class Rectangle(Shape):
    def __init__(self, is_regular):
        super().__init__(is_regular)
        
        #En esta parte también coloqué una excepción para que se ingresara únicamente números
        for i in range(4):
            try:  
                x = float(input(f"Introduce la coordenada x del vértice {i+1}: "))
                y = float(input(f"Introduce la coordenada y del vértice {i+1}: "))
            except ValueError:
                raise ValueError("Las coordenadas deben ser números")
            vertex = Punto(x, y)
            self.add_vertex(vertex)
        
        for i in range(4):  
            start = self._vertices[i]
            end = self._vertices[(i+1)%4]
            edge = Line(start, end)
            self.add_edge(edge)
        
    def compute_area(self):
        a = self._edges[0].compute_length()
        b = self._edges[1].compute_length()
        area = a * b
        return area
    
    def compute_perimeter(self):
        perimeter = sum(edge.compute_length() for edge in self._edges)
        return perimeter

    def compute_inner_angles(self):
        angles = [90, 90, 90, 90]
        return angles


class Square(Rectangle):
    def __init__(self):
        super().__init__(True)

#Imprimir los resultados

try:
    triangle = Triangle(False)
    area = triangle.compute_area()
    print("El área del triángulo es:", area)

    perimeter = triangle.compute_perimeter()
    print("El perímetro del triángulo es:", perimeter)

    if triangle.get_is_regular():
        print("El triángulo es regular")
    else:
        print("El triángulo no es regular")

    angles = triangle.compute_inner_angles()
    print("Los ángulos internos del triángulo son:", angles)

    lengths = [edge.compute_length() for edge in triangle.get_edges()]

    if len(set(lengths)) == 1:
        print("Type: Equilateral")
    elif len(set(lengths)) == 2:
        print("Type: Isosceles")
    else:
        print("Type: Scalene")
except Exception as e:
    print("Ocurrió un error al procesar el triángulo:", e)

try:
    rectangle = Rectangle(False)

    area = rectangle.compute_area()
    print("El área del rectángulo es:", area)

    perimeter = rectangle.compute_perimeter()
    print("El perímetro del rectángulo es:", perimeter)

    angles = rectangle.compute_inner_angles()
    print("Los ángulos internos del rectángulo son:", angles)
except Exception as e:
    print("Ocurrió un error al procesar el rectángulo:", e)
```
