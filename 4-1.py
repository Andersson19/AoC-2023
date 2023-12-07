import helper as h

def get_points(winning, numbers, game_id):
    result = 0
    tmp_winning = []
    for number in numbers:
        if number in winning:
            if number not in tmp_winning and number != ' ':
                tmp_winning.append(number)
                if result == 0:
                    result += 1
                else:
                    result *= 2

    print("Game {}: winning: {} and our winning numbers: {} gives: {} points".format(game_id, winning, tmp_winning, result))

    return result

if __name__ == "__main__":
    path = "./inputs/4.txt"
    test = "./inputs/4-test.txt"

    lines = h.read_file(path)
    sum = 0
    for idx, line in enumerate(lines):
        card_numbers = line.split(": ")[1]
        winning = list(filter(lambda x: x.isdigit(), card_numbers.split(" | ")[0].split(" ")))
        numbers = list(filter(lambda x: x.isdigit(), card_numbers.split(" | ")[1].split(" ")))
        sum += get_points(winning, numbers, idx+1)

    print(sum)