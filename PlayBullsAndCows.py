## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import importlib, math, sys, time
import BullsAndCows

## *************************************************************************
class PlayBullsAndCows:

  # --- Attributes ---
  m_Game = None
  m_Solver = None

  ## -----------------------------------------------------------------------
  def __init__( self, s ):
    self.m_Solver = s
    self.m_Game = BullsAndCows.BullsAndCows(
      self.m_Solver.guess_size( ), self.m_Solver.alphabet( )
      )
    #self.m_Solver = ( n, a )
  # end def

  ## -----------------------------------------------------------------------
  def play( self ):
    nTry = 1
    g = self.m_Solver.guess( 0, 0 )
    [ b, c ] = self.m_Game.check( g )
    t1 = 0
    t2 = 0
    while b < self.m_Game.guess_size( ):
      print( "Try:", nTry, " --->  Bulls:", b, "Cows:", c )
      s_time = time.time( )
      g = self.m_Solver.guess( b, c )
      v_time = float( time.time( ) - s_time )
      t1 += v_time
      t2 += v_time * v_time
      [ b, c ] = self.m_Game.check( g )
      nTry += 1
    # end while
    print( "Try:", nTry, " --->  Bulls:", b, "Cows:", c )
    print( "----------------------------------" )
    print( "---> Solution:", g, "<---" )
    print( "----------------------------------" )
    return [
      nTry,
      t1 / float( nTry ),
      math.sqrt( ( t2 - ( ( t1 * t1 ) / float( nTry ) ) ) / float( nTry ) )
      ]
  # end def

# end class

## *************
## *** main ****
## *************

# Command line arguments
guess_size = int( sys.argv[ 1 ] )
alphabet = sys.argv[ 2 ]
lib_name = sys.argv[ 3 ]
class_name = sys.argv[ 4 ]

# Load library and create a class
solver_module = importlib.import_module( lib_name )
class_module = getattr( solver_module, class_name )
solver = class_module( guess_size, alphabet )

# Create game
game = PlayBullsAndCows( solver )

# Play!
[ nGuesses, avg_time, std_time ] = game.play( )

# Show results
print( "****************************************************" )
print( "* Number of guesses: %d" % nGuesses )
print( "* AVG solving time : %10.4E seconds" % avg_time )
print( "* STD solving time : %10.4E seconds" % std_time )
print( "****************************************************" )

## eof - PlayBullsAndCows.py
