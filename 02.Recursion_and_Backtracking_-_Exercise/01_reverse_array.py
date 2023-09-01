def rev_array(array, new_array, idx):
    if len(new_array) == len(array):
        print(*new_array, sep=' ')
        return
    new_array.insert(0, array[idx])
    rev_array(array, new_array, idx + 1)


array = list(input().split())
new_array = []
rev_array(array, new_array, 0)
