## =========================================================================
## @authors Adrian Garcia & Nicolas Miranda
## =========================================================================

import copy, random
from BullsAndCowsBasePlayer import *

## *************************************************************************
class BullsAndCows_H0( BullsAndCowsBasePlayer ):

    ## -----------------------------------------------------------------------
    m_CurrentSolution = None

    ## -----------------------------------------------------------------------
    def __init__( self, n, a ):
        BullsAndCowsBasePlayer.__init__( self, n, a )
        self.m_CurrentSolution = ""
    # end def

    ## -----------------------------------------------------------------------
    def guess( self, b, c ):
        s = copy.deepcopy( list( self.m_Alphabet ) )

        if (b==0 and c==0):
            for item in list( self.m_CurrentSolution ):
                print("este es uno: "+s)
                #quitar los caracteres que no sirvieron
                self.m_Alphabet = self.m_Alphabet.replace( item, '' )
            random.shuffle( self.m_Alphabet ) #con los caracteres restantes
            self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )

        elif(b == 0 and c > 0): #hay sólo picas
            random.shuflle(self.m_CurrentSolution)

        elif(b > and c == 0): #hay sólo fijas
            pass

        elif(b > 0 and c >0):
            if( b+c == 4 ): #ya están todos los caracteres que se necesitan
                pass #cambiar las posiciones


        return self.m_CurrentSolution
    # end def

# end class

## eof - BullsAndCows_H0.py
