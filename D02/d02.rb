=begin
--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.
=end

# inputs = File.read('in_test.txt').split("\n")
inputs = File.read('in.txt').split("\n")

# p inputs
outcomes = { 0 => ['A Z', 'B X', 'C Y'], 3 => ['A X', 'B Y', 'C Z'], 6 => ['A Y', 'B Z', 'C X'] }
shapes = { 'X' => 1, 'Y' => 2, 'Z' => 3 }
score = 0
inputs.each do |x|
  outcomes.each { |k, items| score += k if items.include? x }
  score += shapes[x[-1]]
end

puts "part 1: #{score}"

=begin
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.
=end

strategies = { 'X' => 0, 'Y' => 3, 'Z' => 6 }
outcomes = { 0 => ['A C', 'B A', 'C B'], 3 => ['A A', 'B B', 'C C'], 6 => ['A B', 'B C', 'C A'] }
shapes = { 'A' => 1, 'B' => 2, 'C' => 3 }
score = 0
inputs.each do |x|
  # p x
  # p x[-1]
  # p strategies[x[-1]]
  # p outcomes[strategies[x[-1]]]
  outcomes[strategies[x[-1]]].each do |item|
    next if item[0] != x[0]

    score += strategies[x[-1]]
    score += shapes[item[-1]]
    # p score
  end
end

puts "part 2: #{score}"
