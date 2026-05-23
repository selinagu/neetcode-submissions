class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for s in strs:
            encode.append(str(len(s)))
            encode.append('#')
            encode.append(s)

        return "".join(encode)

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i: j])
            start = j+1
            decode.append(s[start: start+length])
            i = start + length

        return decode
