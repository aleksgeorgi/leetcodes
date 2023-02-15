class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // pointers for array traversal 
        int i=m-1; // last non-zero element in nums1
        int j=n-1; // last element in nums2
        int k=nums1.length-1; // last index in nums1

        // traversing nums2 
        while(j>=0){
            // If value at i of nums1 > value at j of nums2 then it will be stored 
            // in the first free spot at the end of nums1
            if(i>=0 && nums1[i]>nums2[j]){
                nums1[k]=nums1[i];
                k--; // decrement index in nums1
                i--; // decremenet pointer
            }else{
                nums1[k] = nums2[j];
                k--; // decrement index in nums1
                j--; // decremenet pointer
            }
        }
    }
}