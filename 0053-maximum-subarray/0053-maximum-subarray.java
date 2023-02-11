class Solution {
    public int maxSubArray(int[] nums) {
        int arrLen = nums.length;
        
        // second array for dynamic programming preprocessing (O(n) space)
        int[] OPT = new int[arrLen];

        OPT[0]=nums[0]; 
        
        // run the preprocessing loop, (O(n) time)
        for (int i=1; i<arrLen; i++){
            OPT[i]= Math.max(OPT[i-1] + nums[i], nums[i]);
        }

        // return the max in OPT, (O(n) time)
        int max = OPT[0]; 
        for (int i=1; i<arrLen; i++){
            if(OPT[i]>max){
                max=OPT[i];
            }
        }
        
        return max;
    }//end maxSubArray
}

/*
Dynamic Programming algo runs in O(n)+O(n)=O(n) time & space 
*/