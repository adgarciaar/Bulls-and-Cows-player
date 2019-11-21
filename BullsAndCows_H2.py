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
    posicionInicialPicaDetectada = None

    primeraVezTodosCaracteres = None

    primeraPica = None
    siguientePica = None
    picaTemporal = None

    picaDentroDeSolucion = None

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
        self.posicionInicialPicaDetectada = None
        self.ultimoCaracterCambiado = None

        self.primeraPica = 0
        self.siguientePica = 0
        self.picaTemporal = None
        self.picaDentroDeSolucion = False

        estanTodosLosCaracteres = False

    # end def

    ## -----------------------------------------------------------------------
    def guess( self, b, c ):

        if self.m_CurrentSolution == "":
            s = copy.deepcopy( list( self.m_Alphabet ) )
            random.shuffle( s )
            self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )
            return self.m_CurrentSolution

        #time.sleep(2.0)

        print("Current solution "+self.m_CurrentSolution+"\n")

        if(self.picaFueDetectada == True): #continuar cambiandola de lugar

            print("PICA DETECTADA FLAG")

            if( b > self.fijasIntentoAnterior ): #la pica se convirtió en fija
                self.picaFueDetectada = False
                self.ultimaPosicionPica = 0
                self.picaRecienDetectada = None
                self.posicionInicialPicaDetectada = None

            else: #cambiar la pica a la siguiente posición

                #reestablecer lo que se cambió
                #listCurrentSolution[ self.ultimaPosicionPica ] = self.ultimoCaracterCambiado
                listCurrentSolution = list(self.m_CurrentSolution)
                listCurrentSolution[ self.ultimaPosicionPica ] = self.ultimoCaracterCambiado
                self.m_CurrentSolution = ''.join(listCurrentSolution)
                #self.m_CurrentSolution[ self.ultimaPosicionPica ] = self.ultimoCaracterCambiado

                #s = copy.deepcopy( list( self.m_Alphabet ) )
                #random.shuffle( s )

                #mientras la posición sea una fija o sea la posición donde ya estaba la fija entonces aumentar en 1 la posición
                while(self.posicionesFijas[self.ultimaPosicionPica] == True or self.posicionInicialPicaDetectada == self.ultimaPosicionPica):
                    self.ultimaPosicionPica = self.ultimaPosicionPica + 1

                #hacer un cambio
                listCurrentSolution = list(self.m_CurrentSolution)
                self.ultimoCaracterCambiado = listCurrentSolution[ self.ultimaPosicionPica ]
                #listCurrentSolution[ self.ultimaPosicionPica ] = s[0]
                listCurrentSolution[ self.ultimaPosicionPica ] = self.picaRecienDetectada



                self.m_CurrentSolution = ''.join(listCurrentSolution)

        else:

            if(self.cambioFueRealizado == True): #se hizo un cambio en el turno anterior

                print("CAMBIO REALIZADO")

                #si se mantuvo igual volver a cambiar la posición siguiente
                if(self.fijasIntentoAnterior == b and self.picasIntentoAnterior == c):

                    #reestablecer lo que se cambió
                    #listCurrentSolution[ self.posicionUltimoCaracterCambiado ] = self.ultimoCaracterCambiado
                    listCurrentSolution = list(self.m_CurrentSolution)
                    listCurrentSolution[ self.posicionUltimoCaracterCambiado ] = self.ultimoCaracterCambiado
                    self.m_CurrentSolution = ''.join(listCurrentSolution)
                    #self.m_CurrentSolution[ self.posicionUltimoCaracterCambiado ] = self.ultimoCaracterCambiado

                    while(self.posicionesFijas[self.posicionUltimoCaracterCambiado] == True):
                        self.posicionUltimoCaracterCambiado = self.posicionUltimoCaracterCambiado + 1

                    listCurrentSolution = list(self.m_CurrentSolution)
                    indice = 0
                    #cambiar otra vez por la posición siguiente
                    s = copy.deepcopy( list( self.m_Alphabet ) )
                    random.shuffle( s )
                    while(s[indice] in listCurrentSolution):
                        indice = indice+1

                    #hacer un cambio
                    listCurrentSolution = list(self.m_CurrentSolution)
                    self.ultimoCaracterCambiado = listCurrentSolution[ self.posicionUltimoCaracterCambiado ]
                    listCurrentSolution[ self.posicionUltimoCaracterCambiado ] = s[indice]

                    print("Va a cambiar "+self.m_CurrentSolution[self.posicionUltimoCaracterCambiado]+"\n")
                    #self.m_CurrentSolution[self.posicionUltimoCaracterCambiado+1] = s[ 0: 1 ]
                    print("Por "+s[indice])
                    #print(s[0])

                    self.m_CurrentSolution = ''.join(listCurrentSolution)

                else: #hubo un cambio que nos interesa

                    self.cambioFueRealizado = False

                    if(c > self.picasIntentoAnterior): #lo que se agregó es una pica

                        print("PICA SE DESCUBRIO")

                        nuevaPica = Tupla( self.posicionUltimoCaracterCambiado, self.m_CurrentSolution[self.posicionUltimoCaracterCambiado] )
                        self.picasDetectadas.append(nuevaPica)
                        #quitarla del alfabeto
                        #self.m_Alphabet = self.m_Alphabet.replace( nuevaPica.caracter, '' )
                        self.picaFueDetectada = True
                        self.ultimaPosicionPica = 0
                        self.picaRecienDetectada = nuevaPica.caracter
                        #guardar la posición de la pica detectada para adelante no volver a ponerla ahí
                        self.posicionInicialPicaDetectada = self.posicionUltimoCaracterCambiado

                        #hacer un cambio
                        listCurrentSolution = list(self.m_CurrentSolution)
                        self.ultimoCaracterCambiado = listCurrentSolution[ self.ultimaPosicionPica ]
                        #listCurrentSolution[ self.ultimaPosicionPica ] = s[0]
                        listCurrentSolution[ self.ultimaPosicionPica ] = self.picaRecienDetectada

                        self.m_CurrentSolution = ''.join(listCurrentSolution)

                    elif(b > self.fijasIntentoAnterior): #lo que se agregó una fija

                        print("FIJA SE DESCUBRIO")

                        nuevaFija = Tupla( self.posicionUltimoCaracterCambiado, self.m_CurrentSolution[self.posicionUltimoCaracterCambiado] )
                        self.fijasDetectadas.append(nuevaFija)
                        #quitarla del alfabeto
                        #self.m_Alphabet = self.m_Alphabet.replace( nuevaFija.caracter, '' )
                        #guardar dónde hay una fija
                        self.posicionesFijas[ self.posicionUltimoCaracterCambiado ] = True

                    elif(c < self.picasIntentoAnterior): #lo que se quitó es una pica

                        print("PICA SE DESCUBRIO")

                        nuevaPica = Tupla( self.posicionUltimoCaracterCambiado, self.ultimoCaracterCambiado )
                        self.fijasDetectadas.append(nuevaPica)
                        #quitarla del alfabeto
                        #self.m_Alphabet = self.m_Alphabet.replace( nuevaPica.caracter, '' )
                        self.picaFueDetectada = True
                        self.ultimaPosicionPica = 0
                        self.picaRecienDetectada = nuevaPica.caracter
                        #guardar la posición de la pica detectada para adelante no volver a ponerla ahí
                        self.posicionInicialPicaDetectada = self.posicionUltimoCaracterCambiado

                    elif(b < self.fijasIntentoAnterior): #lo que se quitó es una fija

                        print("FIJA SE DESCUBRIO")

                        nuevaFija = Tupla( self.posicionUltimoCaracterCambiado, self.ultimoCaracterCambiado )
                        self.fijasDetectadas.append(nuevaFija)
                        #quitarla del alfabeto
                        #self.m_Alphabet = self.m_Alphabet.replace( nuevaFija.caracter, '' )
                        #guardar dónde hay una fija
                        self.posicionesFijas[ self.posicionUltimoCaracterCambiado ] = True

                        #volver a colocar la fija que se quitó
                        listCurrentSolution = list(self.m_CurrentSolution)
                        listCurrentSolution[ self.posicionUltimoCaracterCambiado ] = nuevaFija.caracter

                        self.m_CurrentSolution = ''.join(listCurrentSolution)

                    self.posicionUltimoCaracterCambiado = 0 #para en la siguiente ocasión arrancar en 0

            else: #no se ha hecho cambio en el anterior turno

                if (b==0 and c==0): #descartar del alfabeto todos los caracteres que no van

                    print("DESCARTAR TODAS")

                    for item in list( self.m_CurrentSolution ):
                        #print("este es uno que muere: "+item)
                        #quitar los caracteres que no sirvieron
                        self.m_Alphabet = self.m_Alphabet.replace( item, '' )
                    s = copy.deepcopy( list( self.m_Alphabet ) )
                    random.shuffle( s )
                    self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )

                elif( b+c == self.m_GuessSize ): #ya están todos los caracteres que se necesitan

                    print("YA ESTAN TODAS")

                    if (self.picaDentroDeSolucion == False):

                        while(self.posicionesFijas[self.primeraPica] == True):
                            self.primeraPica = self.primeraPica + 1

                        self.siguientePica = self.primeraPica+1
                        while(self.posicionesFijas[self.siguientePica] == True):
                            self.siguientePica = self.siguientePica + 1

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
                                #quitarla del alfabeto
                                #self.m_Alphabet = self.m_Alphabet.replace( nuevaFija.caracter, '' )
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

                        elif (b < self.fijasIntentoAnterior):

                            if(b == self.fijasIntentoAnterior-1):
                                pass
                            elif(b == self.fijasIntentoAnterior-2):
                                pass

                        #else:
                        self.primeraPica = self.siguientePica

                        self.siguientePica = self.primeraPica+1
                        while(self.posicionesFijas[self.siguientePica] == True): #problema acá con índice
                            self.siguientePica = self.siguientePica + 1

                            #hacer un cambio
                        listCurrentSolution = list(self.m_CurrentSolution)
                        self.picaTemporal = self.m_CurrentSolution[ self.siguientePica ]
                            #self.ultimoCaracterCambiado = listCurrentSolution[ self.siguientePica ]
                        listCurrentSolution[ self.siguientePica ] = self.m_CurrentSolution[self.primeraPica]
                        listCurrentSolution[ self.primeraPica ] = self.picaTemporal

                        self.m_CurrentSolution = ''.join(listCurrentSolution)


                    #s = copy.deepcopy( list( self.m_Alphabet ) )
                    #random.shuffle( s )
                    #self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )
                    #return self.m_CurrentSolution
                    #for i in range (0, self.m_GuessSize):
                    #    if ( posicionesParaCambio[i] == False ):

                    #primeraVezTodosCaracteres = True

                else: #averiguar picas o fijas

                    print("HACER CAMBIO")

                    self.cambioFueRealizado = True

                    listCurrentSolution = list(self.m_CurrentSolution)

                    indice = 0
                    #cambiar la primera posición
                    s = copy.deepcopy( list( self.m_Alphabet ) )
                    random.shuffle( s )
                    while(s[indice] in listCurrentSolution):
                        indice = indice+1

                    #hacer un cambio
                    listCurrentSolution = list(self.m_CurrentSolution)

                    self.ultimoCaracterCambiado = listCurrentSolution[ self.posicionUltimoCaracterCambiado ]

                    listCurrentSolution[ self.posicionUltimoCaracterCambiado ] = s[indice]

                    print("Va a cambiar "+self.m_CurrentSolution[self.posicionUltimoCaracterCambiado]+"\n")
                    #self.m_CurrentSolution[self.posicionUltimoCaracterCambiado+1] = s[ 0: 1 ]
                    print("Por "+s[indice])

                    self.m_CurrentSolution = ''.join(listCurrentSolution)


        self.fijasIntentoAnterior = b
        self.picasIntentoAnterior = c

        return self.m_CurrentSolution

    # end def

# end class

## eof - BullsAndCows_H0.py
