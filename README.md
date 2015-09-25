#Status

I consider the first pass here complete. This project meets the requirements set in the original problem statement.

There is a somewhat interesting problem in designing the most efficient and most understandable division of labor between the Rover() and WorldGrid() classes in tracking the Rover()'s position.

For now there's a hybrid approach, where each handles its own interactions with and tracks its own perception of the rover's position. If I want to follow true OOP design, I should condense it to the WorldGrid() class. But this increases inter-object chattiness and, I think, is in some ways harder to read. The weird thing about my current approach is that Rover position in the WorldGrid() class is essentially stateless, which makes it easier for WorldGrid() to do its thing, but does not really follow OOP protocol. On the other hand, philosophically, there's evidence in the real world that perception does not equal fact, so it's possible that having the rover and the worldgrid track the rover independently is more realistic. :)

Anyhow, there are some other minor things to refactor as well (see "Still to do" below), but I consider them minor. A kata is to practice doing things a certain way, and this kata is especially for doing Test Driven Development with Python and the nose testing framework. It's not for demonstrating strict OOP principles.

#Approach and Strategy notes:

Goal for me is not only to program this kata in Python but also to apply test-driven development principles as well as good source control and commenting hygeine, so as I code the classes, 
methods and attributes, I will also code unit tests and write comments meant both for internal use and for Python docstrings. And finally, I will do frequent commits and pushes of these 
code, testing and documentation assets.

##Still to do:
- Implement validation for values in world grid against world extents
- Consider refactoring so the world grid specifically contains and tracks the Rover object's position
- Refactor to validate/raise exception on self.facing not as expected in a central place, probably __init__()
- Refactor so that only the WorldGrid stores extents/wraparound information

#Original Problem statement:
From http://amirrajan.net/Blog/code-katas-mars-rover

- Develop an api that moves a rover around a grid.
- You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
- The rover receives a character array of commands.
- Implement commands that move the rover forward/backward (f,b).
- Implement commands that turn the rover left/right (l,r).
- The only commands you can give the rover are f,b,l, and r.
- Implement wrapping from one edge of the grid to another. (planets are spheres after all)
- Implement obstacle detection before each move to a new square. If a given sequence of commands encounters an obstacle, the rover moves up to the last possible point and reports the obstacle.
Here is an example:
- Let's say that the rover is located at 0,0 facing North on a 100x100 grid.
- Given the command "ffrff" would put the rover at 2,2 facing East.
