def read_file(path):
    file = open(path, 'r')
    lines = file.readlines()
    return [x.strip() for x in lines]

def print_file(path):
    file = open(path,'r')
    for line in file.readlines():
        print(line)