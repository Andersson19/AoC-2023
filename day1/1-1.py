import helper as h

path = './inputs/1.txt'

def quick_solve(line):
    first = line[0]
    last = line[-1]

    return first.isdigit() and last.isdigit()

def slow_solve(line):
    first = -1
    last = -1

    for char in line:
        if char.isdigit():
            if first == -1:
                first = char
            else:
                last = char
    
    if last == -1:
        return int(first+first)
    else:
        return int(first+last)

def solve():
    lines = h.read_file(path)
    sum = 0

    for line in lines:
        line = line.strip()
        if quick_solve(line):
            sum += int(line[0]+line[-1])
        else:
            sum += slow_solve(line)
        
    print(sum)

if __name__ == '__main__':
    solve()