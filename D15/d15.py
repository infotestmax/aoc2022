import sys

print(f"Usage: pyhton {sys.argv[0]} [t|p]")
print(f"    t = test mode")
print(f"    p = production mode")
print(f"  Current: {sys.argv[1:]=}")


"""
--- Day 15: Beacon Exclusion Zone ---
You feel the ground rumble again as the distress signal leads you to a large network of subterranean tunnels. You don't have time to search them all, but you don't need to: your pack contains a set of deployable sensors that you imagine were originally built to locate lost Elves.

The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close enough to the source of the distress signal to use them. You pull the emergency sensor system out of your pack, hit the big button on top, and the sensors zoom off down the tunnels.

Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface and begins monitoring for the nearest signal source beacon. Sensors and beacons always exist at integer coordinates. Each sensor knows its own position and can determine the position of a beacon precisely; however, sensors can only lock on to the one beacon closest to the sensor as measured by the Manhattan distance. (There is never a tie where two beacons are the same distance to a sensor.)

It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). For example:

Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
So, consider the sensor at 2,18; the closest beacon to it is at -2,15. For the sensor at 9,16, the closest beacon to it is at 10,16.

Drawing sensors as S and beacons as B, the above arrangement of sensors and beacons looks like this:

               1    1    2    2
     0    5    0    5    0    5
 0 ....S.......................
 1 ......................S.....
 2 ...............S............
 3 ................SB..........
 4 ............................
 5 ............................
 6 ............................
 7 ..........S.......S.........
 8 ............................
 9 ............................
10 ....B.......................
11 ..S.........................
12 ............................
13 ............................
14 ..............S.......S.....
15 B...........................
16 ...........SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its closest beacon, if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor. There could still be beacons that just happen to not be the closest beacon to any sensor. Consider the sensor at 8,7:

               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########S#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....B############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
This sensor's closest beacon is at 2,10, and so you know there are no beacons that close or closer (in any positions marked #).

None of the detected beacons seem to be producing the distress signal, so you'll need to work out where the distress beacon is by working out where it isn't. For now, keep things simple by counting the positions where a beacon cannot possibly be along just a single row.

So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the row where y=10, you'd like to count the number of positions a beacon cannot possibly exist. The coverage from all sensors near that row looks like this:

                 1    1    2    2
       0    5    0    5    0    5
 9 ...#########################...
10 ..####B######################..
11 .###S#############.###########.
In this example, in the row where y=10, there are 26 positions where a beacon cannot be present.

Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions cannot contain a beacon?
"""

in_text = 'in' if len(sys.argv) > 1 and sys.argv[1] == 'p' else 'in_test'
print(in_text)
with open(in_text + '.txt') as data:
    inputs = [line.strip() for line in data.readlines()]

print(inputs)

import re
commands_extractor = re.compile('.*=(-?\d+),.*=(-?\d+):.*=(-?\d+),.*=(-?\d+)')

parsed = []
for x_ in inputs:
    parsed.append(list(commands_extractor.findall(x_)[0]))

# Change back to int
for x_ in parsed:
    for i_, s_ in enumerate(x_):
        x_[i_] = int(s_)

# Mahattan distance: distance = |x2 - x1| + |y2 - y1|
for x_ in parsed:
    x_.append(abs(x_[0] - x_[2]) + abs(x_[1] - x_[3]))

for x_ in parsed:
    print(x_)

if len(sys.argv) == 1 or sys.argv[1] != 'p':
    for x_ in parsed:
        x_.append([(i_, j_) for i_ in range(x_[0] - x_[4], x_[0] + x_[4] + 1)
                for j_ in range(x_[1] - x_[4], x_[1] + x_[4] + 1)
                if (abs(x_[0] - i_) + abs(x_[1] - j_)) <= x_[4]])

    for x_ in parsed:
        print(x_)


void ='.'

