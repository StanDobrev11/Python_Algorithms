nums = [int(x) for x in input().split()]
# nums = [5, 4, 3, 2, 1, 6, 0, 6, -2]

for i in range(1, len(nums)):
    for j in range(i - 1, -1, -1):
        if nums[j] > nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
        i -= 1

print(*nums)