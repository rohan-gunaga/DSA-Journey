class Solution(object):
    def longestCommonPrefix(self, strs):

        first = strs[0]

        for i in range(len(first)):
            for word in strs[1:]:
                if i >= len(word) or first[i] != word[i]:
                    return first[:i]

        return first

