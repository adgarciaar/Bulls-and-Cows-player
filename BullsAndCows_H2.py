## =========================================================================
## @authors Adrian Garcia & Nicolas Miranda
## =========================================================================

import copy, random
from BullsAndCowsBasePlayer import *

## *************************************************************************
class BullsAndCows_H0( BullsAndCowsBasePlayer ):

    ## -----------------------------------------------------------------------
    m_parametro = None

    ## -----------------------------------------------------------------------
    def __init__( self, n, a ):
        BullsAndCowsBasePlayer.__init__( self, n, a )
        self.m_CurrentSolution = ""
    # end def

    ## -----------------------------------------------------------------------
    def guess( self, b, c ):
        s = copy.deepcopy( list( self.m_Alphabet ) )
        #random.shuffle( s )
        #return ''.join( s[ 0: self.m_GuessSize ] )
        # end def

# end class

## eof - BullsAndCows_H0.py
