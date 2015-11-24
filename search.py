# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  from Node import Node

  stack = util.Stack()
  fringe = Node(problem.getStartState(), [], [])

  stack.push(fringe)

  while not stack.isEmpty():
  	fringe = stack.pop()

  	for coord, direction, steps in problem.getSuccessors(fringe.c):
  		if not coord in fringe.v:
  			if problem.isGoalState(coord):
  				return fringe.a + [direction]
  			newFringe = Node(coord, fringe.a + [direction], fringe.v + [coord])
  			stack.push(newFringe)

  return []

def breadthFirstSearch(problem):
  from Node import Node

  queue = util.Queue()
  fringe = Node(problem.getStartState(), [], [])

  queue.push(fringe)

  while not queue.isEmpty():
  	fringe = queue.pop()

        for coord, direction, steps in problem.getSuccessors(fringe.c):
            if not coord in fringe.v:
                if problem.isGoalState(coord):
                    return fringe.a + [direction]
                newFringe = Node(coord, fringe.a + [direction], fringe.v + [coord])
                queue.push(newFringe)
  return []
      
def uniformCostSearch(problem):
  from Node import Node

  queue = util.PriorityQueue()
  fringe = Node(problem.getStartState(), [], [])

  queue.push(fringe, 0)

  while not queue.isEmpty():
  	fringe = queue.pop()

  	if problem.isGoalState(fringe.c):
  		return fringe.a

        fringe.v += fringe.c

        for coord, direction, steps in problem.getSuccessors(fringe.c):
            if not coord in fringe.v:
                newFringe = Node(coord, fringe.a + [direction], fringe.v + [coord])
                queue.push(newFringe, problem.getCostOfActions(fringe.a + [direction]))

  return []


def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  from Node import Node

  queue = util.PriorityQueue()
  fringe = Node(problem.getStartState(), [], [])

  queue.push(fringe, heuristic(problem.getStartState(), problem))

  while not queue.isEmpty():
    fringe = queue.pop()

    if problem.isGoalState(fringe.c):
    	return fringe.a

    fringe.v += fringe.c

    for coord, direction, cost in problem.getSuccessors(fringe.c):
        if not coord in fringe.v:
            score = problem.getCostOfActions(fringe.a + [direction]) + heuristic(coord, problem)
            newFringe = Node(coord, fringe.a + [direction], fringe.v + [coord])
            queue.push(newFringe, score)

  return []
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch