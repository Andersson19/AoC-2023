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

    north = 0
    south = 0

    if up.isdigit():
        north += get_fullnumber(y-1,x,up)   # fullnumber is guaranteed here and only here
    else:
        if up_left.isdigit():                   # need to check for number on left
            north += get_fullnumber(y-1,x-1,up_left)
        if up_right.isdigit():                  # and to check for number on right
            north += get_fullnumber(y-1,x+1,up_right) 

    if down.isdigit():
        south += get_fullnumber(y+1,x,down) # fullnumber is guaranteed here and only here
    else:
        if down_left.isdigit():                 # need to check for number on left
            south += get_fullnumber(y+1,x-1,down_left) 
        if down_right.isdigit():                # and to check for number on right
            south += get_fullnumber(y+1,x+1,down_right)

    if left.isdigit():                      
        left = get_fullnumber(y,x-1,left)   # left is guaranteed here and only here
    else:
        left = 0
    if right.isdigit():
        right = get_fullnumber(y,x+1,right) # right is guaranteed here and only here
    else:
        right = 0

    return north+south+left+right           # break it down and sum it for me boy

if __name__ == "__main__":
    lines = h.read_file('./inputs/3.txt')
    # lines = h.read_file('./inputs/3-test')
    
    # distinct chars from lines (excl. '.' and digits)
    symbols = ['*', '+', '=', '%', '-', '#', '@', '/', '&', '$']

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