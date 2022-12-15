import sys

print(f"Usage: pyhton {sys.argv[0]} [t|p]")
print(f"    t = test mode")
print(f"    p = production mode")
print(f"  Current: {sys.argv[1:]=}")


"""
--- Day 14: Regolith Reservoir ---
The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the waterfall itself, and that doesn't make any sense. However, you do notice a little path that leads behind the waterfall.

Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, and the signal definitely leads further inside.

As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!

Fortunately, your familiarity with analyzing the path of falling material will come in handy here. You scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly air with structures made of rock.

Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the path, where x represents distance to the right and y represents distance down. Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:

498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
This scan means that there are two paths of rock; the first path consists of two straight lines, and the second path consists of three straight lines. (Specifically, the first path consists of a line of rock from 498,4 through 498,6 and another line of rock from 498,6 through 496,6.)

The sand is pouring into the cave from point 500,0.

Drawing rock as #, air as ., and the source of the sand as +, this becomes:


  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.
Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes to rest. A unit of sand is large enough to fill one tile of air in your scan.

A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source.

So, drawing sand that has come to rest as o, the first unit of sand simply falls straight down and then stops:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
......o.#.
#########.
The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its left:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
.....oo.#.
#########.
After a total of five units of sand have come to rest, they form this pattern:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
......o.#.
....oooo#.
#########.
After a total of 22 units of sand:

......+...
..........
......o...
.....ooo..
....#ooo##
....#ooo#.
..###ooo#.
....oooo#.
...ooooo#.
#########.
Finally, only two more units of sand can possibly come to rest:

......+...
..........
......o...
.....ooo..
....#ooo##
...o#ooo#.
..###ooo#.
....oooo#.
.o.ooooo#.
#########.
Once all 24 units of sand shown above have come to rest, all further sand flows out the bottom, falling into the endless void. Just for fun, the path any new sand takes before falling forever is shown here with ~:

.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
~..........
~..........
~..........
Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?
"""

in_text = 'in' if len(sys.argv) > 1 and sys.argv[1] == 'p' else 'in_test'
print(in_text)
with open(in_text + '.txt') as data:
    #inputs = [line.strip() for line in data.readlines()]
    inputs = [line.rstrip() for line in data.readlines()]

print(inputs)

rocks = []
# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9
for i_, x_ in enumerate(inputs):
    rocks.append([])
    for r_ in (x_.split(' -> ')):
        rocks[i_].append((int(r_.split(',')[1]), int(r_.split(',')[0])))

import numpy as np

# print(rocks)

rs_flat = [[], []]
for rs in rocks:
    for r_ in rs:
        rs_flat[0].append(r_[0])
        rs_flat[1].append(r_[1])
# print(rs_flat)
min_h = min(rs_flat[0])
max_h = max(rs_flat[0])
print("[0] min:", min_h)
print("[0] max:", max_h)
min_l = min(rs_flat[1])
max_l = max(rs_flat[1])
print("[1] min:", min_l)
print("[1] max:", max_l)

void = "."
rock = "#"
cave = []
for i_ in range(max_h + 3):
    cave.append([])
    for j_ in range(500 * 2):
        cave[i_].append(void)

# print("----- full cave")
# for c_ in cave:
#     print(''.join(c_))

for rs in rocks:
    for i_, r_ in enumerate(rs[:-1]):
        if r_[0] == rs[i_+1][0]:
            for j_ in range(min(rs[i_+1][1],r_[1]), max(rs[i_+1][1],r_[1]) + 1):
                cave[r_[0]][j_] = rock
        else:
            for j_ in range(min(r_[0], rs[i_ + 1][0]),
                            max(r_[0], rs[i_ + 1][0]) + 1):
                cave[j_][r_[1]] = rock

ml = 89 if len(
    sys.argv) > 1 and sys.argv[1] == 'p' else 9  # margin left for print
mr = 160 if len(
    sys.argv) > 1 and sys.argv[1] == 'p' else 10  # margin right for print

print(f"----- cave[{min_l - ml}: {max_l + mr}]")
for c_ in cave:
    print(''.join(c_[min_l - ml: max_l + mr]))


