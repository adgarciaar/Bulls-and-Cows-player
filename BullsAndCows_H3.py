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
class BullsAndCows_H3( BullsAndCowsBasePlayer ):

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

        #self.picasDetectadas = []

    ## -----------------------------------------------------------------------
    def guess( self, b, c ):

        if self.m_CurrentSolution == "":
            s = copy.deepcopy( list( self.m_Alphabet ) )
            random.shuffle( s )
            self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )
            return self.m_CurrentSolution
        else:

            #time.sleep(1.0)
            print("Current solution "+self.m_CurrentSolution+"\n")

            if (b==0 and c==0): #descartar del alfabeto todos los caracteres que no van

                self.cambioFueRealizado = False

                print("DESCARTAR TODAS")

                for item in list( self.m_CurrentSolution ):
                    #print("este es uno que muere: "+item)
                    #quitar los caracteres que no sirvieron
                    self.m_Alphabet = self.m_Alphabet.replace( item, '' )
                s = copy.deepcopy( list( self.m_Alphabet ) )
                random.shuffle( s )
                self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )

            if(self.cambioFueRealizado == True):

                #print("Cambio fue realizado")
                #print(self.posicionesValidas)
                #print("posicion del cambio: "+str(self.posicionDelCambio))

                if( b !=  self.fijasIntentoAnterior or c != self.picasIntentoAnterior):
                #if( b != self.fijasIntentoAnterior):

                    print("fijas anteriores = "+ str(self.fijasIntentoAnterior))
                    print("fijas actuales = "+ str(b))

                    print("picas anteriores = "+ str(self.picasIntentoAnterior))
                    print("picas actuales = "+ str(c))

                    #hubo un cambio que nos interesa

                    self.posicionDelCambio = self.posicionDelCambio-1

                    if(b != self.fijasIntentoAnterior):

                        if(b > self.fijasIntentoAnterior): #lo que se agregó una fija

                            print("FIJA SE DESCUBRIO")

                            nuevaFija = Tupla( self.posicionDelCambio, self.m_CurrentSolution[self.posicionDelCambio] )
                            self.fijasDetectadas.append(nuevaFija)
                            #quitarla del alfabeto
                            #self.m_Alphabet = self.m_Alphabet.replace( nuevaFija.caracter, '' )
                            #guardar dónde hay una fija
                            self.posicionesFijas[ self.posicionDelCambio ] = True
                            self.posicionesValidas[ self.posicionDelCambio ] = True

                        elif(b < self.fijasIntentoAnterior): #lo que se quitó es una fija

                            print("FIJA SE DESCUBRIO")

                            nuevaFija = Tupla( self.posicionDelCambio, self.caracterCambiado )
                            self.fijasDetectadas.append(nuevaFija)
                            #quitarla del alfabeto
                            #self.m_Alphabet = self.m_Alphabet.replace( nuevaFija.caracter, '' )
                            #guardar dónde hay una fija
                            self.posicionesFijas[ self.posicionDelCambio ] = True

                            self.posicionesValidas[ self.posicionDelCambio ] = True

                            listCurrentSolution = list(self.m_CurrentSolution)

                            #descartar lo que se agregó
                            #self.m_Alphabet = self.m_Alphabet.replace( listCurrentSolution[self.posicionDelCambio], '' )

                            #revertir cambio
                            listCurrentSolution[ self.posicionDelCambio ] = self.caracterCambiado
                            self.m_CurrentSolution = ''.join(listCurrentSolution)

                            #volver a colocar la fija que se quitó
                            #listCurrentSolution = list(self.m_CurrentSolution)
                            #listCurrentSolution[ self.posicionUltimoCaracterCambiado ] = nuevaFija.caracter

                            #self.m_CurrentSolution = ''.join(listCurrentSolution)



                    #print(self.posicionesValidas)
                    #print("posicion del cambio: "+str(self.posicionDelCambio))

                    self.cambioFueRealizado = False
                    self.posicionDelCambio = 0
                    self.caracterCambiado = None

                    conta = 0
                    for item in self.posicionesValidas:
                        if (item == True):
                            conta = conta + 1
                    if (conta == len(self.posicionesValidas)):
                        print("se lleno")

                else:
                    #descartar lo que se agregó
                    listCurrentSolution = list(self.m_CurrentSolution)
                    self.m_Alphabet = self.m_Alphabet.replace( listCurrentSolution[self.posicionDelCambio], '' )
                    self.m_Alphabet = self.m_Alphabet.replace( self.caracterCambiado, '' )

            if( (b+c == self.m_GuessSize)  ): #ya están todos los caracteres que se necesitan

                self.cambioFueRealizado = False

                s = copy.deepcopy( list( self.m_Alphabet ) )
                random.shuffle( s )
                self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )

            else: #realizar cambio

                self.cambioFueRealizado = True

                listCurrentSolution = list(self.m_CurrentSolution)

                indice = 0
                #cambiar la primera posición
                s = copy.deepcopy( list( self.m_Alphabet ) )
                random.shuffle( s )
                #while(s[indice] in listCurrentSolution): #para no repetir uno mismo
                #    print("un caracter es: "+s[indice])
                #    indice = indice+1

                if ( self.posicionDelCambio == self.m_GuessSize ):
                    self.posicionDelCambio = 0
                while ( self.posicionesFijas[ self.posicionDelCambio ] == True ):
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

        return self.m_CurrentSolution
