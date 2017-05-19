import util
from state import State


def validate(problem, solution):
    '''
    Return true if `solution` is a valid plan for `problem`.
    Otherwise, return false.

    OBSERVATION: you should check action applicability,
    next-state generation and if final state is indeed a goal state.
    It should give you some indication of the correctness of your planner,
    mainly for debugging purposes.
    '''
    state = problem.init

    for action in solution:
        if action.precond.issubset(state):
            successor = state.union(action.pos_effect)
            successor = successor.difference(action.neg_effect)
            state = successor
        else:
            return False
            
    return problem.goal.issubset(state)
