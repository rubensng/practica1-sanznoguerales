def checktriangle(a, b, c):
    if (c < a + b) and (b < a + c) and (a < c + b):
        if a == b and a == c:
            return "Triangulo equilatero"
        elif a == b or b == c: 
            return "Triangulo isosceles"
        else:
            return "Triangulo escaleno"
    else:
        return "No es un triangulo"

if __name__ == "__main__":
    print("Numero de casos de prueba:")
    n = int(input())
    print(n)
    
    
    for _ in range(n):
        print("Marcar los valores de longitud de los lados del triangulo (uno por linea):")
        a = int(input())
        print(f"{a},", end="")
        
        b = int(input())
        print(f"{b},", end="")
        
        c = int(input())
        print(f"{c}:")
        
        checktriangle(a, b, c)