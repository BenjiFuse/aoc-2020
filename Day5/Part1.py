"""This part was easily verified by hand, but I coded before thinking"""

def get_seat(bpass):
    """returns a (row, col) int tuple for the given seat string"""
    row = line[:-3]
    row = row.replace('F', '0')
    row = row.replace('B', '1')
    row = int(row, 2)

    col = line[-3:]
    col = col.replace('L', '0')
    col = col.replace('R', '1')
    col = int(col, 2) 

    return row, col

with open('input.txt', 'r') as f:
    lines = f.read().split()
    max_id = 0

    for line in lines:
       row, col = get_seat(line)
       id = row*8 + col
       max_id = id if id > max_id else max_id

    print(max_id)