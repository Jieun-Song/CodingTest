class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        len1, len2 = len(word1),len(word2)
        loop = min(len1, len2)

        for i in range(loop):
            result += word1[i]+word2[i]

        if len1>len2:
            result += word1[loop:]
        elif len1 < len2:
            result += word2[loop:]
            
        return result

