## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

from BullsAndCowsBasePlayer import *

## *************************************************************************
class InteractiveBullsAndCows( BullsAndCowsBasePlayer ):

  ## -----------------------------------------------------------------------
  def guess( self, b, c ):
    g = input( "Enter your guess: " )
    if len( g ) != self.m_GuessSize:
      print( "Incompatible guess size." )
    # end if
    return g
  # end def

# end class

## eof - InteractiveBullsAndCows.py
