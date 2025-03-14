class Solution:
    def reverseVowels(self, s: str) -> str:
        myStr = list(s)
        vowels = []
        consonants = []
        for i in myStr:
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                vowels.append(i)
                consonants.append(0)
                continue
            consonants.append(i)
        for j in range(len(consonants)):
            if consonants[j] == 0:
                consonants[j] = vowels.pop()

        return ''.join(consonants)