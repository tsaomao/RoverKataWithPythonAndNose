from nose.tools import assert_is, assert_is_instance, assert_in, assert_equal, raises
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

  def testRoverSetup(self):
    rv = Rover()
    rv.startRover((10, 5), "South")
    assert_equal(10, rv.positionX)
    assert_equal(5, rv.positionY)
    assert_equal("South", rv.facing)

  def testRoverTurnRight(self):
    rv = Rover()
    assert_equal("North", rv.facing)
    rv.turnRight()
    assert_equal("East", rv.facing)
    rv.turnRight()
    assert_equal("South", rv.facing)
    rv.turnRight()
    assert_equal("West", rv.facing)
    rv.turnRight()
    assert_equal("North", rv.facing)

  @raises(ValueError)
  def testRoverTurnRightException(self):
    rv = Rover()
    rv.startRover((10, 5), "Elephant")
    rv.turnRight()
    
  def testRoverTurnLeft(self):
    rv = Rover()
    assert_equal("North", rv.facing)
    rv.turnLeft()
    assert_equal("West", rv.facing)
    rv.turnLeft()
    assert_equal("South", rv.facing)
    rv.turnLeft()
    assert_equal("East", rv.facing)
    rv.turnLeft()
    assert_equal("North", rv.facing)

  @raises(ValueError)
  def testRoverTurnLeftException(self):
    rv = Rover()
    rv.startRover((10, 5), "Elephant")
    rv.turnLeft()
    
