import helper as h

def get_game(line):
    lines = line.split(": ")
    return lines[1]

def get_sets(line):
    return line.split("; ")

def get_minimum_possible(set, min_blue, min_green, min_red):
    colors = set.split(", ")
    
    for color in colors:
        color_and_amount = color.split(" ")
        color = color_and_amount[1]
        amount = int(color_and_amount[0])

        match color:
            case "blue":
                if amount > min_blue:
                    min_blue = amount
            case "green":
                if amount > min_green:
                    min_green = amount
            case "red":
                if amount > min_red:
                    min_red = amount
        
    return min_blue,min_green,min_red

def calc_power(game):
    sets = get_sets(game)

    blue = 0
    green = 0
    red = 0

    for set in sets:
        blue, green, red = get_minimum_possible(set, blue, green, red)

    return blue*green*red

def solve(lines):
    sum = 0
    for line in lines:
        line = line.strip()
        game = get_game(line)
        sum += calc_power(game)
    print(sum)

if __name__ == "__main__":
    path = './inputs/2.txt'
    test = './inputs/2-test.txt'

    lines = h.read_file(path)
    solve(lines)