class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n=nums.length;
        Map<Integer,Integer> map=new HashMap<>();
        int[] r=new int[2];
        for(int i=0;i<n;i++){
            if(map.containsKey(target-nums[i])){
                r[1]=i;
                r[0]=map.get(target-nums[i]);
                return r;
            }
            map.put(nums[i],i);
        }
        return r;
    }
}