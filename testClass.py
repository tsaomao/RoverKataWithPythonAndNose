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
    assert_equal(100, rv.worldWrapExtents)

  def testRoverSetup(self):
    rv = Rover()
    rv.startRover((10, 5), "South", 100)
    assert_equal(10, rv.positionX)
    assert_equal(5, rv.positionY)
    assert_equal("South", rv.facing)
    assert_equal(100, rv.worldWrapExtents)

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
    rv.startRover((10, 5), "Elephant", 100)
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
    rv.startRover((10, 5), "Elephant", 100)
    rv.turnLeft()

  def testRoverMoveForward(self):
    wg1 = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 6)], 100)
    wg2 = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 4)], 100)
    rv = Rover()
    rv.startRover((10, 5), "South", 100)
    assert_equal(False, rv.moveForward(wg2))
    assert_equal(True, rv.moveForward(wg1))
    assert_equal(10, rv.positionX)
    assert_equal(4, rv.positionY)

  def testRoverMoveBackward(self):
    wg1 = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 6)], 100)
    wg2 = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 4)], 100)
    rv = Rover()
    rv.startRover((10, 5), "North", 100)
    assert_equal(False, rv.moveBackward(wg2))
    assert_equal(True, rv.moveBackward(wg1))
    assert_equal(10, rv.positionX)
    assert_equal(4, rv.positionY)

  def testRoverWorldWrapSimple(self):
    wg = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 6), (1, 100), (2, -100), (100, 1), (-100, 2)], 100)
    rv = Rover()
    rv.startRover((1, -100), "South", 100)
    assert_equal(False, rv.moveForward(wg))
    assert_equal(True, rv.moveBackward(wg))
    rv.startRover((1, -100), "North", 100)
    assert_equal(False, rv.moveBackward(wg))
    assert_equal(True, rv.moveForward(wg))
    rv.startRover((2, 100), "North", 100)
    assert_equal(False, rv.moveForward(wg))
    assert_equal(True, rv.moveBackward(wg))
    rv.startRover((2, 100), "South", 100)
    assert_equal(False, rv.moveBackward(wg))
    assert_equal(True, rv.moveForward(wg))
    rv.startRover((-100, 1), "West", 100)
    assert_equal(False, rv.moveForward(wg))
    assert_equal(True, rv.moveBackward(wg))
    rv.startRover((-100, 1), "East", 100)
    assert_equal(False, rv.moveBackward(wg))
    assert_equal(True, rv.moveForward(wg))
    rv.startRover((100, 2), "East", 100)
    assert_equal(False, rv.moveForward(wg))
    assert_equal(True, rv.moveBackward(wg))

  def testRoverWorldWrapCommandString(self):
    wg = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 6), (1, 100), (2, -100), (100, 1), (-100, 2)], 100)
    rv = Rover()
    rv.startRover((1, -98), "East", 100)
    #s/b at (4, 100), facing South
    resultBool, resultString = rv.parseCommandString("fffrfff", wg)
    assert_equal(True, resultBool)
    assert_equal("Commands successful.", resultString)
    assert_equal(4, rv.positionX)
    assert_equal(100, rv.positionY)
    assert_equal("South", rv.facing)
    #s/b (1, -100), facing South, hit obstacle at (1, 100)
    rv.startRover((1, -98), "East", 100)
    resultBool, resultString = rv.parseCommandString("rfff", wg)
    assert_equal(False, resultBool)
    assert_equal("Commands aborted. Obstacle encountered.", resultString)
    assert_equal(1, rv.positionX)
    assert_equal(-100, rv.positionY)
    assert_equal("South", rv.facing)

  def testRoverCommands(self):
    wg = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 6)], 100)
    rv = Rover()
    rv.startRover((8, 4), "North", 100)
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
    rv.startRover((8, 4), "North", 100)
    resultBool, resultString = rv.parseCommandString("frfflf", wg)
    assert_equal(False, resultBool)
    assert_equal("Commands aborted. Obstacle encountered.", resultString)
    assert_equal(10, rv.positionX)
    assert_equal(5, rv.positionY)
    

  @raises(CommandValidationError)  
  def testRoverCommandException(self):
    wg = WorldGrid([(1, 1), (-1, -1), (2, 1), (10, 6)], 100)
    rv = Rover()
    rv.startRover((8, 4), "North", 100)
    resultBool, resultString = rv.parseCommandString("mff", wg)
    

class TestWorldGrid:

  def testWorldGridCreation(self):
    wg = WorldGrid([(1, 1), (-1, -1), (2, 1)], 100)
    assert_is_instance(wg, WorldGrid)
    assert_equal([(1, 1), (-1, -1), (2, 1)], wg.obstacleGrid)
    assert_equal(100, wg.worldWrapExtents)
    

  def testIsBlocked(self):
    wg = WorldGrid([(1, 1), (-1, -1), (2, 1)], 100)
    assert_equal(True, wg.isBlocked((-1, -1)))
    assert_equal(False, wg.isBlocked((0, 0)))

  def testWorldWrap(self):
    wg = WorldGrid([(1, 100), (2, -100), (100, 1), (-100, 2)], 100)
    assert_equal(True, wg.isBlocked((1, -101)))
    assert_equal(True, wg.isBlocked((2, 101)))
    assert_equal(True, wg.isBlocked((-101, 1)))
    assert_equal(True, wg.isBlocked((101, 2)))
    assert_equal(False, wg.isBlocked((5, -101)))
    assert_equal(False, wg.isBlocked((5, 101)))
    assert_equal(False, wg.isBlocked((-101, 5)))
    assert_equal(False, wg.isBlocked((101, 5)))

  
class TestExceptions:

  def testCommandValidationError(self):
    ex = CommandValidationError()
    assert_is_instance(ex, CommandValidationError) 
