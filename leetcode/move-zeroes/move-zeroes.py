nums = [0, 1]

if nums[0] == 0: 
    for i in range(1, len(nums)): 
        if nums[i] != 0: 
            nums[0] = nums[i]
            nums[i] = 0
            break

i, j = len(nums) - 1, len(nums) - 1 # i and j are pointers for non-zeroes and zeroes, respectively
while i >= 0 and j >= 0: 
    if nums[i] == 0: 
        i -=1
        continue
    if nums[j] != 0 or i > j: 
        j -= 1
        continue
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t

print(nums)