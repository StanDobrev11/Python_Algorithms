def binary_find_target_index(nums, target, left_idx, right_idx):
    middle_idx = (right_idx + left_idx) // 2
    middle_el = nums[middle_idx]

    if target == middle_el:
        print(middle_idx)
        return
    if left_idx > right_idx:
        print(-1)
        return

    if target > middle_el:
        left_idx = middle_idx + 1
        binary_find_target_index(nums, target, left_idx, right_idx)

    else:
        right_idx = middle_idx - 1
        binary_find_target_index(nums, target, left_idx, right_idx)


nums = [int(x) for x in input().split()]
target = int(input())
binary_find_target_index(nums, target, 0, len(nums) - 1)
