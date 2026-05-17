class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        i = 0
        j = length - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] == target:
                result = []
                result.append(i + 1)
                result.append(j + 1)
                return result
            else:
                i += 1