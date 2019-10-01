def funcionHardcore():
    pass

def funcionCompararContraOriginal():
    pass

def funcionGenerarOriginal():
    pass

def funcionGenerarUnAleatorio():
    pass

def main():

    alfabeto = []
    V = [] #guarda los intentos (adivinados)
    arregloFijas = [] #guarda las fijas obtenidas (previamente)
    arregloPicas = [] #guardar las picas obtenidas (previamente)

    #se genera la secuencia que se va a adivinar
    original = funcionGenerarOriginal(alfabeto)

    #se genera una secuencia inicial para adivinar la original
    adivinado = funcionGenerarUnAleatorio(alfabeto)
    V.append(adivinado)

    fijas, picas = funcionCompararContraOriginal(original, adivinado)
    arregloFijas.append(fijas)
    arregloPicas.append(picas)

    while( fijas!=4 ):
        adivinado = funcionHardcore(V, alfabeto, arregloFijas, arregloPicas)
        V.append(adivinado)
        fijas, picas = funcionCompararContraOriginal(original, adivinado)
        arregloFijas.append(fijas)
        arregloPicas.append(picas)
    #end while

    print("Juego terminado")

if __name__== "__main__":
    main()
