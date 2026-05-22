class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str = encoded_str + str(len(s)) + "/:"
            for s_ in s:
                if s_ == '/':
                    encoded_str = encoded_str + '/'
                encoded_str = encoded_str + s_
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        len_ = ""
        while(i < len(s)):
            while(s[i] != '/'):
                len_ = len_ + s[i]
                i = i + 1
            i = i + 2
            len__ = int(len_)
            len_ = ""
            # print(len__)
            word = ""
            while(len__ > 0):
                if i < len(s) - 1 and s[i] == '/' and s[i+1] == '/':
                    i = i + 1
                word = word + s[i]
                len__ = len__ - 1
                i = i + 1
            # print(word)
            decoded_list.append(word)
            
        return decoded_list
