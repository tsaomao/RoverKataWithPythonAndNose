Approach and Strategy notes:

Goal for me is not only to program this kata in Python but also to apply test-driven development principles as well as good source control and commenting hygeine, so as I code the classes, 
methods and attributes, I will also code unit tests and write comments meant both for internal use and for Python docstrings. And finally, I will do frequent commits and pushes of these 
code, testing and documentation assets.

Still to do:
- Implement wrapping for the world grid
- Consider refactoring so the world grid specifically contains and tracks the Rover object's position
- refactor to validate/raise exception on self.facing not as expected in a central place, probably __init__()

Original Problem statement:
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
