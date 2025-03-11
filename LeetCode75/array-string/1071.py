class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        gong = []
        for i in range(1, max(len1,len2)+1):
            if (len1%i==0)and(len2%i==0):
                gong.append(i)
        print(gong)
        
        for _ in range(len(gong)):
            result = gong.pop()
            gongStr = str1[:result]
            
            myStr1 = gongStr*(len1//result)
            myStr2 = gongStr*(len2//result)

            if (myStr1 == str1)and(myStr2 == str2):
                return gongStr
        return ""