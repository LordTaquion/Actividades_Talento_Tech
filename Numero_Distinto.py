# Realizado por Jairo Andres Sánchez

def devolver_distinto(num1, num2, num3):
    
    numeros = [num1, num2, num3]
    resultado = sum(numeros)

    if resultado > 15:
        mayor = max(numeros)
        print("Usted ingreso ", numeros)
        print(f"El numero mayor de esta lista es: {mayor}")

    elif resultado < 10:
        menor = min(numeros)
        print("Usted ingreso ", numeros)
        print(f"El numero menor de esta lista es: {menor}")

    else:
        medio = sorted(numeros)[1]
        print("Usted ingreso ", numeros)
        print(f"El numero intermedio de esta lista es: {medio}")

devolver_distinto(4, 7, 1)