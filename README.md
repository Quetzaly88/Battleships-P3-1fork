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

### Bugs

### Validator Testing

## Deployment

## Credits

- This project uses the [Code Institute student template](https://github.com/Code-Institute-Org/python-essentials-template) for deploying the third portfolio project, the Python command-line project
- The idea of using battleships is a suggested one by the Code Institute with "Ultimate Battleships" as inspiration

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.