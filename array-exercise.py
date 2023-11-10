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
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(maxSubArray(nums))


# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements
# NB: you must do this in-place without making a copy of the array

def moveZeros(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0 and nums[count] == 0:
            nums[count], nums[i] = nums[i], nums[count]

        if nums [count] != 0:
            count += 1
    return nums

# nums = [0, 1, 0, 3, 12]
# print(moveZeros(nums))

# Given an integer array nums, return true if any value appears at least twice in the array and return false if every element
# is distinct

def containsDuplicate(nums):
    mydict = {}
    for i in range(len(nums)):
        if nums[i] in mydict.values():
            return True
        else:
            mydict[i] = nums[i]

nums = [3,3]
# nums = [0, 1, 0, 3, 12]
print(containsDuplicate(nums))