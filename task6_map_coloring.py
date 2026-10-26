"""Task 6 - Map Colouring Problem using CSP (backtracking)"""
import matplotlib
import matplotlib.pyplot as plt

states = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

solution = {}


def valid(state, color):
    for n in neighbors[state]:
        if n in solution and solution[n] == color:
            return False
    return True


def csp(index=0):
    if index == len(states):
        return True
    state = states[index]
    for color in colors:
        if valid(state, color):
            solution[state] = color
            if csp(index + 1):
                return True
            del solution[state]
    return False


csp()
for state in states:
    print(state, "->", solution[state])

# Display the coloured map
pos = {'A': (0, 1), 'B': (-1, 0), 'C': (1, 0), 'D': (0, -1)}

plt.figure(figsize=(4, 6))
for state in neighbors:
    for n in neighbors[state]:
        x = [pos[state][0], pos[n][0]]
        y = [pos[state][1], pos[n][1]]
        plt.plot(x, y, 'k-', zorder=1)

for state in states:
    plt.scatter(*pos[state], s=1500, c=solution[state], edgecolors='black', zorder=2)
    plt.text(pos[state][0], pos[state][1], state, ha='center', va='center',
             color='white', fontsize=14, zorder=3)

plt.title("Map Colouring (CSP)")
plt.axis('off')
plt.savefig("map_colouring.png")
if matplotlib.get_backend().lower() != 'agg':
    plt.show()
