def duck_duck_goose(players, goose):
    return players[(goose % len(players) - 1)].name

print(duck_duck_goose(['a', 'b', 'c', 'd'], 1))

