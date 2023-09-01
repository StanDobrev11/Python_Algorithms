def gen_vector(idx, vector):
    if idx == len(vector):
        print(*vector, sep=' ')
        return

    for num in range(1, len(vector) + 1):
        vector[idx] = num
        gen_vector(idx + 1, vector)


n = int(input())

vector = [1] * n

gen_vector(0, vector)