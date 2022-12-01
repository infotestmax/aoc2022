inputs = File.read('in.txt').split("\n")

# p inputs
calories = []
start = 0
tmp_sum = 0
inputs.each_with_index do |item, i|
  if inputs[i] == ''
    calories.append(tmp_sum)
    tmp_sum = 0
  else
    tmp_sum += inputs[i].to_i
  end
  calories.append(tmp_sum) if tmp_sum != 0 and i == inputs.size - 1
end

# p calories
puts "part 1: #{calories.max}"

puts "part 2: #{calories.sort{ |a, b| a <=> b }.last(3).sum}"
