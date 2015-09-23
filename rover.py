"""Module to implement Rover Kata. See README.md for more information."""

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
