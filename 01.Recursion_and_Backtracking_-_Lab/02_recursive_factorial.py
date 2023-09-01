def calc_fact(x):
    if x == 0:
        return 1
    return x * calc_fact(x - 1)


n = int(input())
print(calc_fact(n))
