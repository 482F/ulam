from PIL import Image


def NoD_list(mn):
    progress = 0.1
    num_list = [1 for x in range(mn)]
    num_list[0] = 0
    for index in range(1, mn):
        if num_list[index] == 1:
            for mul_num in range(2, mn // (index + 1) + 1):
                num_list[mul_num * (index + 1) - 1] += 1
        if (mn * progress <= index):
            print("NoD_list: ", index , "/" , mn, ", " , int(progress * 10), "0%", sep="")
            progress += 0.1
    return num_list
    #mn = 10 -> [0, 1, 1, 2, 1, 3, 1, 2, 2,  3]
    #           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def start_pos(mx, my):
    return [mx - 1, my - 1]

def make_direction(mx, my):
    return [-1, 0]

def make_width(mx, my):
    return [mx - 1, my - 1]

def next_direction(current_direction):
    current_direction = tuple(current_direction)
    direction_dict = {
            (-1, 0): [0, -1],
            (0, -1): [1, 0],
            (1, 0): [0, 1],
            (0, 1): [-1, 0],
            }
    return direction_dict[current_direction]
def pos_list(mx, my):
    num = 1
    pos = start_pos(mx, my)
    pos_list = [pos[:]]
    direction = make_direction(mx, my)
    width = make_width(mx, my)
    current_width = width[:]
    width[0] += 1
    index = 0
    progress = 0.1
    mn = mx * my
    while (num <= (mn) - 1):
        if (current_width[index] == 0):
            width[index] -= 1
            current_width = width[:]
            direction = next_direction(direction)
            index = [1, 0][index]
        current_width[index] -= 1
        num += 1
        pos[index] += direction[index]
        pos_list.append(pos[:])
        if (mn * progress <= num):
            print("pos_list: ", num , "/" , mn, ", " , int(progress * 10), "0%", sep="")
            progress += 0.1
    return pos_list[::-1]

def normalization(target):
    ma = max(target)
    mi = min(target)
    return [int((num - mi) / ma * 255) for num in target]

mx = 1920
my = 1080
img = Image.new('RGB', (mx, my))
poss = pos_list(mx, my)
NoDs = normalization(NoD_list(mx * my))
for num in range(mx * my):
    color = NoDs[num]
    color = [color for k in range(3)]
    img.putpixel(tuple(poss[num]), tuple(color))
img.show()
img.save("ulam.png")
