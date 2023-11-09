# Leetcode exercise
# Given an array of integers nums and a target, return indeces of the two numbers such that they add up to target
def twoSums(nums, target):
    output = []
    track = 0
    while track < len(nums):
        for i in range(track+1, len(nums)-1):
            if nums[track] + nums[i] == target:
                output.append(nums[track])
                output.append(nums[i])
                break
        track += 1
    return output

nums = [2, 7, 11, 15]
target = 9

print(twoSums(nums, target))
