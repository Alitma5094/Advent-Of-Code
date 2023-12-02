with open("input.txt") as f:
    data = f.read().split("\n")

# Test Data
# data = [
#     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
# ]

total = 0

for game in data:
    game_id = int(game.split(":")[0].split()[1])
    max_red = 0
    max_green = 0
    max_blue = 0

    rounds = game.split(":")[1].strip()

    for round in rounds.split(";"):
        for pull in round.strip().split(","):
            color = pull.strip().split()[1]
            value = int(pull.strip().split()[0])
            if color == "red" and value > max_red:
                max_red = value
            elif color == "green" and value > max_green:
                max_green = value
            elif color == "blue" and value > max_blue:
                max_blue = value

    total += max_red * max_green * max_blue


print(total)
