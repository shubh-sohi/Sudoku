# Sudoku  
A GUI implementation of the Sudoku game using python's pygame library.  
This game is still under minor and frequent updates and some TODO's. This is not the final version.  
## Features

### Hover
* When the user hovers over a tile in the grid, the row, column and the sub grid of that cube highlightes making   it easy for the 
user to see what numbers are already used.  
* When the user hover over any one of the buttons, the highlight making it visually appealing. 
  
![Hover](https://github.com/shubh-sohi/Sudoku/blob/master/Assets/1.png "Sudoku")

### Helper row
* When the user hover over any empty cube, the initially empty row besides the available row text gets filled up.  
It uses an the get_values function defined and implemented in the Sudoku_init.py file under the Solver folder.
* The get_values function takes the current row and column as parameters which the GUI determines from the mouse position and then 
the finction returns a python set() data structure with all used values. Using those values the helper row is filled up with numbers.
  
![Helper row]( "Sudoku")

### Mouse Down
* When the mouse button is clicked on an empty cube, the row and column highlighter get fixed to that row, column along with 
the helper row.
* Moving the cursor then will not move any of the highlighters and not change the helper row.
* Then the user can fill in number from 1 - 9 in the cube
* To finalize a number, the user is expected to press the return key
* If the number user returns is in the helper row, and thus not in any row, column and subgrid. The cube is highlighted green 
showing that the number entered has been accepted and is implemented into the Sudoku list.
  
![Mouse Down]( "Sudoku")

### Solve Sudoku
* Pressing the Solve Sudoku button will implement the solving algorithm defined and implemented in the Sudoku_init.py file.
  
![Solve]( "Sudoku")

### TODO
* Internal doccumentation
* Implement The "New Sudoku", "Make my own Sudoku" and "Reset" buttons.
* Finish the Sudoku_generator file which will help implementing new random unsolved Sudoku games when the "New Sudoku" button is pressed
* Add background music
* delete key function


#### Hidden Easter Egg
There is one position in the game window that if pressed will unleash some funky colours.  
P.S- This might give you a headache.
Hint: Sudoku doesn't likes to be cliked.
  
![Click on the big Sudoku test]( "Sudoku")

The game implements the pygame library which can be installed in a mac using the following commend  
`python -m pip install pygame==1.9.3`

An implementaion of Sudoku solver using an algorith similar to but not exactly like backtracking. Backtracking algorithms use 
recursion, which in some intense cases tends to become extreamly tricky if not handelled correctly.
* The main solver uses while loop to get to the next empty slot in the grid
* Tries values from 1 to 9 in that order
* A checker function is calles on every value which only returns True is a value can be safely placed into that slot
* The value's instance is stored in a dictionary with its row and column number.
* If at any instance a slot returns False for all values 1 to 9, the while loop counter for row and columnd is manually changes 
to go back to the previous solved slot row and column and try a diffternt value in that slot, different = other than the value previously used.
