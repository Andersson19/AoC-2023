import helper as h

GLOBAL_MATRIX = []

def get_fullnumber(y,x,value):
    curr_left = x-1
    curr_right = x+1
    min_left = 0
    max_right = len(GLOBAL_MATRIX[y]) - 1
    done_left = False
    done_right = False

    result = str(value)
    # check left
    while(curr_left >= min_left and not done_left):
        tmp = GLOBAL_MATRIX[y][curr_left]
        if tmp.isdigit():
            result = str(tmp) + result
            curr_left -= 1
        else:
            done_left = True

    while(curr_right <= max_right and not done_right):
        tmp = GLOBAL_MATRIX[y][curr_right]
        if tmp.isdigit():
            result = result + str(tmp)
            curr_right += 1
        else:
            done_right = True

    return int(result)

def get_numbers(x,y):
    up = GLOBAL_MATRIX[y-1][x]
    up_left = GLOBAL_MATRIX [y-1][x-1]
    up_right = GLOBAL_MATRIX[y-1][x+1]
    down = GLOBAL_MATRIX[y+1][x]                # what a dork lmao
    down_left = GLOBAL_MATRIX[y+1][x-1]
    down_right = GLOBAL_MATRIX[y+1][x+1]
    left = GLOBAL_MATRIX[y][x-1]
    right = GLOBAL_MATRIX[y][x+1]

    all_symbols = [left, right]

    if up.isdigit():
        all_symbols.append(up)
    else:
        all_symbols.append(up_left)
        all_symbols.append(up_right)

    if down.isdigit():
        all_symbols.append(down)
    else:
        all_symbols.append(down_left)
        all_symbols.append(down_right)

    
    if len(list(filter(lambda x: x.isdigit(), all_symbols))) != 2:
        return 0

    value1 = value2 = 0

    if up.isdigit():
        value1 = get_fullnumber(y-1,x,up)
    else:
        if up_left.isdigit():
            value1 = get_fullnumber(y-1,x-1,up_left)                   # need to check for number on left
        if up_right.isdigit():
            if value1 > 0:
                value2 = get_fullnumber(y-1,x+1,up_right)
                return value1 * value2
            else:
                value1 = get_fullnumber(y-1,x+1,up_right)                  # and to check for number on right

    if down.isdigit():
        if value1 > 0:
            value2 = get_fullnumber(y+1,x,down) # fullnumber is guaranteed here and only here
            return value1 * value2
        else:
            value1 = get_fullnumber(y+1,x,down)
    else:
        if down_left.isdigit():                 # need to check for number on left
            if value1 > 0:
                value2 = get_fullnumber(y+1,x-1,down_left) 
                return value1 * value2
            else:
                value1 = get_fullnumber(y+1,x-1,down_left) 
                
        if down_right.isdigit():                # and to check for number on right
            if value1 > 0:
                value2 = get_fullnumber(y+1,x+1,down_right)
                return value1 * value2
            else:
                value1 = get_fullnumber(y+1,x+1,down_right)

    if left.isdigit():
        if value1 > 0:
            value2 = get_fullnumber(y,x-1,left)   # left is guaranteed here and only here
            return value1 * value2
        else:
            value1 = get_fullnumber(y,x-1,left)   # left is guaranteed here and only here

    value2 = get_fullnumber(y,x+1,right) # right is guaranteed here and only here
    return value1 * value2

if __name__ == "__main__":
    lines = h.read_file('./inputs/3.txt')
    # lines = h.read_file('./inputs/3-test')
    
    symbols = ['*']

    for line in lines:
        arr = []
        for char in line:
            arr.append(char)
        GLOBAL_MATRIX.append(arr)

    sum = 0
    for y, arr in enumerate(GLOBAL_MATRIX):
        for x, char in enumerate(arr):
            if char in symbols:
                sum += get_numbers(x,y)

    print("sum:{}".format(sum))