## =========================================================================
## @authors Adrian Garcia & Nicolas Miranda
## =========================================================================

import copy, random
from BullsAndCowsBasePlayer import *

class Tupla:
    def __init__(self, posicion, caracter):
        self.posicion = posicion
        self.caracter = caracter

## *************************************************************************
class BullsAndCows_H2( BullsAndCowsBasePlayer ):

    ## -----------------------------------------------------------------------
    m_CurrentSolution = None

    fijasDetectadas = None
    picasDetectadas = None

    ultimoCaracterCambiado = None
    posicionUltimoCaracterCambiado = None

    fijasIntentoAnterior = None
    picasIntentoAnterior = None

    cambioFueRealizado = None

    posicionesFijas = None

    picaRecienDetectada = None
    picaFueDetectada = None
    ultimaPosicionPica = None

    ## -----------------------------------------------------------------------
    def __init__( self, n, a ):
        BullsAndCowsBasePlayer.__init__( self, n, a )
        self.m_CurrentSolution = ""
        self.fijasDetectadas = []
        self.picasDetectadas = []
        self.posicionUltimoCaracterCambiado = 0
        self.cambioFueRealizado = False
        self.posicionesFijas = []
        for i in range (0, n):
            self.posicionesFijas.append(False)
        self.picaRecienDetectada = None
        self.picaFueDetectada = False
        self.ultimaPosicionPica = 0
        self.ultimoCaracterCambiado = None
    # end def

    ## -----------------------------------------------------------------------
    def guess( self, b, c ):

        print("Current solution "+self.m_CurrentSolution+"\n")

        if(self.picaFueDetectada == True): #continuar cambiandola de lugar
            if( b > self.fijasIntentoAnterior ): #la pica se convirtió en fija
                self.picaFueDetectada = False
                self.ultimaPosicionPica = 0
                self.picaRecienDetectada = None

            else: #cambiar la pica a la siguiente posición

                #reestablecer lo que se cambió
                listCurrentSolution[ self.ultimaPosicionPica ] = self.ultimoCaracterCambiado

                s = copy.deepcopy( list( self.m_Alphabet ) )
                random.shuffle( s )

                while(self.posicionesFijas[self.ultimaPosicionPica] == True):
                    self.ultimaPosicionPica = self.ultimaPosicionPica + 1

                #hacer un cambio
                listCurrentSolution = list(self.m_Alphabet)
                self.ultimoCaracterCambiado = listCurrentSolution[ self.ultimaPosicionPica ]
                listCurrentSolution[ self.ultimaPosicionPica ] = s[0]

                print("Va a cambiar "+self.m_CurrentSolution[self.ultimaPosicionPica]+"\n")
                #self.m_CurrentSolution[self.posicionUltimoCaracterCambiado+1] = s[ 0: 1 ]
                print("Por "+s[0])
                #print(s[0])

                self.m_CurrentSolution = ''.join(listCurrentSolution)

        else:

            if(self.cambioFueRealizado == True): #se hizo un cambio en el turno anterior

                #si se mantuvo igual volver a cambiar la posición siguiente
                if(self.fijasIntentoAnterior == b and self.picasIntentoAnterior == c):

                    #reestablecer lo que se cambió
                    listCurrentSolution[ self.posicionUltimoCaracterCambiado ] = self.ultimoCaracterCambiado

                    while(self.posicionesFijas[self.posicionUltimoCaracterCambiado] == True):
                        self.posicionUltimoCaracterCambiado = self.posicionUltimoCaracterCambiado + 1

                    #cambiar otra vez por la posición siguiente
                    s = copy.deepcopy( list( self.m_Alphabet ) )
                    random.shuffle( s )

                    #hacer un cambio
                    listCurrentSolution = list(self.m_Alphabet)
                    self.ultimoCaracterCambiado = listCurrentSolution[ self.posicionUltimoCaracterCambiado ]
                    listCurrentSolution[ self.posicionUltimoCaracterCambiado ] = s[0]

                    print("Va a cambiar "+self.m_CurrentSolution[self.posicionUltimoCaracterCambiado]+"\n")
                    #self.m_CurrentSolution[self.posicionUltimoCaracterCambiado+1] = s[ 0: 1 ]
                    print("Por "+s[0])
                    #print(s[0])

                    self.m_CurrentSolution = ''.join(listCurrentSolution)

                else: #hubo un cambio que nos interesa

                    self.cambioFueRealizado = False

                    if(c > self.picasIntentoAnterior): #lo que se agregó es una pica
                        nuevaPica = Tupla( self.posicionUltimoCaracterCambiado, self.m_CurrentSolution[self.posicionUltimoCaracterCambiado] )
                        self.picasDetectadas.append(nuevaPica)
                        #quitarla del alfabeto
                        #self.m_Alphabet = self.m_Alphabet.replace( nuevaPica.caracter, '' )
                        self.picaFueDetectada = True
                        self.ultimaPosicionPica = 0
                        self.picaRecienDetectada = nuevaPica.caracter

                    elif(b > fijasIntentoAnterior): #lo que se agregó una fija
                        nuevaFija = Tupla( self.posicionUltimoCaracterCambiado, self.m_CurrentSolution[self.posicionUltimoCaracterCambiado] )
                        self.fijasDetectadas.append(nuevaFija)
                        #quitarla del alfabeto
                        #self.m_Alphabet = self.m_Alphabet.replace( nuevaFija.caracter, '' )
                        #guardar dónde hay una fija
                        self.posicionesFijas[ self.posicionUltimoCaracterCambiado ] = True

                    elif(c < picasIntentoAnterior): #lo que se quitó es una fija
                        nuevaPica = Tupla( self.posicionUltimoCaracterCambiado, self.ultimoCaracterCambiado )
                        self.fijasDetectadas.append(nuevaPica)
                        #quitarla del alfabeto
                        #self.m_Alphabet = self.m_Alphabet.replace( nuevaPica.caracter, '' )
                        self.picaFueDetectada = True
                        self.ultimaPosicionPica = 0
                        self.picaRecienDetectada = nuevaPica.caracter

                    elif(b < fijasIntentoAnterior): #lo que se quitó es una fija
                        nuevaFija = Tupla( self.posicionUltimoCaracterCambiado, self.ultimoCaracterCambiado )
                        self.fijasDetectadas.append(nuevaFija)
                        #quitarla del alfabeto
                        #self.m_Alphabet = self.m_Alphabet.replace( nuevaFija.caracter, '' )
                        #guardar dónde hay una fija
                        self.posicionesFijas[ self.posicionUltimoCaracterCambiado ] = True

                    self.posicionUltimoCaracterCambiado = 0 #para en la siguiente ocasión arrancar en 0

            else: #no se ha hecho cambio en el anterior turno

                if (b==0 and c==0): #descartar del alfabeto todos los caracteres que no van

                    for item in list( self.m_CurrentSolution ):
                        #print("este es uno que muere: "+item)
                        #quitar los caracteres que no sirvieron
                        self.m_Alphabet = self.m_Alphabet.replace( item, '' )
                    s = copy.deepcopy( list( self.m_Alphabet ) )
                    random.shuffle( s )
                    self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )

                elif( b+c == self.m_GuessSize ): #ya están todos los caracteres que se necesitan

                    s = copy.deepcopy( list( self.m_Alphabet ) )
                    random.shuffle( s )
                    self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )
                    #return self.m_CurrentSolution
                    #for i in range (0, self.m_GuessSize):
                    #    if ( posicionesParaCambio[i] == False ):

                else: #averiguar picas o fijas
                    self.cambioFueRealizado = True

                    #cambiar la primera posición
                    s = copy.deepcopy( list( self.m_Alphabet ) )
                    random.shuffle( s )

                    #hacer un cambio
                    listCurrentSolution = list(self.m_Alphabet)

                    self.ultimoCaracterCambiado = listCurrentSolution[ self.posicionUltimoCaracterCambiado ]

                    listCurrentSolution[ self.posicionUltimoCaracterCambiado ] = s[0]

                    print("Va a cambiar "+self.m_CurrentSolution[self.posicionUltimoCaracterCambiado]+"\n")
                    #self.m_CurrentSolution[self.posicionUltimoCaracterCambiado+1] = s[ 0: 1 ]
                    print("Por "+s[0])

                    self.m_CurrentSolution = ''.join(listCurrentSolution)


        self.fijasIntentoAnterior = b
        self.picasIntentoAnterior = c

        return self.m_CurrentSolution

    # end def

# end class

## eof - BullsAndCows_H0.py