sand = "o"
initial_sand = (0,500)

def move_sand(initial):
    global max_h, void, sand

    stucked = False
    sc = initial
    while (sc[0] < max_h + 2):
        if cave[sc[0]+1][sc[1]] == void:
            sc = [sc[0] + 1, sc[1]]
        elif cave[sc[0]+1][sc[1]-1] == void:
            sc = [sc[0] + 1, sc[1]-1]
        elif cave[sc[0] + 1][sc[1] + 1] == void:
            sc = [sc[0] + 1, sc[1] + 1]
        else:
            # stucked
            if sc == initial:
                cave[sc[0]][sc[1]] = sand
                return -1
            else:
                cave[sc[0]][sc[1]] = sand
                return 0
        if sc[0] > max_h + 1:
            return -1

step = 500 if len(sys.argv) > 1 and sys.argv[1] == 'p' else 1

t_ = 1
while True:
    if move_sand(initial_sand) != -1:
        if ((t_ % step) == 0):
            print(f"===== {t_}")
            for c_ in cave:
                print(''.join(c_[min_l - ml:max_l + mr]))
        t_ += 1
    else:
        break
print(f"===== {t_ - 1}")
for c_ in cave:
    print(''.join(c_[min_l - ml:max_l + mr]))

print(f"part 1: {t_ - 1}")

# p --> 578

"""
--- Part Two ---
You realize you misread the scan. There isn't an endless void at the bottom of the scan - there's floor, and you're standing on it!

You don't have time to scan the floor, so assume the floor is an infinite horizontal line with a y coordinate equal to two plus the highest y coordinate of any point in your scan.

In the example above, the highest y coordinate of any point is 9, and so the floor is at y=11. (This is as if your scan contained one extra rock path like -infinity,11 -> infinity,11.) With the added floor, the example above now looks like this:

        ...........+........
        ....................
        ....................
        ....................
        .........#...##.....
        .........#...#......
        .......###...#......
        .............#......
        .............#......
        .....#########......
        ....................
<-- etc #################### etc -->
To find somewhere safe to stand, you'll need to simulate falling sand until a unit of sand comes to rest at 500,0, blocking the source entirely and stopping the flow of sand into the cave. In the example above, the situation finally looks like this after 93 units of sand come to rest:

............o............
...........ooo...........
..........ooooo..........
.........ooooooo.........
........oo#ooo##o........
.......ooo#ooo#ooo.......
......oo###ooo#oooo......
.....oooo.oooo#ooooo.....
....oooooooooo#oooooo....
...ooo#########ooooooo...
..ooooo.......ooooooooo..
#########################
Using your scan, simulate the falling sand until the source of the sand becomes blocked. How many units of sand come to rest?
"""

print("")
print("====================--------====================")
print("==================== PART 2 ====================")
print("====================--------====================")

cave = []

for i_ in range(max_h + 3):
    cave.append([])
    for j_ in range(500 * 2):
        cave[i_].append(void)

for i_ in range(500 * 2):
    cave[max_h + 2][i_] = rock

for rs in rocks:
    for i_, r_ in enumerate(rs[:-1]):
        if r_[0] == rs[i_ + 1][0]:
            for j_ in range(min(rs[i_ + 1][1], r_[1]),
                            max(rs[i_ + 1][1], r_[1]) + 1):
                cave[r_[0]][j_] = rock
        else:
            for j_ in range(min(r_[0], rs[i_ + 1][0]),
                            max(r_[0], rs[i_ + 1][0]) + 1):
                cave[j_][r_[1]] = rock

for c_ in cave:
    print(''.join(c_[min_l - ml:max_l + mr]))

t_ = 1
while True:
    if move_sand(initial_sand) != -1:
        if ((t_ % step) == 0):
            print(f"===== {t_}")
            for c_ in cave:
                print(''.join(c_[min_l - ml:max_l + mr]))
        t_ += 1
    else:
        break

print(f"===== {t_}")
for c_ in cave:
    print(''.join(c_[min_l - ml:max_l + mr]))

print(f"part 2: {t_}")

# p --> 24377
