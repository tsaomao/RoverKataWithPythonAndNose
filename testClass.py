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

  def testRoverMoveForward(self):
    wg1 = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 6)])
    wg2 = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 4)])
    rv = Rover()
    rv.startRover((10, 5), "South")
    assert_equal(False, rv.moveForward(wg2))
    assert_equal(True, rv.moveForward(wg1))
    assert_equal(10, rv.positionX)
    assert_equal(4, rv.positionY)

  def testRoverMoveBackward(self):
    wg1 = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 6)])
    wg2 = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 4)])
    rv = Rover()
    rv.startRover((10, 5), "North")
    assert_equal(False, rv.moveBackward(wg2))
    assert_equal(True, rv.moveBackward(wg1))
    assert_equal(10, rv.positionX)
    assert_equal(4, rv.positionY)

  def testRoverCommands(self):
    wg = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 6)])
    rv = Rover()
    rv.startRover((8, 4), "North")
    resultBool, resultString = rv.parseCommandString("frff", wg)
    assert_equal(True, resultBool)
    assert_equal("Commands successful.", resultString)
    assert_equal(10, rv.positionX)
    assert_equal(5, rv.positionY)
    resultBool, resultString = rv.parseCommandString("lf", wg)
    assert_equal(False, resultBool)
    assert_equal("Commands aborted. Obstacle encountered.", resultString)
    assert_equal(10, rv.positionX)
    assert_equal(5, rv.positionY)

  @raises(CommandValidationError)  
  def testRoverCommandException(self):
    wg = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 6)])
    rv = Rover()
    rv.startRover((8, 4), "North")
    resultBool, resultString = rv.parseCommandString("mff", wg)
    

class TestWorldGrid:

  def testWorldGridCreation(self):
    wg = WorldGrid([(1, 1), (-1, -1), (2, 1)])
    assert_is_instance(wg, WorldGrid) 
    assert_equal([(1, 1), (-1, -1), (2, 1)], wg.obstacleGrid)

  def testIsBlocked(self):
    wg = WorldGrid([(1, 1), (-1, -1), (2, 1)])
    assert_equal(True, wg.isBlocked((-1, -1)))
    assert_equal(False, wg.isBlocked((0, 0)))
    

  
class TestExceptions:

  def testCommandValidationError(self):
    ex = CommandValidationError()
    assert_is_instance(ex, CommandValidationError) 
