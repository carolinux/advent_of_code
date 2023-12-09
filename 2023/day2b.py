s = 0
const = {"blue": 14, "red": 12, "green": 13 }
with open("aoc2.txt", 'r') as f:
    i = 1
    for line in f.readlines():

        games = line.split(":")[1]
        valid = True
        games = games.split(";")
        const = {"blue": 0, "red": 0, "green": 0}
        for game in games:
            configs = game.split(",")
            for config in configs:
                config = config.strip().split(" ")
                num = int(config[0])
                color = config[1]
                const[color] = max(const[color], num)

        mult=1
        for color, pow in const.items():
            mult*=pow


        if valid:
            s+=mult
        i+=1



print(s)