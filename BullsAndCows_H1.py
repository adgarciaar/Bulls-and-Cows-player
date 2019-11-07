## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import copy, random
from BullsAndCowsBasePlayer import *

## *************************************************************************
class BullsAndCows_H1( BullsAndCowsBasePlayer ):

  ## -----------------------------------------------------------------------
  m_CurrentSolution = None

  ## -----------------------------------------------------------------------
  def __init__( self, n, a ):
    BullsAndCowsBasePlayer.__init__( self, n, a )
    self.m_CurrentSolution = ""
  # end def

  ## -----------------------------------------------------------------------
  def guess( self, b, c ):
    if self.m_CurrentSolution != "":
      if b == 0 and c == 0:
        for s in list( self.m_CurrentSolution ):
          self.m_Alphabet = self.m_Alphabet.replace( s, '' )
        # end for
      # end if
    # end if
    s = copy.deepcopy( list( self.m_Alphabet ) )
    random.shuffle( s )
    self.m_CurrentSolution = ''.join( s[ 0: self.m_GuessSize ] )
    return self.m_CurrentSolution
  # end def

# end class

## eof - BullsAndCows_H1.py
