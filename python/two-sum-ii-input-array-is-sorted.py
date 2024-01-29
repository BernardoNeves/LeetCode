class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers)-1
        current_sum = numbers[i] + numbers[j]
        while current_sum != target:
            if current_sum < target:
                i += 1
            else:
                j -= 1
            current_sum = numbers[i] + numbers[j]
        return [i+1, j+1]
