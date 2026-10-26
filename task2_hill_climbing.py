"""Task 2 - Hill Climbing for the Blocks World (global heuristic)"""

start_state = ['A', 'D', 'C', 'B']   # index 0 = top block
goal_state = ['D', 'C', 'B', 'A']


def display(state):
    """Display blocks vertically"""
    for block in state:
        print(block)


def heuristic(state):
    """
    Global heuristic:
    +3 for correct top block, +2 for correct third block,
    +1 for correct second block, +0 for correct bottom block
    wrong position: -3, -2, -1, 0
    """
    score = 0
    weights = [3, 2, 1, 0]
    for i in range(4):
        if state[i] == goal_state[i]:
            score += weights[i]
        else:
            score -= weights[i]
    return score


def get_neighbours(state):
    """Neighbours: take the top block and insert it at every other position."""
    neighbours = []
    for pos in range(1, len(state)):
        new_state = state[1:]
        new_state.insert(pos, state[0])
        neighbours.append(new_state)
    return neighbours


def hill_climbing(start):
    current = start
    current_h = heuristic(current)
    step = 0
    while current != goal_state:
        best_neighbour, best_h = None, current_h
        for n in get_neighbours(current):
            h = heuristic(n)
            if h > best_h:
                best_neighbour, best_h = n, h
        if best_neighbour is None:      # no better neighbour -> local maximum
            print("Stuck at local maximum")
            break
        current, current_h = best_neighbour, best_h
        step += 1
        print("\nIn move", step)
        display(current)
        print("Heuristic value =", current_h)
    return current


print("Initial State \n")
display(start_state)
print("Heuristic value =", heuristic(start_state))

current = hill_climbing(start_state)

if current == goal_state:
    print("\nGoal State Reached")
    print("Maximum Heuristic =", heuristic(current))
    print("Hill climbing Successfully")
