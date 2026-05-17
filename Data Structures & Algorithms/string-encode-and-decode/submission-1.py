class Solution:

    def encode(self, strs: List[str]) -> str:
        full = ""
        for string in strs:
            full = full + str(len(string)) + "#" + string 
        return full 
        
    def decode(self, s: str) -> List[str]:
        str_list = []
        i = 0

        while i < len(s):
            length_str = ""
            while s[i] != "#":
                length_str += s[i]
                i += 1

            length = int(length_str)

            # 2️⃣ Skip '#'
            i += 1

            # 3️⃣ Read exactly 'length' characters
            string = ""
            for _ in range(length):
                string += s[i]
                i += 1

            str_list.append(string)
        
        return str_list
