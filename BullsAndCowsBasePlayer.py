## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

## *************************************************************************
class BullsAndCowsBasePlayer:

  # --- Attributes ---
  m_Alphabet = None
  m_GuessSize = 0

  ## -----------------------------------------------------------------------
  def __init__( self, n, a ):
    self.m_Alphabet = a
    self.m_GuessSize = n
  # end def

  ## -----------------------------------------------------------------------
  def guess_size( self ):
    return( self.m_GuessSize )
  # end def

  ## -----------------------------------------------------------------------
  def alphabet( self ):
    return( self.m_Alphabet )
  # end def

  ## -----------------------------------------------------------------------
  def guess( self, b, c ):
    pass
  # end def

# end class

## eof - BullsAndCowsBasePlayer.py
