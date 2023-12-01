with open("input.txt") as f:
    data = f.read().split("\n")

# Test Data
# data = [
#     "two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen",
# ]

total = 0

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for line in data:
    numbers = []

    for i in range(len(line)):
        char = line[i]
        if char.isnumeric():
            numbers.append(int(char))
        else:
            for key in nums:
                if line.startswith(key, i):
                    numbers.append(nums[key])

    if len(numbers) > 0:
        total += (numbers[0] * 10) + numbers[-1]

print(total)
