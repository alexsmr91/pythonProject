

def get_uniq_numbers(src: list):
    tmp = set()
    unq = set()
    for el in src:
        if el in tmp:
            unq.discard(el)
        else:
            unq.add(el)
        tmp.add(el)
    return [x for x in src if x in unq]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))