def print_sensor_area(i_):
    x_ = parsed[i_]
    x_min = x_[0] - x_[4]
    x_max = x_[0] + x_[4]
    y_min = x_[1] - x_[4]
    y_max = x_[1] + x_[4]
    x_correcteur = abs(max(0, x_min) - x_min)
    print("x_correcteur: ", x_correcteur)
    y_correcteur = abs(max(0, y_min) - y_min)
    print("y_correcteur: ", y_correcteur)
    x_min += x_correcteur
    x_max += x_correcteur
    y_min += y_correcteur
    y_max += y_correcteur
    to_print = []

    for _ in range(y_min,y_max+1):
        to_print.append([])
        for _ in range(x_min,x_max+1):
            to_print[-1].append(void)

    # print("x_[-1]: ", x_[-1])

    for z_ in x_[-1]:
        # print("z_[0], z_[1]: ", z_[0], z_[1])
        to_print[z_[1] + y_correcteur][z_[0] + x_correcteur] = "#"

    for e_, p_ in enumerate(parsed):
        if (p_[0]+x_correcteur) in range(x_min, x_max + 1) and (p_[1]+y_correcteur) in range(y_min, y_max + 1):
            print(f"{e_}: ({p_[0]}, {p_[1]})")
            # to_print[p_[1] + y_correcteur][p_[0] + x_correcteur] = f"{e_}"
            to_print[p_[1] + y_correcteur][p_[0] + x_correcteur] = "S"
        if (p_[2] + x_correcteur) in range(
                x_min, x_max + 1) and (p_[3] + y_correcteur) in range(
                    y_min, y_max + 1):
            to_print[p_[3] + y_correcteur][p_[2] + x_correcteur] = "B"

    print(f"Sensor @{i_}: ({x_[0]}, {x_[1]})")
    for p_ in to_print:
        print(''.join(p_))

if len(sys.argv) == 1 or sys.argv[1] != 'p':
    print_sensor_area(6)  # sensor at 8,7


def get_sensor_correctors(i_):
    x_ = parsed[i_]
    x_min = x_[0] - x_[4]
    x_max = x_[0] + x_[4]
    y_min = x_[1] - x_[4]
    y_max = x_[1] + x_[4]
    x_correcteur = abs(max(0, x_min) - x_min)
    y_correcteur = abs(max(0, y_min) - y_min)
    return x_correcteur, y_correcteur, x_min + x_correcteur, x_max + x_correcteur, y_min + y_correcteur, y_max + y_correcteur


def get_every_sensors_area():

    g_x_c = 0  # global x correcteur
    g_y_c = 0  # global y correcteur
    g_x_min = 0
    g_x_max = 0
    g_y_min = 0
    g_y_max = 0
    for i_ in range(len(parsed)):
        x_c, y_c, x_min, x_max, y_min, y_max = get_sensor_correctors(i_)
        print(f"{i_}: ", x_c, y_c, x_min, x_max, y_min, y_max)
        g_x_c = x_c if x_c > g_x_c else g_x_c
        g_y_c = y_c if y_c > g_y_c else g_y_c
        g_x_min = x_min if x_min < g_x_min else g_x_min
        g_x_max = x_max if x_max > g_x_max else g_x_max
        g_y_min = y_min if y_min < g_y_min else g_y_min
        g_y_max = y_max if y_max > g_y_max else g_y_max

    # to_print = []
    # for _ in range(g_y_min, g_y_max * 2):
    #     to_print.append([])
    #     for _ in range(g_x_min, g_x_max * 2):
    #         to_print[-1].append(void)

    # for p_ in to_print:
    #     print(''.join(p_))

    # for x_ in parsed:
    #     x_min = x_[0] - x_[4]
    #     x_max = x_[0] + x_[4]
    #     y_min = x_[1] - x_[4]
    #     y_max = x_[1] + x_[4]
    #     x_min += g_x_c
    #     x_max += g_x_c
    #     y_min += g_y_c
    #     y_max += g_y_c

    #     for z_ in x_[-1]:
    #         print(z_)
    #         print(g_x_c, g_y_c)
    #         print(f"x: 0-{len(to_print[0])}", f"y: 0-{len(to_print)}")
    #         print([z_[1] + g_y_c],[z_[0] + g_x_c])
    #         to_print[z_[0] + g_x_c][z_[1] + g_y_c] = "#"

    # for e_, p_ in enumerate(parsed):
    #     if (p_[0] + g_x_c) in range(x_min,
    #                                 x_max + 1) and (p_[1] + g_y_c) in range(
    #                                     y_min, y_max + 1):
    #         print(f"{e_}: ({p_[0]}, {p_[1]})")
    #         to_print[p_[1] + g_y_c][p_[0] + g_x_c] = "S"
    #     if (p_[2] + g_x_c) in range(x_min,
    #                                 x_max + 1) and (p_[3] + g_y_c) in range(
    #                                     y_min, y_max + 1):
    #         to_print[p_[3] + g_y_c][p_[2] + g_x_c] = "B"

    # print(f"Sensors areas")
    # for p_ in to_print:
    #     print(''.join(p_))

    # return to_print, g_y_c

    return g_x_c, g_y_c, g_x_min, g_x_max, g_y_min, g_y_max

