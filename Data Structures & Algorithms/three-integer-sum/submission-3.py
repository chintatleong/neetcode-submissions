class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []

        for i in range(len(sorted_nums)):
            # Skip duplicate i values, as same value
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            j = i + 1
            k = len(sorted_nums) - 1


            while j < k:
                total = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if total == 0:
                    combo = []
                    combo.append(sorted_nums[i])
                    combo.append(sorted_nums[j])
                    combo.append(sorted_nums[k])
                    result.append(combo)

                    # move once, just need to update either one of the pointer
                    # because next loop will handle the rest
                    j += 1

                elif total < 0:
                    j += 1
                else:
                    k -= 1
        
        return result
            
        
