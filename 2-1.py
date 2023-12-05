import helper as h

GLOBAL_MAX_RED = 12
GLOBAL_MAX_GREEN = 13
GLOBAL_MAX_BLUE = 14

def get_game_id(line):
    lines = line.split(" ")
    return int(lines[1][:-1])

def get_game(line):
    lines = line.split(": ")
    return lines[1]

def get_sets(line):
    return line.split("; ")

def set_possible(set):
    colors = set.split(", ")
    
    for color in colors:
        color_and_amount = color.split(" ")
        color = color_and_amount[1]
        amount = color_and_amount[0]

        match color:
            case "blue":
                if int(amount) > GLOBAL_MAX_BLUE:
                    return False
            case "green":
                if int(amount) > GLOBAL_MAX_GREEN:
                    return False
            case "red":
                if int(amount) > GLOBAL_MAX_RED:
                    return False
        
    return True

def game_is_possible(game):
    sets = get_sets(game)

    for set in sets:
        if not set_possible(set):
            return False
    return True

def solve(lines):
    sum = 0
    for line in lines:
        line = line.strip()
        game = get_game(line)
        game_id = get_game_id(line)
        if game_is_possible(game):
            sum += game_id
    print(sum)

if __name__ == "__main__":
    path = './inputs/2.txt'
    test = './inputs/2-test.txt'

    lines = h.read_file(path)
    solve(lines)