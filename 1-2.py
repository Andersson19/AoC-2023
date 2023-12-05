import helper as h
import re

path = './inputs/1.txt'
path_test = './inputs/1-test.txt'

def convert_to_int(n):
    match n:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
        case _:
            return n
        

    
def slow_solve(line):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    my_regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
    print(re.findall(my_regex, line));
    'nineight'
    dict = {}

    for number in numbers:
        if number in line:
            start_index = line.find(number)
            last_index = line.rfind(number)
            dict[number] = (start_index, last_index)
        
    lowest_index = 999999
    highest_index = -1
    lowest_number = ""
    highest_number = ""

    for key in dict.keys():
        start_index, last_index = dict[key]
        if start_index < lowest_index:
            lowest_index = start_index
            lowest_number = key
        if last_index > highest_index:
            highest_index = last_index
            highest_number = key


    if not lowest_number.isdigit():
        lowest_number = convert_to_int(lowest_number)
    if not highest_number.isdigit():
        highest_number = convert_to_int(highest_number)

    
    return int(lowest_number+highest_number)

def solve():
    lines = h.read_file(path)
    sum = 0

    for line in lines:
        sum += slow_solve(line.strip())

    print(sum)

if __name__ == '__main__':
    solve()