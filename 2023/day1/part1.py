with open("input.txt") as f:
    data = f.read().split("\n")

# Test Data
# data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

total = 0

for line in data:
    numbers = []
    for char in line:
        if char.isnumeric():
            numbers.append(int(char))
    if len(numbers) > 0:
        total += (numbers[0] * 10) + numbers[-1]

print(total)
