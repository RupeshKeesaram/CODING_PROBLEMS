class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] memo = new int[target+1];
        memo[0] = 1;
        
        for(int i=0;i<=target;i++)
        {
            for(int num:nums)
            {
                if(num<=i)
                {
                    memo[i]+=memo[i-num];
                }
            }
        }
        return memo[target];
    }
}
