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

