def calc_sum(array, idx):
    if idx == len(array) - 1:
        return array[idx]
    return array[idx] + calc_sum(array, idx + 1)


array = [int(i) for i in input().split()]

print(calc_sum(array, 0))
