=begin
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
=end

# inputs = File.read('in_test.txt').split("\n")
inputs = File.read('in.txt').split("\n")
p inputs.first(9)

cs = []
crates = []
commands = []
stacks = []
inputs.each do |x_|
  # p x_
  next if x_.strip == ''

  if x_.strip[0] == '['
    xr = x_.gsub('    ', '[x] ').gsub('][', '] [').gsub('  ', ' ')
    p xr
    cs.append([])
    xr.split(' ').each do |c_|
      cs[-1].append(c_[1])
    end
  end

  stacks = x_.strip.split('   ') if x_.strip[0] == '1'
  commands.append(/\s*\w* (\d*) \w* (\d*) \w* (\d*)\s*/.match(x_).to_a) if x_.strip[0] == 'm'
end

# p cs # from inputs

# p crates
# p stacks
# p commands

# Transpose and reverse cs into stacks for pop and append use
(0...stacks[-1].to_i).to_a.each do |i_|
  crates.append([])
  (0...cs.size).to_a.each do |j_|
    crates[-1].append(cs[-(j_ + 1)][i_]) if i_ < cs[-(j_ + 1)].size
  end
  crates[-1].pop while crates[-1][-1] == 'x'
end
puts 'Crates after transpose'
p crates

saved_crates = crates.collect { |x| x.collect { |_| _ } }

commands.each do |c_|
  # p c_
  (0...(c_[1].to_i)).to_a.each do |_|
    crates[stacks.index(c_[3])].append(crates[stacks.index(c_[2])].pop)
  end
  # p crates
end

top_crates = []
(0...crates.size).to_a.each { |i_| top_crates.append(crates[i_][-1]) }
puts 'Top crates after commands'
p top_crates

puts "part 1: #{top_crates.join}"

=begin
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
=end

crates = []
saved_crates.each { |cs_| crates.append(cs_.reverse) }
puts 'Crates reversed'
p crates

commands.each do |c_|
  # p c_
  n = c_[1].to_i
  crates[stacks.index(c_[3])] = crates[stacks.index(c_[2])].take(n) + crates[stacks.index(c_[3])]
  crates[stacks.index(c_[2])] = crates[stacks.index(c_[2])].drop(n)
  # p crates
end

top_crates = []
(0...crates.size).to_a.each { |i_| top_crates.append(crates[i_][0]) }
puts 'Top crates after commands'
p top_crates

puts "part 2: #{top_crates.join}"
