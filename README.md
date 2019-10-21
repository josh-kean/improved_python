# improved_python

Welcome to the Pithon depository. To play this game you will need Python3 and the PyGame library installed on your machine. 

The only available user controls are the directional arrows. 
Up to move up, Left to move left, Right to move right, and Down to move down

# About
This project is an ongoing effort to rewrite one of my first Python projects in a more maintainable and scalable syntax.
The code was written using the guidlines set in PEP 8 (https://www.python.org/dev/peps/pep-0008/)
The original project can be found at this GitHub repository; https://github.com/josh-kean/Pithon

# Structure
The entire game screen and it's associated settings (length, width, background) are stored in their own class. 
The "snake" (moving digits in Pi) is contained in its own class. The following properties are all contained within the snake class;
  1. The current length of the snake.
  2. The direction that the snake is moving in.
  3. Movement controls (allowing the user to control the direction of the snake).
  4. A function to go through the snake positions and render the appropriate digit of Pi.
  
The "food" (next digit in Pi) is also contained in it's own class. The following properties are contained within the food class;
  1. A function to display a digit in Pi.
  2. The food's position on the game board.
  3. The ability to detect the snake's position and not render food anywhere within the snakes body
  
# Design Process
The first step I did was to generate a dictionary of the digits in Pi mapped to their index in Pi. A dictionary was chosen to decrease the required time to access the next digit information.

This was done by finding the first hundred digits in Pi online and parsing them through the following Python function;
pi_digits = "31415..." (the actual string was excluded from this README for consistency)<br/>
pi = {x: pi_digits[x] for x in range(len(pi_digits))}

The result of the dictionary pi were saved in a new Python file to import into the main game file. 

The next step was to create the game elements, including the game screen, snake, and food. All were built into their own classes to maintain clarity when updating various ingame elements.

# TODO
I would like to make the following changes to this program in the future;
  1. Add a hard mode where 2 digits appear on the screen, one of which is incorrect and will cause the game to end.
  2. Allow the Snake class and the Food class to talk to eachother. Their values are being passed to eachother in the main game function rite now, which is something I'd like to remove for DRY purposes.
