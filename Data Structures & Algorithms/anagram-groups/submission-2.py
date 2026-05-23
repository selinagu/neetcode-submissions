class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for word in strs:
            count[tuple(sorted(word))].append(word)

        return list(count.values())