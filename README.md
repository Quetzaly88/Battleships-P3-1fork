# A Battleships Game
Portfolio Project 3 Python Essentials - Code Institute

## About
This game is of [battleships](http://battleship-game.net/), a well known game originally made on paper after WWI. This version differs from many others in that it is for one user against the computer with randomly generated battleship locations of one square. 

## How To Play

The game will first ask the user to enter a username before randomly generating 4 ship locations on both your board and the computer's board, these are signified with the letter "o". 

The game will then request that the user enters a column and row number (essentially, co-ordinates) of the location they suspect a battleship is laid. If that location is on a battleship, it is a hit and marked as "#". If the location is not on a battleship, it is a miss and marked as "*". 

The computer and user will take ten turns to find all 4 of the ships, should all 10 turns be taken without finding 4 ships, the game will state who has had the most hits and display them as the winner. 

## Features

### Existing Features

### Future Features

## Testing

### Manual Testing

### Bugs/Updates after Testing

- After user testing, starting at 0 was a little confusing so the code was updated to accept numbers between 1 and 5 instead.
- After user feedback, I also implemented the input breaks where the user must press enter to continue so that they could see the result of each turn without needing to scroll up.

### Validator Testing

## Deployment

## Credits

- This project uses the [Code Institute student template](https://github.com/Code-Institute-Org/python-essentials-template) for deploying the third portfolio project, the Python command-line project
- The idea of using battleships is a suggested one by the Code Institute with "Ultimate Battleships" as inspiration
- Thank you to my friend Jodie Clark for being my user and testing the game, your points were invaluable.
