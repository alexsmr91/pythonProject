
def get_numbers(src: list):
    return (src[i] for i in range(1, len(src)) if (src[i] > src[i-1]))


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))

