class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        num = len(strs)
        for s in zip(*strs):
            if len(set(s))==1:
                ans+=s[0]
            else:
                break
        return ans
      
      
#       Time complexity is 66ms & space complexity is 14MB
