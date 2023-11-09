# Leetcode exercise
# Given an array of integers nums and a target, return indeces of the two numbers such that they add up to target
def twoSums(nums, target):
    output = []
    track = 0
    while track < len(nums):
        for i in range(track+1, len(nums)):
            if nums[track] + nums[i] == target:
                output.append(track)
                output.append(i)
                break
        track += 1
    return output

def twoSumOptimized(nums, target):
    mydict = {}
    for i, n in enumerate(nums):
        if n in mydict:
            return [mydict[n], i]
        else:
            mydict[target - n] = i 

# nums = [2, 7, 11, 15]
# nums = [3, 2, 4]
# target = 6

# print(twoSumOptimized(nums, target))
# print(twoSums(nums, target))

# Given an integer array nums, find the subarray with the largest sum and return its sum
def maxSubArray(nums):
    maxSum = float('-inf')
    currentSum = 0

    for num in nums:
        currentSum += num
        if currentSum > maxSum:
            maxSum = currentSum

        if currentSum < 0:
            currentSum = 0

    return maxSum
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
