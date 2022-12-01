with open('in.txt') as data:
    inputs = [line.strip() for line in data.readlines()]
# print(inputs)

calories = []
tmp_sum = 0
last_index =  len(inputs) - 1
for i_ in range(len(inputs)):
    if inputs[i_] == "":
        calories.append(tmp_sum)
        tmp_sum = 0
    else:
        # print(inputs[i_])
        tmp_sum += int(inputs[i_])
    if i_ == last_index and tmp_sum != 0:
        calories.append(tmp_sum)

# print(calories)
print(f"part 1: {max(calories)}")

# print(sorted(calories)[-3:])
print(f"part 2: {sum(sorted(calories)[-3:])}")
