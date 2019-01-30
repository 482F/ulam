def NoD_list(mn):
    num_list = [1 for x in range(mn)]
    num_list[0] = 0
    for index in range(1, mn):
        if num_list[index] == 1:
            for mul_num in range(2, mn // (index + 1) + 1):
                num_list[mul_num * (index + 1) - 1] += 1
    return num_list
    #mn = 10 -> [0, 1, 1, 2, 1, 3, 1, 2, 2,  3]
    #           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def start_pos(mr, mc):
    return [mr - 1, mc - 1]

def make_direction(mr, mc):
    return [-1, 0]

def make_width(mr, mc):
    return [mr - 1, mc - 1]

def next_direction(current_direction):
    current_direction = tuple(current_direction)
    direction_dict = {
            (-1, 0): [0, -1],
            (0, -1): [1, 0],
            (1, 0): [0, 1],
            (0, 1): [-1, 0],
            }
    return direction_dict[current_direction]
def pos_list(mr, mc):
    num = 1
    pos = start_pos(mr, mc)
    pos_list = [pos[:]]
    direction = make_direction(mr, mc)
    width = make_width(mr, mc)
    current_width = width[:]
    width[0] += 1
    index = 0
    while (num <= (mr * mc) - 1):
        if (current_width[index] == 0):
            width[index] -= 1
            current_width = width[:]
            direction = next_direction(direction)
            index = [1, 0][index]
        current_width[index] -= 1
        num += 1
        pos[index] += direction[index]
        pos_list.append(pos[:])
    return pos_list[::-1]
print(pos_list(4, 3))

