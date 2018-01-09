# Bombsweeper

The game is played by revealing cells of the grid by indicating each cell. 
On selection of a cell,
If no bomb is revealed, a digit is instead displayed in the cell, indicating how many adjacent cells contain bombs.
if no bombs are adjacent, the cell displays 0, and all adjacent cells will be recursively revealed.
If a cell containing a bomb is revealed, the player loses the game and all the cells with bombs are revealed.
The player uses this information to deduce the contents of other cells.
User may either safely reveal each cell or mark the square as containing a cell by using a flag.
A question mark may be placed in an unrevealed cell to serve as an aid to logical deduction.
Timer
Number of flags available
