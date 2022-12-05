"""
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?
"""

# with open('in_test.txt') as data:
with open('in.txt') as data:
    #inputs = [line.strip() for line in data.readlines()]
    inputs = [line.rstrip() for line in data.readlines()]

print(inputs[:9])

import re
commands_extractor = re.compile('\s*\w* (\d*) \w* (\d*) \w* (\d*)\s*')

cs = []
crates = []
commands = []
for x_ in inputs:
    if x_ != '':
        if x_.strip()[0] == '[':
            xr = x_.replace('    ', '[x] ').replace('][', '] [').replace('  ', ' ')
            print(xr)
            cs.append([c_[1] for c_ in xr.split(' ')])
        if x_.strip()[0] == '1':
            stacks = x_.strip().split('   ')
        if x_.strip()[0] == 'm':
            commands.append(
                list(commands_extractor.findall(x_)[0]))
# print(cs) # from inputs

# Transpose and reverse cs into stacks for pop and append use
for i_ in range(int(stacks[-1])):
    crates.append([cs[-(j_+1)][i_] for j_ in range(len(cs)) if i_ < len(cs[-(j_+1)])])
    while crates[-1][-1] == 'x':
        crates[-1].pop()

# print(crates)
# print(stacks)
# print(commands)

for c_ in commands:
    for _ in range(int(c_[0])):
        to_move = crates[stacks.index(c_[1])].pop()
        crates[stacks.index(c_[2])].append(to_move)
    # print(c_, crates)

print(f"part 1: {''.join(crates[i_][-1] for i_ in range(len(crates)))}")

"""
--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
"""
crates = []
# Transpose and reverse cs into stacks for pop and append use
for i_ in range(int(stacks[-1])):
    crates.append([
        cs[-(j_+1)][i_] for j_ in range(len(cs)) if i_ < len(cs[-(j_+1)])
    ])
    while crates[-1][-1] == 'x':
        crates[-1].pop()

# print(crates)
# print(stacks)
# print(commands)

for c_ in commands:
    to_move = []
    for _ in range(int(c_[0])):
        to_move.append(crates[stacks.index(c_[1])].pop())
    for i_ in range(len(to_move)):
        crates[stacks.index(c_[2])].append(to_move[-(i_+1)])
    # print(c_, crates)

print(f"part 2: {''.join(crates[i_][-1] for i_ in range(len(crates)))}")
