class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ''
        for s in strs:
            encode = encode + str(len(s)) + '#' + s

        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        j = 0

        while i < len(s):
            while s[i] != '#':
                i += 1

            length = int(s[j:i])
            decode.append(s[i+1: i+length+1])

            i = i+length+1
            j = i

        return decode