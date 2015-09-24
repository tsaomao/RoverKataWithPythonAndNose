"""Module to implement Rover Kata. See README.md for more information.

To do:
- refactor to validate/raise exception on self.facing not as expected in a central place, probably __init__()"""

class Rover:
  """Rover class to fulfill Rover Kata.
  Tracks positionX, position Y, facing, and possibly other attributes.
  Includes many methods for moving and interacting with the WorldGrid class.

  Assumptions:
    positionX = 0 && positionY = 0 are default origin starting coordinates.
    Grid for position is an arbitrarily large 2 dimensional grid of positive and negative integers.
    Valid facing is one element of ["North", "South", "East", "West"]
    Default start position is (0, 0) and North facing if not stated otherwise."""
  positionX = 0
  positionY = 0
  facing = "North"

  def startRover(self, startingCoords, startingFace):
    """Rover given a startRover() command is moved to specific startingCoords tuple (positionX, positionY) with specified
    startingFace facing. No validation of incoming values here."""
    self.positionX = startingCoords[0]
    self.positionY = startingCoords[1]
    self.facing = startingFace

  def turnRight(self):
    """turnRight() method spins rover clockwise (as seen from above) 90 degrees on each command. Basic validation of
    self.facing values is done here, with an unknown value raising an exception. Probably needs refactoring."""
    if (self.facing == "North"):
      self.facing = "East"
    elif (self.facing == "East"):
      self.facing = "South"
    elif (self.facing == "South"):
      self.facing = "West"
    elif (self.facing == "West"):
      self.facing = "North"
    else:
      raise ValueError('Facing value not in ["North", "South", "East", "West"]')

  def turnLeft(self):
    """turnLeft() method spins rover counter-clockwise (as seen from above) 90 degrees on each command. Basic validation of
    self.facing values is done here, with an unknown value raising an exception. Probably needs refactoring."""
    if (self.facing == "North"):
      self.facing = "West"
    elif (self.facing == "West"):
      self.facing = "South"
    elif (self.facing == "South"):
      self.facing = "East"
    elif (self.facing == "East"):
      self.facing = "North"
    else:
      raise ValueError('Facing value not in ["North", "South", "East", "West"]')

  def moveForward(self, wgInst):
    """moveForward() method projects next block coords, uses the WorldGrid object to validate that this is possible, and,
    depending on the facing, increments or decrements the positionX or positionY attribute by one.

    For purposes of this function these are the increments/decrements for a given facing:
    - North: increment positionY
    - South: decrement positionY
    - East: increment positionX
    - West: decrement positionX

    Takes an instance of WorldGrid for access to the WorldGrid().isBlocked() method."""
    if (self.facing == "North"):
      proposedCoords = (self.positionX, self.positionY + 1)
    elif (self.facing == "South"):
      proposedCoords = (self.positionX, self.positionY - 1)
    elif (self.facing == "East"):
      proposedCoords = (self.positionX + 1, self.positionY)
    elif (self.facing == "West"):
      proposedCoords = (self.positionX - 1, self.positionY)
    else:
      raise ValueError('Facing value not in ["North", "South", "East", "West"]')

    if (wgInst.isBlocked(proposedCoords)):
      # May want to refactor as a custom exception or return value.
      # Also may want to provide more information about obstacle (coords, move-from point, etc)
      print "moveForward() command blocked by obstacle in front of rover."
      return False
    else:
      self.positionX = proposedCoords[0]
      self.positionY = proposedCoords[1]
      return True
    
  def moveBackward(self, wgInst):
    """moveBackwawrd() method projects next block coords, uses the WorldGrid object to validate that this is possible, and,
    depending on the facing, increments or decrements the positionX or positionY attribute by one.

    For purposes of this function these are the increments/decrements for a given facing:
    - North: decrement positionY
    - South: increment positionY
    - East: decrement positionX
    - West: increment positionX

    Takes an instance of WorldGrid for access to the WorldGrid().isBlocked() method."""
    if (self.facing == "North"):
      proposedCoords = (self.positionX, self.positionY - 1)
    elif (self.facing == "South"):
      proposedCoords = (self.positionX, self.positionY + 1)
    elif (self.facing == "East"):
      proposedCoords = (self.positionX - 1, self.positionY)
    elif (self.facing == "West"):
      proposedCoords = (self.positionX + 1, self.positionY)
    else:
      raise ValueError('Facing value not in ["North", "South", "East", "West"]')

    if (wgInst.isBlocked(proposedCoords)):
      # May want to refactor as a custom exception or return value.
      # Also may want to provide more information about obstacle (coords, move-from point, etc)
      print "moveBackward() command blocked by obstacle behind rover."
      return False
    else:
      self.positionX = proposedCoords[0]
      self.positionY = proposedCoords[1]
      return True

  

class WorldGrid:
  """WorldGrid class will return information about the world including whether there exists
  an obstacle at a specified tuple. WorldGrid is 2 dimensional, but may be refactored to other dimensions and/or
  general properties and behavior."""
  obstacleGrid = []

  def __init__(self, obstacles):
    self.obstacleGrid = []
    self.obstacleGrid.extend(obstacles)

  def isBlocked(self, proposedTuple):
    if (proposedTuple in self.obstacleGrid):
      return True
    else:
      return False
