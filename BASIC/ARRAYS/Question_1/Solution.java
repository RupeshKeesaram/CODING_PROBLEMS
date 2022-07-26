class Solution {
    public int[] runningSum(int[] nums) {
        
        // declaring a simple array of length nums
      
        int[] ans = new int[nums.length];
      
      // main logic
        for(int i=0;i<nums.length;i++)
        {
            if(i==0)
                ans[i]=nums[i];
            else
                ans[i]=ans[i-1]+nums[i];
        }
     
        return ans;
    }
}
