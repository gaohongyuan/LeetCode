# Next Greater Element II

# O(n); two loops; store index instead of value due to duplication

# Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
#
# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                d[stack.pop()] = nums[i]
            stack.append(i)

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                d[stack.pop()] = nums[i]
            if stack == []:
                break

        return map(lambda x: d[x] if x in d else -1, range(len(nums)))
        # This return clause above can be replaced with the following for more readability:
        #
        # res = []
        # for i in range(len(nums)):
        #     if i in d:
        #         res.append(d[i])
        #     else:
        #         res.append(-1)
        # return res
