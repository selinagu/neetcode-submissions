from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for s in strs:
            output[tuple(sorted(s))].append(s)

        return list(output.values())