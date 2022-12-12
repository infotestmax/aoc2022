import sys

print(f"Usage: pyhton {sys.argv[0]} [t|p]")
print(f"    t = test mode")
print(f"    p = production mode")
print(f"  Current: {sys.argv[1:]=}")


"""
--- Day 12: Hill Climbing Algorithm ---
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?
"""

in_text = 'in' if len(sys.argv) > 1 and sys.argv[1] == 'p' else 'in_test'
print(in_text)
with open(in_text + '.txt') as data:
    #inputs = [line.strip() for line in data.readlines()]
    inputs = [line.rstrip() for line in data.readlines()]

print(inputs)


def dijkstra(current, nodes, distances):
    # These are all the nodes which have not been visited yet
    unvisited = {node: None for node in nodes}
    # It will store the shortest distance from one node to another
    visited = {}
    # It will store the predecessors of the nodes
    currentDistance = 0
    unvisited[current] = currentDistance
    # Running the loop while all the nodes have been visited
    while True:
        # iterating through all the unvisited node
        for neighbour, distance in distances[current].items():
            # Iterating through the connected nodes of current_node (for
            # example, a is connected with b and c having values 10 and 3
            # respectively) and the weight of the edges
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        # Till now the shortest distance between the source node and target node
        # has been found. Set the current node as the target node
        visited[current] = currentDistance
        if unvisited.get(current, None):
            del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        # print("--- sorted candidates ---")
        # print(sorted(candidates, key = lambda x: x[1]))
        if candidates:
            current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
        else:
            break
    return visited

# nodes = ('A', 'B', 'C', 'D', 'E')
# distances = {
#     'A': {'B': 5, 'C': 2},
#     'B': {'C': 2, 'D': 3},
#     'C': {'B': 3, 'D': 7},
#     'D': {'E': 7},
#     'E': {'D': 9}}
# current = 'A'

#print(dijkstra(current, nodes, distances))

for i_ in range(len(inputs)):
    inputs[i_] = [c_ for c_ in inputs[i_]]

max_i = len(inputs)
max_j = len(inputs[0])

max_value = sys.maxsize

nodes = tuple(f"{i_},{j_}" for i_ in range(max_i) for j_ in range(max_j))
print(f"nodes: {nodes}")
distances = {}

print(ord('a')) # 97
values = { c_: ord(c_) - 97 for c_ in 'abcdefghijklmnopqrstuvwxyz' }
values['S'] = 0
values['E'] = 26
print(values)


def get_eligible_neighbours(n_):
    global max_i, max_j, max_value
    i_, j_ = int(n_[0]), int(n_[1])
    current_value = values[inputs[i_][j_]]
    neighbours_to_include = []
    if i_ > 0 and (values[inputs[i_-1][j_]] - current_value) < 2: # can go up
        neighbours_to_include.append(f"{i_-1},{j_}")
    if i_ < max_i - 1 and (values[inputs[i_+1][j_]] - current_value) < 2: # can go down
        neighbours_to_include.append(f"{i_+1},{j_}")
    if j_ > 0 and (values[inputs[i_][j_-1]] - current_value) < 2: # can go left
        neighbours_to_include.append(f"{i_},{j_-1}")
    if j_ < max_j - 1 and (values[inputs[i_][j_+1]] - current_value) < 2: # can go right
        neighbours_to_include.append(f"{i_},{j_+1}")
    return neighbours_to_include


start = None
end = None
for node in nodes:
    n_ = node.split(',')
    if inputs[int(n_[0])][int(n_[1])] == 'S':
        start = node # define the sarting point
    elif inputs[int(n_[0])][int(n_[1])] == 'E':
        end = node # define the end point
    #get the neighbours into a dictionay
    neighbours_to_include = get_eligible_neighbours(n_)

    distances[node] = {x_: 1 for x_ in neighbours_to_include}

# print(start, distances[start])
# print(end, distances[end])

print(f"part 1: {dijkstra(start, nodes, distances)[end]}")
# --> p: 412

"""
--- Part Two ---
As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^
This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?
"""

def dijkstra_with_end(current, nodes, distances, end):
    # These are all the nodes which have not been visited yet
    unvisited = {node: None for node in nodes}
    # It will store the shortest distance from one node to another
    visited = {}
    # It will store the predecessors of the nodes
    currentDistance = 0
    unvisited[current] = currentDistance
    # Running the loop while all the nodes have been visited
    while True:
        # iterating through all the unvisited node
        for neighbour, distance in distances[current].items():
            # Iterating through the connected nodes of current_node (for
            # example, a is connected with b and c having values 10 and 3
            # respectively) and the weight of the edges
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        # Till now the shortest distance between the source node and target node
        # has been found. Set the current node as the target node
        visited[current] = currentDistance
        if unvisited.get(current, None):
            del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        # Arrêter dès que 'end' a été atteint
        for n_ in candidates:
            if end == n_[0]:
                break
        if candidates:
            current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
        else:
            break
    return visited


start = []
end = None
for node in nodes:
    n_ = node.split(',')
    if inputs[int(n_[0])][int(n_[1])] in ['S', 'a']:
        start.append(node) # append the sarting points
    elif inputs[int(n_[0])][int(n_[1])] == 'E':
        end = node # define the end point
    #get the neighbours into a dictionay
    neighbours_to_include = get_eligible_neighbours(n_)
    distances[node] = {x_: 1 for x_ in neighbours_to_include}

# for i_, s_ in enumerate(start):
#     print(f"start[{i_}]: {s_}", distances[s_])
# print(f"end: {end}", distances[end])

result = [dijkstra_with_end(s_, nodes, distances, end) for s_ in start]
# print(f"---------- result[0] ----------> :\n{result[0]}")
print(f"part 2: {min([r_[end] for r_ in result if r_.get(end, None)])}")

# --> p: 402
