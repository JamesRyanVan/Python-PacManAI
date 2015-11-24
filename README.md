# Python PacMan - Artifical Intelligence

Python pacman is a traditional pacman game, auto completed by search and agent algorithms. Each of the following sub heading is a seperate artifical intelligence challenge. 

If you wish to manually start playing the game, start pacman.py:

```
python pacman.py
```

##### Techical Details

The Pac-Man projects are written in Python 2.7 and do not depend on any packages external to a standard Python distribution.

## Search

Search implements depth-first, breadth-first, uniform cost, and A* search algorithms. These algorithms are used to solve navigation and traveling salesman problems in the Pacman world. These search alogorithms use functions from a node class, which helps store and track data.

To read the full search project details and problems, download search.html from the instructions folder. 

##### To test search.py, you can use the following commands (easy to hard mazes):

```
python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 
```
Bonus problems are not yet completed.

## Multi-Agent

Classic Pacman is modeled as both an adversarial and a stochastic search problem. Multi-Agent implement multiagent minimax and expectimax algorithms, as well as designing evaluation functions.

Currently being worked on.

## Reinforcement Learning

- Incompelete

## Ghostbusters

- Incompelete

## Classification

- Incompelete

## Contest: Pacman Capture the Flag

- Incompelete

#Credits

The projects were developed by John DeNero, Dan Klein, Pieter Abbeel, and many others. 
