## =========================================================================
## Adrian Garcia, Nicolas Miranda
## =========================================================================

import copy, random
from BullsAndCowsBasePlayer import *

## *************************************************************************
class BullsAndCows_H5( BullsAndCowsBasePlayer ):

  ## -----------------------------------------------------------------------
  def __init__( self, n, a ):
    BullsAndCowsBasePlayer.__init__( self, n, a )
    self.m_CurrentSolution = ""

    self.indice = 0
    self.caracterCambiado = None

    self.picasIntentoAnterior = None
    self.fijasIntentoAnterior = None
  # end def

  ## -----------------------------------------------------------------------
  def guess( self, b, c ):

    if (caracterCambiado != None):
        if (b<self.fijasIntentoAnterior):
            #

    if self.m_CurrentSolution != "":
        if b == 0 and c == 0:
            for s in list( self.m_CurrentSolution ):
                self.m_Alphabet = self.m_Alphabet.replace( s, '' )
        else:
            pass


    s = copy.deepcopy( list( self.m_Alphabet ) )
    random.shuffle( s )
    self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )
    return self.m_CurrentSolution
  # end def

# end class

## eof - BullsAndCows_H1.py
