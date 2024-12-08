from collections import defaultdict

s = 4
center = ord('A') + s
triangle_table: dict[ int, list[set[tuple[tuple[chr, int], tuple[chr, int]]], chr] ]
def set_center(size: int):
    global s, center
    s = size
    center = ord('A') + s - 1
    init_triangle_table()

def init_triangle_table():
    global triangle_table
    triangle_table = { i - 65 : [['p', set()] for j in range(0, s*2 + (s - abs(center - i)*2) + 1) ] for i in range(65, 65+(s*2)-1) if i != center}


def check_for_triangles(links: list[tuple[tuple[chr, int], tuple[chr, int]]], direction: str, played_by: chr):

    for link in links:
        if ord(link[0][0]) < center:
            # Gornja polovina table
            ind = ord(link[0][0]) - 65

            if direction == 'D':
                triangle_table[ind][link[0][1] + link[1][1] - 2][1].add(link)
                if ind > 0:
                    triangle_table[ind - 1][link[0][1] + link[1][1] - 1 - 2][1].add(link)

            elif direction == 'DD':
                triangle_table[ind][(link[0][1]-1)*2][1].add(link)
                if ind + s > link[0][1]:
                    triangle_table[ind][(link[0][1]-1)*2 + 1][1].add(link)

            elif direction == 'DL':
                triangle_table[ind][link[0][1] * 2][1].add(link)
                if link[0][1] > 0:
                    triangle_table[ind][link[0][1] * 2  - 1][1].add(link)

        else:
            # Donja polovina table

            ind = ord(link[1][0]) - 65
            pind = 3 - ord(link[1][0]) + center
            if direction == 'D':
                triangle_table[ind][link[0][1] + link[1][1] - 2][1].add(link)
                if ind < (s-1)*2: # TODO: Test this
                    triangle_table[ind + 1][link[0][1] + link[1][1] - 2 - 1][1].add(link)

            elif direction == 'DD':
                triangle_table[ind][(link[0][1]-1) * 2][1].add(link)
                if link[0][1] > 1:
                    triangle_table[ind][(link[0][1]-1) * 2 - 1][1].add(link)

            elif direction == 'DL':
                triangle_table[ind][(link[1][1] - 1) * 2][1].add(link)
                if link[0][1] < pind + s:
                    triangle_table[ind][(link[1][1]-1) * 2 + 1][1].add(link)

    return triangle_table


# to_return.append(["x", ord(char) - ord('A'), (dLink[0][1] - 1) * 2, False])
def get_triangles():
    global triangle_table
    triangles = []
    # for entry in triangle_table:
        # TODO: ask FantomCek what is dLink[0][1] - 1
        # triangles.append(  [     t[0], entry,          for t in triangle_table[entry] if len(t[1]) == 3])
    return triangles

def test():
    set_center(4)

    # Nasumicni potezi za testiranje
    # check_for_triangles([(('G',1),('G',2)), (('F',1),('F',2)), (('A',1),('A',2)), (('B',1),('B',2))], 'D', 'X')
    # check_for_triangles([(('F',1),('G',1)), (('F',2),('G',2)), (('A',4),('B',5)), (('A',1),('B',2))], 'DD', 'O')
    # check_for_triangles([(('F', 2), ('G', 1)), (('F', 5), ('G', 4)), (('A', 1), ('B', 1)), (('A', 3), ('B', 3))], 'DL','X')

    # Potezi koji obrazuju trougao
    check_for_triangles([(('G', 1), ('G', 2))], 'D','X')
    check_for_triangles([(('F', 2), ('G', 2))], 'DD', 'X')
    check_for_triangles([(('F', 2), ('G', 1))], 'DL', 'X')

    for entry in triangle_table:
        print('   '* abs(center - 65 - entry) * 2, entry+65, ' : ' , end="    ")
        for t in triangle_table[entry]:
            print(t[0] if len(t[1]) == 3 else 'k', end='     ')
        print()

    for entry in triangle_table:
       print(entry, ' : ', triangle_table[entry] )

test()