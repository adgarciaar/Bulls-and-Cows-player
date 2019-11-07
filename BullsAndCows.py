## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import copy, random

## *************************************************************************
class BullsAndCows:

  # --- Attributes ---
  m_Alphabet = ""
  m_Solution = ""

  ## -----------------------------------------------------------------------
  def __init__( self, n, a = "0123456789" ):
    self.m_Alphabet = a
    s = copy.deepcopy( list( self.m_Alphabet ) )
    random.shuffle( s )
    self.m_Solution = ''.join( s[ 0: n ] )
  # end def

  ## -----------------------------------------------------------------------
  def guess_size( self ):
    return len( self.m_Solution )
  # end def

  ## -----------------------------------------------------------------------
  def check( self, guess ):
    if len( guess ) != len( self.m_Solution ):
      return [ 0, 0 ]
    else:
      # Check if guess has repeated elements
      l = list( dict.fromkeys( list( guess ) ) )
      if len( l ) != len( guess ):
        return [ 0, 0 ]
      else:
        m = [ False for i in range( len( self.m_Solution ) ) ]

        # Count bulls (b)
        b = 0
        for i in range( len( self.m_Solution ) ):
          if self.m_Solution[ i ] == guess[ i ]:
            m[ i ] = True
            b += 1
          # end if
        # end for

        # Count cows (c)
        c = 0
        for i in range( len( self.m_Solution ) ):
          for j in range( len( guess ) ):
            if i != j:
              if self.m_Solution[ i ] == guess[ j ] and not m[ i ]:
                c += 1
                m[ i ] = True
              # end if
            # end if
          # end for
        # end for

        # Inform results
        return [ b, c ]
      # end if
  # end def

# end class

## eof - BullsAndCows.py
