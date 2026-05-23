class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = [[strs[0]]]
        for i in range(1, len(strs)):
            found = False
            str_sorted = sorted(list(strs[i]))
            for group in output:
                if str_sorted == sorted(list(group[0])):
                    group.append(strs[i])
                    found = True
            if not found:
                output.append([strs[i]])

        return output
