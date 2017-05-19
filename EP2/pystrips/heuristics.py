import util


def h_naive(state, planning):
    return 0


def h_add(state, planning):
    '''
    Return heuristic h_add value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''

    h = {}

    for p in planning.problem.goal:
        if p in state:
            h[p] = 0
        else:
            h[p] = float("inf")

    X = state # X is a set of propositions
    actions = planning.actions
    condition = True

    while condition:
        for action in actions:
            if action.precond.issubset(X):
                X = X.union(action.pos_effect)
                for p in action.pos_effect:
                    newSum = 1
                    for q in action.precond:
                        newSum += h.get(q)
                    if (h.get(p) < newSum):
                        result = 0
                        for g in planning.problem.goal:
                            result += h.get(g)
                        return result
                    h[p] = min(h.get(p), newSum)

def h_max(state, planning):
    '''
    Return heuristic h_max value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''

    h = {}

    for p in planning.problem.goal:
        if p in state:
            h[p] = 0
        else:
            h[p] = float("inf")

    X = state # X is a set of propositions
    actions = planning.actions
    condition = True

    while condition:
        for action in actions:
            if action.precond.issubset(X):
                X = X.union(action.pos_effect)
                for p in action.pos_effect:
                    newSum = 1
                    for q in action.precond:
                        if (h.get(q) != None):
                            newSum += h.get(q)
                    if (h.get(p) != None and h.get(p) < newSum):
                        result = -1
                        for g in planning.problem.goal:
                            if h.get(g) > result:
                                result = h.get(g)
                            return result
                    if (h.get(p) != None):
                        h[p] = min(h.get(p), newSum)


def h_ff(state, planning):
    '''
    Return heuristic h_ff value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    util.raiseNotDefined()
    ' YOUR CODE HERE '
