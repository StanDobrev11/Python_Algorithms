nums = [int(x) for x in input().split()]  # [5, 4, 3, 2, 1, 6, 0, 6, -2]

for idx in range(len(nums)):
    # current_num = nums[idx]
    for next_idx in range(idx + 1, len(nums)):

        if nums[idx] > nums[next_idx]:
            nums[idx], nums[next_idx] = nums[next_idx], nums[idx]

print(*nums)