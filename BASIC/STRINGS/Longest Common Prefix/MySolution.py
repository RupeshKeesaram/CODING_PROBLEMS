class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs.sort(key=len)
        for i in range(len(strs[0])):
            count=0
            for j in range(len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                    f=1
                    break
                else:
                    count+=1
            else:
                j=0
                f=0
            if(f==1):
                break
            if(count==len(strs)-1):
                ans+=strs[j][i]
        return ans
