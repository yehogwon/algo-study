nums = [0,1,0,3,12]

non_zeros = [item for item in nums if item != 0]
zeros = [item for item in nums if item == 0]
nums = non_zeros + zeros

print(non_zeros, zeros, nums)