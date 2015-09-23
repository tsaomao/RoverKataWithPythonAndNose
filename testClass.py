from nose.tools import assert_is, assert_is_instance, assert_in, assert_equal
from rover import *

class TestRover:

  def testRoverCreation(self):
    rv = Rover()
    assert_is_instance(rv, Rover) 

  def testRoverInitialValues(self):
    rv = Rover()
    assert_equal(0, rv.positionX)
    assert_equal(0, rv.positionY)
    assert_equal("North", rv.facing)