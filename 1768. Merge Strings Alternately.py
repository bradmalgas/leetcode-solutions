class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        shortest = min(len(word1), len(word2))
        for i in range(shortest):
            merged += word1[i]
            merged += word2[i]
        merged += word1[shortest:]
        merged += word2[shortest:]
        return merged
