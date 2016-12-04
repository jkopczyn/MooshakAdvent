
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
        print first_coord, second_coord
        for pair in segments:
            if check_intersection(pair, [first_coord, second_coord]):
                return "crossing" 
        segments.append([first_coord, second_coord])
    return "not crossing"

def coord(string):
    return [int(s) for s in string.split(',')]

def check_intersection(first_line, second_line):
    first_left, first_right = [coord[0] for coord in sorted(first_line)]
    second_left, second_right = [coord[0] for coord in sorted(second_line)]
    first_bottom, first_top = [coord[1] for coord in sorted(first_line, key=lambda x: x[1])]
    second_bottom, second_top = [coord[1] for coord in sorted(second_line, key=lambda x: x[1])]
    if first_left >= second_right or second_left >= first_right:
        return False
    if first_bottom >= second_top or second_bottom >= first_top:
        return False
    return True

print main()
