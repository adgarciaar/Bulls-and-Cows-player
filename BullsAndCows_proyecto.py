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

    ## -----------------------------------------------------------------------
    def guess( self, b, c ):

        if self.m_CurrentSolution == "":
            s = copy.deepcopy( list( self.m_Alphabet ) )
            random.shuffle( s )
            self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )
            return self.m_CurrentSolution

        time.sleep(0.3)
        #print("Current solution "+self.m_CurrentSolution+"\n")

        if(self.cambioFueRealizado == True):

            if( b !=  self.fijasIntentoAnterior or c != self.picasIntentoAnterior):

                #hubo un cambio que nos interesa

                self.posicionDelCambio = self.posicionDelCambio-1

                if(b > self.fijasIntentoAnterior): #lo que se agregó es una fija

                    nuevaFija = Tupla( self.posicionDelCambio, self.m_CurrentSolution[self.posicionDelCambio] )
                    self.fijasDetectadas.append(nuevaFija)

                    #guardar dónde hay una fija
                    self.posicionesFijas[ self.posicionDelCambio ] = True
                    self.posicionesValidas[ self.posicionDelCambio ] = True

                elif(b < self.fijasIntentoAnterior): #lo que se quitó es una fija

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

                elif(c > self.picasIntentoAnterior): #lo que se agregó es una pica

                    nuevaPica = Tupla( self.posicionDelCambio, self.m_CurrentSolution[self.posicionDelCambio] )
                    self.picasDetectadas.append(nuevaPica)

                    self.posicionesValidas[ self.posicionDelCambio ] = True

                elif(c < self.picasIntentoAnterior): #lo que se quitó es una pica

                    nuevaPica = Tupla( self.posicionDelCambio, self.caracterCambiado )
                    self.picasDetectadas.append(nuevaPica)

                    self.posicionesValidas[ self.posicionDelCambio ] = True

                    listCurrentSolution = list(self.m_CurrentSolution)

                    #descartar lo que se agregó
                    #self.m_Alphabet = self.m_Alphabet.replace( listCurrentSolution[self.posicionDelCambio], '' )

                    #revertir cambio
                    listCurrentSolution[ self.posicionDelCambio ] = self.caracterCambiado
                    self.m_CurrentSolution = ''.join(listCurrentSolution)

                self.cambioFueRealizado = False
                self.posicionDelCambio = 0
                self.caracterCambiado = None

        if (b==0 and c==0): #descartar del alfabeto todos los caracteres que no van

            self.cambioFueRealizado = False

            for item in list( self.m_CurrentSolution ):
                #print("este es uno que muere: "+item)
                #quitar los caracteres que no sirvieron
                self.m_Alphabet = self.m_Alphabet.replace( item, '' )
            s = copy.deepcopy( list( self.m_Alphabet ) )
            random.shuffle( s )
            self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )

        elif( b+c == self.m_GuessSize ): #ya están todos los caracteres que se necesitan

            self.cambioFueRealizado = False

            #self.m_Alphabet = self.m_CurrentSolution
            #s = copy.deepcopy( list( self.m_Alphabet ) )
            #random.shuffle( s )
            #self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )

            if (self.picaDentroDeSolucion == False):

                while(self.posicionesFijas[self.primeraPica] == True):
                    self.primeraPica = self.primeraPica + 1

                self.siguientePica = self.primeraPica+1
                while(self.posicionesFijas[self.siguientePica] == True):
                    self.siguientePica = self.siguientePica + 1
                    if(self.siguientePica == len(self.posicionesFijas)):
                        self.siguientePica = 0

                #hacer un cambio
                listCurrentSolution = list(self.m_CurrentSolution)
                self.picaTemporal = self.m_CurrentSolution[ self.siguientePica ]
                #self.ultimoCaracterCambiado = listCurrentSolution[ self.siguientePica ]
                listCurrentSolution[ self.siguientePica ] = self.m_CurrentSolution[self.primeraPica]
                listCurrentSolution[ self.primeraPica ] = self.picaTemporal

                self.m_CurrentSolution = ''.join(listCurrentSolution)

                self.picaDentroDeSolucion = True

            else:
                if (b > self.fijasIntentoAnterior):

                    if(b == self.fijasIntentoAnterior+1): #se ganó una fija

                        nuevaFija = Tupla( self.siguientePica, self.m_CurrentSolution[self.siguientePica] )
                        self.fijasDetectadas.append(nuevaFija)

                        #guardar dónde hay una fija
                        self.posicionesFijas[ self.siguientePica ] = True

                    elif(b == self.fijasIntentoAnterior+2):

                        nuevaFija = Tupla( self.siguientePica, self.m_CurrentSolution[self.siguientePica] )
                        self.fijasDetectadas.append(nuevaFija)
                        self.posicionesFijas[ self.siguientePica ] = True

                        nuevaFija = Tupla( self.primeraPica, self.m_CurrentSolution[self.primeraPica] )
                        self.fijasDetectadas.append(nuevaFija)
                        self.posicionesFijas[ self.primeraPica ] = True

                    self.primeraPica = 0
                    self.siguientePica = 0
                    self.picaTemporal = None
                    self.picaDentroDeSolucion = False

                #else:
                self.primeraPica = self.siguientePica

                self.siguientePica = self.primeraPica+1
                while(self.posicionesFijas[self.siguientePica] == True): #problema acá con índice
                    self.siguientePica = self.siguientePica + 1
                    if(self.siguientePica == len(self.posicionesFijas)):
                        self.siguientePica = 0

                    #hacer un cambio
                listCurrentSolution = list(self.m_CurrentSolution)
                self.picaTemporal = self.m_CurrentSolution[ self.siguientePica ]
                    #self.ultimoCaracterCambiado = listCurrentSolution[ self.siguientePica ]
                listCurrentSolution[ self.siguientePica ] = self.m_CurrentSolution[self.primeraPica]
                listCurrentSolution[ self.primeraPica ] = self.picaTemporal

                self.m_CurrentSolution = ''.join(listCurrentSolution)

        else:
            self.cambioFueRealizado = True

            listCurrentSolution = list(self.m_CurrentSolution)

            indice = 0
            s = copy.deepcopy( list( self.m_Alphabet ) )
            random.shuffle( s )
            while(s[indice] in listCurrentSolution): #para no repetir uno mismo
                indice = indice+1

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
