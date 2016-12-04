
segments = []
def main():
    while(True):
        item = raw_input().strip()
        if not item:
            break
        if not segments:
            first_coord = coord(item)
            item = raw_input().strip()
            second_coord = coord(item)
        else:
            second_coord = coord(item)
            first_coord = segments[-1][1]
        for pair in segments:
            if check_intersection(pair, [first_coord, second_coord]):
                return "crossing" 
        segments.append([first_coord, second_coord])
    return "not crossing"

def coord(string):
    return [0,0]

def check_intersection(first_line, second_line):
    return True

print main()
