class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
        }
        int m=0;
        int n=0;
        for(int i:map.keySet()){
            if(n<map.get(i)){
                m=i;
                n=map.get(i);
            }
        }
        return m;
    }
}