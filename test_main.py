import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_exists(self) : 
        self.assertTrue( "dmin" in globals(), "The variable dmin is not defined" )
        self.assertTrue( "lowq" in globals(), "The variable lowq is not defined" )
        self.assertTrue( "median" in globals(), "The variable median is not defined" )
        self.assertTrue( "highq" in globals(), "The variable highq is not defined" )
        self.assertTrue( "dmax" in globals(), "The variable dmax is not defined" )
        
   def test_values(self) : 
       x.sort()
       self.assertTrue( x[0]==dmin, "dmin has not been calculated correctly" )
       self.assertTrue( x[len(x)-1]==dmax, "dmax has not been calculated correctly" )
       self.assertTrue( np.abs( np.percentile( x, 25 ) - lowq ) < 1e-7, "lowq has not been calculated correctly" )
       self.assertTrue( np.abs( np.percentile( x, 50) - median ) < 1e-7, "median has not been calculated correctly" )
       self.assertTrue( np.abs( np.percentile(x, 75 ) - highq ) < 1e-7, "highq has not been calculated correctly" )
