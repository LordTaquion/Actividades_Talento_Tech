import random

def secret():
    palabras = ["python", "programacion", "ordenador", "desarrollo", "inteligencia", "talento", "aleatorio", "computacion", "ahorcado", "estudiar"]
    return random.choice(palabras)

def mostrar_tablero(palabra, letra_adivinada):
    tablero = ""
    for i in palabra:
        if i in letra_adivinada:
            tablero += i + " "
        else:
            tablero += "_ "
    return tablero

def inicio_juego():
    palabra = secret()
    letra_adivinada = []
    vidas = 6

    print("Hola este es el juego del ahorcado, tienes que adivinar las letras de una la palabra, tienes 6 vidas para rellenar los espacios")
    print(mostrar_tablero(palabra, letra_adivinada))

    while True:
        letra = input("Ingrese una letra: ").lower()
        if letra in palabra:
            letra_adivinada.append(letra)
            print ("Acertaste")
        elif letra in letra_adivinada:
            print("Ya intentaste con esta letra")
        else:
            vidas -= 1
            print("Incorrecto. Te quedan {} vidas".format(vidas))
            if vidas == 0:
                print("Perdiste, la palbara era '{}'.".format(palabra))
                break
        
        tablero = mostrar_tablero(palabra, letra_adivinada) 
        print (tablero)

        if "_" not in tablero:
            print("¡Felicidades! ¡Ganaste!")
            break

inicio_juego()