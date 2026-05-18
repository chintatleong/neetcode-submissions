class Solution:

    def encode(self, strs: List[str]) -> str:
        full = ""
        for string in strs:
            full = str(len(string)) + full + string 
        return full 
        
    def decode(self, s: str) -> List[str]:
        str_list = []

        start = 0
        length = int(s[0])
        count = 0

        for n in s:
            string = ""
            string = string + n
            count += 1

            if count == length:
                if n.isdigit():
                    length = int(n)
                count = 0
                str_list.append(string)
            
        
        return str_list