# to_print, g_y_c = get_every_sensors_area()

g_x_c, g_y_c, g_x_min, g_x_max, g_y_min, g_y_max = get_every_sensors_area()
print("g_x_c, g_y_c, g_x_min, g_x_max, g_y_min, g_y_max :", g_x_c, g_y_c,
      g_x_min, g_x_max, g_y_min, g_y_max)

in_area = set()

if len(sys.argv) > 1 and sys.argv[1] == 'p':
    reduced = [[x_[0], abs(x_[1] - 2_000_000), x_[4]] for x_ in parsed]
    for i_ in range(g_x_min - g_x_c, g_x_max + 1):
        # if i_ % 5_000 == 0:
        #     print(f"--- {i_} ---")
        for x_ in reduced:
            if (abs(x_[0] - i_) + x_[1]) <= x_[2]:
                in_area.add(i_)
                break

    # B (-85806, 2000000)
    in_area.remove(-85806)
else:
    reduced = [[x_[0], abs(x_[1] - 10), x_[4]] for x_ in parsed]
    for i_ in range(g_x_min - g_x_c, g_x_max + 1):
        for x_ in reduced:
            if (abs(x_[0] - i_) + x_[1]) <= x_[2]:
                in_area.add(i_)
                break

    # B (2, 10)
    in_area.remove(2)

# print("====== in_area:")
# for x_ in in_area:
#     print(x_)

print(f"part 1: {len(in_area)}")
# p --> 4811413

"""
--- Part Two ---
Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not detected by any sensor, but the distress beacon must have x and y coordinates each no lower than 0 and no larger than 4000000.

To isolate the distress beacon's signal, you need to determine its tuning frequency, which can be found by multiplying its x coordinate by 4000000 and then adding its y coordinate.

In the example above, the search space is smaller: instead, the x and y coordinates can each be at most 20. With this reduced search area, there is only a single position that could have a beacon: x=14, y=11. The tuning frequency for this distress beacon is 56000011.

Find the only possible position for the distress beacon. What is its tuning frequency?
"""

# RedPixel solution with z3 solver
from parse import parse
from z3 import *

with open(in_text + ".txt") as f:
    ls = f.read().splitlines()
sensors = [
    parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", l)
    for l in ls
]

# for s_ in sensors:
#     print(s_)

s = z3.Solver()
x = Int('x')
y = Int('y')

if len(sys.argv) > 1 and sys.argv[1] == 'p':
    ubound = 4_000_000
else:
    ubound = 20
s.add(x >= 0, x <= ubound)
s.add(y >= 0, y <= ubound)
for sx, sy, bx, by in sensors:
    d = abs(sx - bx) + abs(sy - by)
    s.add(Abs(sx - x) + Abs(sy - y) > d)
s.check()
m = s.model()

print(f"mx: {m[x].as_long()}, my: {m[y].as_long()}")

print(f"part 2: {m[x].as_long() * 4000000 + m[y].as_long()}")
# p --> 13171855019123
