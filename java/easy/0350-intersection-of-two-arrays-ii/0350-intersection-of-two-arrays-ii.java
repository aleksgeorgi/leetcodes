class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        
        /*
        PROGRAM WALKTRHOUGH (brute force) O(n^2)
        
        2) compare the number of indeces of the arrays
        3) take put the smallest index on the outside for loop, the larger inside
        4) compare each index of the smaller array agains the larger 
        
        
        OUTPUT
            array of intersecting elements 
        */
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        ArrayList<Integer> list = new ArrayList<Integer>();
                
        int nums1Len = nums1.length;
        int nums2Len = nums2.length;
                
        //store elements in nums1 in hashmap
        for(int i=0; i<nums1Len; i++){
            //add key:value or increment by 1 existing key
             map.put(nums1[i], map.getOrDefault(nums1[i], 0)+1);
        }
        
        //traverse nums2 for common elements
        for(int i=0; i<nums2Len; i++){
            //if we still have elements, add to array and decremement frequency
            if(map.containsKey(nums2[i]) && map.get(nums2[i]) > 0){
                list.add(nums2[i]);
                map.put(nums2[i], map.get(nums2[i])-1); 
            }
        }
        
        //declare a new array to return
        int[] intersection = new int[list.size()];
        
        //add elements from ArrayList to array
        for(int i=0; i<list.size(); i++){
            intersection[i]=list.get(i); 
        }
        
    return intersection;
    }
}