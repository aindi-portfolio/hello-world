#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def leetcode(nums):
    if len(nums) == 0:
        return False
    else:
        s_one = set(nums)
        return len(s_one) == len(nums)


print(leetcode([1,2,3,4,5,1])) # false