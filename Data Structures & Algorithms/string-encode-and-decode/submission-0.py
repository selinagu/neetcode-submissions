class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ''
        for stri in strs:
            n = len(stri)
            encode = encode + str(n) + '#' + stri

        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        k = 0
        i = 0
        while i < len(s):
            if s[i] == "#":
                length = int(s[k: i])
                decode.append(s[i+1: i+length+1])
                k = i+length+1
                i = k
            else:
                i += 1

        return decode
