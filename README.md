# ProgrAmsterdam - Rush Hour
In this project we aim to find algorithms to solve the game named Rush Hour. This game is played on a grid/board. First of, we start with a 6 x 6 grid on which the game is played. Later versions of the game will include larger grids (9x9 and 12x12). On the grid there are cars and trucks. The cars take up 2 squares each and the trucks take up 3 squares each. Also all vehicles can only be moved within a straight line along the grid and they cannot be rotated. In this game the goal is to ride a red car out through the exit of the board. However there are other vehicles that obstruct the path which makes the puzzle harder. The goal is to move the vehicles around so that the exit path for the red car becomes clear and the red car can exit.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Software you need to install for this this project:

```
Python 3.6.x
```

requirements.txt contains all used modules in this project.

```
pip install -r requirements.txt
```

## How to run the solver
To run the solver, simply run the solver.py file.
```
python solver.py
```

The solver will ask for different types of input that you should follow in the following order:

- Which game you want to solve
- What type of algorithm you want to use

Depending on the algorithm it asks for extra input.
When picking breadth-first search:
- Breadth-first Search
- Breadth-first search with a heuristic checking for the amount of cars in front of the red car(basically best-first search per level)
- Beam Search

When picking Beam Search:
- Input for the beam width

Be careful! Boards bigger than 6x6 tend to be unsolvable through brute-force. Instead pick either the A*-search or the beam search to solve those type of boards.

## Solutions
If the solver finds a solution, the solution(as a visualization and in a .csv file) will be saved in the __/solutions/the used algorithm/..__ folder. Some algorithms that we've implemented need a destination point.
Therefore the last move of a solution will be saved in __/solutions/endSolution__.

## Authors
Kevin Vuong 	- 	10730141
Michael Berend 	- 	10534075
Jelle Roebroek 	- 	10815279
