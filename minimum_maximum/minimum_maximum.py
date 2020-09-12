def run():
    inputs = [1, 2, 3, 4, 5]
    print(minimum_maximum(inputs))


def minimum_maximum(ent: list):
    min_list = [ent[0]]
    max_list = [ent[0]]

    for i in range(1, len(ent)):
        min_list.append(ent[i])
        min_list.sort()
        min_list = min_list[:4]

        max_list.append(ent[i])
        max_list.sort(reverse=True)
        max_list = max_list[:4]

    return f'{sum(min_list)} {sum(max_list)}'
