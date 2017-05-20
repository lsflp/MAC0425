import util
import sys

def h_naive(state, planning):
    return 0


def h_add(state, planning):
    '''
    Return heuristic h_add value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''

    h = {}

    for p in state:
        h[p] = 0

    for p in planning.problem.goal:
        if p not in state:
            h[p] = sys.maxsize

    fixpoint = False
    X = state

    while not fixpoint:
        for action in planning.applicable(state):
            X = X.union(action.pos_effect)
            newSum = 1
            # Calculating sum of action preconditions
            for p in action.precond:
                # If precond not defined before, it is infinity.
                # Infinity plus anything equals infinity.
                if h.get(p) == None:
                    newSum = sys.maxsize
                    break
                else:
                    newSum += h.get(p)
            fixpoint = True
            for p in action.pos_effect:
                if h.get(p) == None:
                    h[p] = sys.maxsize
                if newSum < h.get(p):
                    h[p] = newSum
                    fixpoint = False
            if fixpoint:
                break

    # Since h(n) >= 0
    heuristic = 0
    for p in planning.problem.goal:
        heuristic += h.get(p)
    return heuristic

def h_max(state, planning):
    '''
    Return heuristic h_max value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''

    h = {}

    for p in state:
        h[p] = 0

    for p in planning.problem.goal:
        if p not in state:
            h[p] = sys.maxsize

    fixpoint = False
    X = state

    while not fixpoint:
        for action in planning.applicable(state):
            X = X.union(action.pos_effect)
            newSum = 1
            # Calculating sum of action preconditions
            for p in action.precond:
                # If precond not defined before, it is infinity.
                # Infinity plus anything equals infinity.
                if h.get(p) == None:
                    newSum = sys.maxsize
                    break
                else:
                    newSum += h.get(p)
            fixpoint = True
            for p in action.pos_effect:
                if h.get(p) == None:
                    h[p] = sys.maxsize
                if newSum < h.get(p):
                    h[p] = newSum
                    fixpoint = False
            if fixpoint:
                break

    # Since h(n) >= 0
    heuristic = -1
    for p in planning.problem.goal:
        if h.get(p) > heuristic:
            heuristic = h.get(p)
    return heuristic

def h_ff(state, planning):
    '''
    Return heuristic h_ff value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    util.raiseNotDefined()
    ' YOUR CODE HERE '
