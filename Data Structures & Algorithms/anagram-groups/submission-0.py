class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        empty_list = []

# seen[sorted_str]:list[str, str, str]
        for n in strs:
            sorted_str = "".join(sorted(n))

            if sorted_str in seen:
                seen[sorted_str].append(n)
            else:
                seen[sorted_str] = [n]


        for element in seen.values():
            empty_list.append(element)

        return empty_list
        

