## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import copy, random
from BullsAndCowsBasePlayer import *

## *************************************************************************
class BullsAndCows_H0( BullsAndCowsBasePlayer ):

  ## -----------------------------------------------------------------------
  def guess( self, b, c ):
    s = copy.deepcopy( list( self.m_Alphabet ) )
    random.shuffle( s )
    return ''.join( s[ 0: self.m_GuessSize ] )
  # end def

# end class

## eof - BullsAndCows_H0.py
