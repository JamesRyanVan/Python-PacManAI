# Python PacMan - Artifical Intelligence

Python pacman is a traditional pacman game, auto completed by search and agent algorithms. Each of the following sub heading is a seperate 'project'. 

##### Techical Details

The Pac-Man projects are written in Python 2.7 and do not depend on any packages external to a standard Python distribution.

## Search

Search implements depth-first, breadth-first, uniform cost, and A* search algorithms. These algorithms are used to solve navigation and traveling salesman problems in the Pacman world. These search alogorithms use functions from a node class, which helps store and track data.

To read the full search project details and problems, download search.html from the instructions folder. 

##### To test search.py, you can use the following commands (easy to hard mazes):

- python pacman.py
- python pacman.py --layout testMaze --pacman GoWestAgent
- python pacman.py --layout tinyMaze --pacman GoWestAgent
- python pacman.py -h
- python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
- python pacman.py -l tinyMaze -p SearchAgent
- python pacman.py -l mediumMaze -p SearchAgent
- python pacman.py -l bigMaze -z .5 -p SearchAgent
- python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
- python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
- python eightpuzzle.py
- python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
- python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
- python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
- python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 
- python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
- python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
- python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
- python pacman.py -l testSearch -p AStarFoodSearchAgent
- python pacman.py -l trickySearch -p AStarFoodSearchAgent
- python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
- python pacman.py -l bigSearch -p ApproximateSearchAgent -z .5 -q 

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
