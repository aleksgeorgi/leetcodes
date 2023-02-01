class Solution {
    public int countElements(int[] nums) {
        int count=0;
		int max=Integer.MIN_VALUE;
		int min=Integer.MAX_VALUE;
		    for(int i=0;i<nums.length;i++){
		        if(nums[i]<min)
		            min=nums[i];
		        if(nums[i]>max)
		            max=nums[i];
		    }
		    for(int k:nums){
		        if(min<k && k<max)
		            count++;
            }
            return count;
     }
}