# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # Inicializa una pila para los nodos por explorar
    frontier = util.Stack()

    # Inicializa un conjunto para los nodos ya explorados
    explored = set()

    # Agrega el estado inicial a la pila
    frontier.push((problem.getStartState(), []))

    while not frontier.isEmpty():
        # Extrae el nodo actual y el camino hasta él
        node, path = frontier.pop()

        # Si el nodo es el objetivo, devuelve el camino hasta él
        if problem.isGoalState(node):
            return path

        # Si el nodo no ha sido explorado
        if node not in explored:
            # Marca el nodo como explorado
            explored.add(node)

            # Agrega los sucesores del nodo a la pila
            for successor, action, _ in problem.getSuccessors(node):
                frontier.push((successor, path + [action]))

    # Si no se encuentra un camino al objetivo, levanta una excepción
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # Inicializa una cola para los nodos por explorar
    frontier = util.Queue()

    # Inicializa un conjunto para los nodos ya explorados
    explored = set()

    # Agrega el estado inicial a la cola
    frontier.push((problem.getStartState(), []))

    while not frontier.isEmpty():
        # Extrae el nodo actual y el camino hasta él
        node, path = frontier.pop()

        # Si el nodo es el objetivo, devuelve el camino hasta él
        if problem.isGoalState(node):
            return path

        # Si el nodo no ha sido explorado
        if node not in explored:
            # Marca el nodo como explorado
            explored.add(node)

            # Agrega los sucesores del nodo a la cola
            for successor, action, _ in problem.getSuccessors(node):
                frontier.push((successor, path + [action]))

    # Si no se encuentra un camino al objetivo, levanta una excepción

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Inicializa una cola de prioridad para los nodos por explorar
    frontier = util.PriorityQueue()

    # Inicializa un conjunto para los nodos ya explorados
    explored = set()

    # Agrega el estado inicial a la cola con prioridad 0
    frontier.push((problem.getStartState(), []), 0)

    while not frontier.isEmpty():
        # Extrae el nodo actual y el camino hasta él
        node, path = frontier.pop()

        # Si el nodo es el objetivo, devuelve el camino hasta él
        if problem.isGoalState(node):
            return path

        # Si el nodo no ha sido explorado
        if node not in explored:
            # Marca el nodo como explorado
            explored.add(node)

            # Agrega los sucesores del nodo a la cola con la prioridad igual al costo del camino
            for successor, action, cost in problem.getSuccessors(node):
                newPath = path + [action]
                newCost = problem.getCostOfActions(newPath)
                frontier.update((successor, newPath), newCost)

    # Si no se encuentra un camino al objetivo, levanta una excepción

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Inicializa una cola de prioridad para los nodos por explorar
    frontier = util.PriorityQueue()

    # Inicializa un conjunto para los nodos ya explorados
    explored = set()

    # Agrega el estado inicial a la cola con prioridad 0
    frontier.push((problem.getStartState(), []), 0)

    while not frontier.isEmpty():
        # Extrae el nodo actual y el camino hasta él
        node, path = frontier.pop()

        # Si el nodo es el objetivo, devuelve el camino hasta él
        if problem.isGoalState(node):
            return path

        # Si el nodo no ha sido explorado
        if node not in explored:
            # Marca el nodo como explorado
            explored.add(node)

            # Agrega los sucesores del nodo a la cola con la prioridad igual al costo del camino más la heurística
            for successor, action, cost in problem.getSuccessors(node):
                newPath = path + [action]
                newCost = problem.getCostOfActions(newPath) + heuristic(successor, problem)
                frontier.update((successor, newPath), newCost)

    # Si no se encuentra un camino al objetivo, levanta una excepción


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
