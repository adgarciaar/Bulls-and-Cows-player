## =========================================================================
## @authors Adrian Garcia & Nicolas Miranda
## =========================================================================

import time

import copy, random
from BullsAndCowsBasePlayer import *

class Tupla:
    def __init__(self, posicion, caracter):
        self.posicion = posicion
        self.caracter = caracter

## *************************************************************************
class BullsAndCows_proyecto( BullsAndCowsBasePlayer ):

    def __init__( self, n, a ):

        BullsAndCowsBasePlayer.__init__( self, n, a )
        self.m_CurrentSolution = ""

        self.fijasDetectadas = []
        self.picasDetectadas = []

        self.posicionesFijas = []
        for i in range (0, n):
            self.posicionesFijas.append(False)

        self.posicionesValidas = []
        for i in range (0, n):
            self.posicionesValidas.append(False)

        self.cambioFueRealizado = False
        self.posicionDelCambio = 0
        self.caracterCambiado = None

        self.fijasIntentoAnterior = None
        self.picasIntentoAnterior = None

        self.primeraPica = 0
        self.siguientePica = 0
        self.picaTemporal = None
        self.picaDentroDeSolucion = False

        self.seRevirtioFija = False
        self.seRevirtioPica = False

        self.posicionInicialPica = 0
        self.posicionActualPica = 0
        self.picaMoviendose = None
        self.caracterReemplazado = None

        self.vaEnPasoMoverPicas = False

    ## -----------------------------------------------------------------------
    def guess( self, b, c ):

        if self.m_CurrentSolution == "":
            s = copy.deepcopy( list( self.m_Alphabet ) )
            random.shuffle( s )
            self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )

            self.fijasIntentoAnterior = b
            self.picasIntentoAnterior = c
            print("--------------------------------------------------")
            return self.m_CurrentSolution

        #time.sleep(0.3)
        print("Current solution "+self.m_CurrentSolution)
        print("Numero de fijas detectadas: "+str(len(self.fijasDetectadas)))

        if(self.cambioFueRealizado == True):

            #print("fijas intento anterior: "+str(self.fijasIntentoAnterior))
            #print("picas intento anterior: "+str(self.picasIntentoAnterior))

            if( b !=  self.fijasIntentoAnterior or c != self.picasIntentoAnterior):

                #hubo un cambio que nos interesa

                self.posicionDelCambio = self.posicionDelCambio-1

                if(b > self.fijasIntentoAnterior): #lo que se agregó es una fija

                    #print("fija detectada agregada")

                    nuevaFija = Tupla( self.posicionDelCambio, self.m_CurrentSolution[self.posicionDelCambio] )
                    self.fijasDetectadas.append(nuevaFija)

                    #guardar dónde hay una fija
                    self.posicionesFijas[ self.posicionDelCambio ] = True
                    self.posicionesValidas[ self.posicionDelCambio ] = True

                elif(b < self.fijasIntentoAnterior): #lo que se quitó es una fija

                    #print("fija detectada removida pero puesta")

                    nuevaFija = Tupla( self.posicionDelCambio, self.caracterCambiado )
                    self.fijasDetectadas.append(nuevaFija)

                    #guardar dónde hay una fija
                    self.posicionesFijas[ self.posicionDelCambio ] = True

                    self.posicionesValidas[ self.posicionDelCambio ] = True

                    listCurrentSolution = list(self.m_CurrentSolution)

                    #descartar lo que se agregó
                    #self.m_Alphabet = self.m_Alphabet.replace( listCurrentSolution[self.posicionDelCambio], '' )

                    #revertir cambio
                    listCurrentSolution[ self.posicionDelCambio ] = self.caracterCambiado
                    self.m_CurrentSolution = ''.join(listCurrentSolution)
                    self.seRevirtioFija = True
                    #self.fijasIntentoAnterior = self.fijasIntentoAnterior + 1

                    #print("ahora quedo: "+self.m_CurrentSolution)

                if(c > self.picasIntentoAnterior and b == self.fijasIntentoAnterior): #lo que se agregó es una pica

                    #print("pica detectada agregada")

                    nuevaPica = Tupla( self.posicionDelCambio, self.m_CurrentSolution[self.posicionDelCambio] )
                    #self.picasDetectadas.append(nuevaPica)

                    self.posicionesValidas[ self.posicionDelCambio ] = True

                elif(c < self.picasIntentoAnterior and b == self.fijasIntentoAnterior): #lo que se quitó es una pica

                    #print("pica detectada removida pero puesta")

                    nuevaPica = Tupla( self.posicionDelCambio, self.caracterCambiado )
                    #self.picasDetectadas.append(nuevaPica)

                    self.posicionesValidas[ self.posicionDelCambio ] = True

                    listCurrentSolution = list(self.m_CurrentSolution)

                    #descartar lo que se agregó
                    #self.m_Alphabet = self.m_Alphabet.replace( listCurrentSolution[self.posicionDelCambio], '' )

                    #revertir cambio
                    listCurrentSolution[ self.posicionDelCambio ] = self.caracterCambiado
                    self.m_CurrentSolution = ''.join(listCurrentSolution)
                    self.seRevirtioPica = True
                    #self.picasIntentoAnterior = self.picasIntentoAnterior + 1

                    #print("ahora quedo: "+self.m_CurrentSolution)

                self.cambioFueRealizado = False
                self.posicionDelCambio = 0
                self.caracterCambiado = None

                if (self.seRevirtioFija == True):
                    self.fijasIntentoAnterior = self.fijasIntentoAnterior + 1
                    self.seRevirtioFija = False
                    self.picasIntentoAnterior = c

                if (self.seRevirtioPica == True):
                    self.picasIntentoAnterior = self.picasIntentoAnterior + 1
                    self.seRevirtioPica = False
                    self.fijasIntentoAnterior = b

                if( self.seRevirtioFija == False and self.seRevirtioPica == False):
                    self.fijasIntentoAnterior = b
                    self.picasIntentoAnterior = c
                print("--------------------------------------------------")
                return self.m_CurrentSolution

        if (b==0 and c==0): #descartar del alfabeto todos los caracteres que no van

            self.cambioFueRealizado = False

            for item in list( self.m_CurrentSolution ):
                #print("este es uno que muere: "+item)
                #quitar los caracteres que no sirvieron
                self.m_Alphabet = self.m_Alphabet.replace( item, '' )
            s = copy.deepcopy( list( self.m_Alphabet ) )
            random.shuffle( s )
            self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )

        elif( b+c == self.m_GuessSize or self.vaEnPasoMoverPicas == True ): #ya están todos los caracteres que se necesitan

            print("caso todos ya estan")

            #time.sleep(0.4)

            self.cambioFueRealizado = False
            self.vaEnPasoMoverPicas = True

            if (self.picaDentroDeSolucion == False):

                print("entra primera vez a jugar con picas")

                while(self.posicionesFijas[self.posicionInicialPica] == True):
                    self.posicionInicialPica = self.posicionInicialPica + 1

                self.posicionActualPica = self.posicionInicialPica + 1

                while(self.posicionesFijas[self.posicionActualPica] == True):
                    self.posicionActualPica = self.posicionActualPica + 1

                self.picaMoviendose = self.m_CurrentSolution[ self.posicionInicialPica ]
                listCurrentSolution = list(self.m_CurrentSolution)
                self.caracterReemplazado = self.m_CurrentSolution[ self.posicionActualPica ]
                listCurrentSolution[ self.posicionActualPica ] = self.picaMoviendose
                listCurrentSolution[ self.posicionInicialPica ] = '_'

                self.m_CurrentSolution = ''.join(listCurrentSolution)

                self.picaDentroDeSolucion = True

                print("termina la primera vez")

            else: #se está moviendo una pica

                print("entra segunda vez a jugar con picas")

                print(self.posicionesFijas)

                if (b > self.fijasIntentoAnterior): #si cambió # de fijas

                    print("aumento fijas")

                    nuevaFija = Tupla( self.posicionActualPica, self.m_CurrentSolution[self.posicionActualPica] )
                    self.fijasDetectadas.append(nuevaFija)

                    #guardar dónde hay una fija
                    self.posicionesFijas[ self.posicionActualPica ] = True

                    #revertir el cambio
                    listCurrentSolution = list(self.m_CurrentSolution)
                    #listCurrentSolution[ self.posicionActualPica ] = self.caracterReemplazado
                    listCurrentSolution[ self.posicionInicialPica ] = self.caracterReemplazado
                    self.m_CurrentSolution = ''.join(listCurrentSolution)

                    self.posicionInicialPica = 0
                    self.posicionActualPica = 0
                    self.picaMoviendose = None
                    self.caracterReemplazado = None
                    self.picaDentroDeSolucion = False

                elif(b < self.fijasIntentoAnterior):

                    print("se redujo fijas")

                    #revertir el cambio y marcar fija

                    #revertir el cambio
                    listCurrentSolution = list(self.m_CurrentSolution)
                    listCurrentSolution[ self.posicionActualPica ] = self.caracterReemplazado
                    listCurrentSolution[ self.posicionInicialPica ] = self.picaMoviendose
                    self.m_CurrentSolution = ''.join(listCurrentSolution)

                    #marcar fija
                    self.posicionesFijas[ self.posicionInicialPica ] = True

                    #reinicializar variables
                    self.posicionInicialPica = 0
                    self.posicionActualPica = 0
                    self.picaMoviendose = None
                    self.caracterReemplazado = None
                    self.picaDentroDeSolucion = False

                else: #continuar moviendo la pica, porque no cambió el # de fijas

                    print("se continua moviendo pica")

                    #revertir el cambio
                    listCurrentSolution = list(self.m_CurrentSolution)
                    listCurrentSolution[ self.posicionActualPica ] = self.caracterReemplazado
                    listCurrentSolution[ self.posicionInicialPica ] = self.picaMoviendose
                    self.m_CurrentSolution = ''.join(listCurrentSolution)

                    #moverse a la siguiente posición con una pica
                    self.posicionActualPica = self.posicionActualPica + 1
                    if (self.posicionActualPica == self.m_GuessSize):
                        self.posicionActualPica = 0
                    while(self.posicionesFijas[self.posicionActualPica] == True):
                        self.posicionActualPica = self.posicionActualPica + 1
                        if (self.posicionActualPica == self.m_GuessSize):
                            self.posicionActualPica = 0

                    #cambiar la siguiente posición
                    listCurrentSolution = list(self.m_CurrentSolution)
                    self.caracterReemplazado = self.m_CurrentSolution[ self.posicionActualPica ]
                    listCurrentSolution[ self.posicionActualPica ] = self.picaMoviendose
                    listCurrentSolution[ self.posicionInicialPica ] = '_'

                    self.m_CurrentSolution = ''.join(listCurrentSolution)


        else: # se hace cambio porque no se cumple los otros casos principales

            #print("caso se hace cambio")

            self.cambioFueRealizado = True

            listCurrentSolution = list(self.m_CurrentSolution)

            indice = 0
            s = copy.deepcopy( list( self.m_Alphabet ) )
            random.shuffle( s )
            while(s[indice] in listCurrentSolution): #para no repetir uno mismo
                indice = indice+1

            if ( self.posicionDelCambio == self.m_GuessSize ):
                self.posicionDelCambio = 0
            while ( self.posicionesValidas[ self.posicionDelCambio ] == True ):
                self.posicionDelCambio = self.posicionDelCambio + 1
                if ( self.posicionDelCambio == self.m_GuessSize ):
                    self.posicionDelCambio = 0

            #hacer un cambio
            listCurrentSolution = list(self.m_CurrentSolution)
            self.caracterCambiado = listCurrentSolution[ self.posicionDelCambio ]
            listCurrentSolution[ self.posicionDelCambio ] = s[indice]

            self.posicionDelCambio = self.posicionDelCambio + 1

            self.m_CurrentSolution = ''.join(listCurrentSolution)

        self.fijasIntentoAnterior = b
        self.picasIntentoAnterior = c
        print("--------------------------------------------------")
        return self.m_CurrentSolution
