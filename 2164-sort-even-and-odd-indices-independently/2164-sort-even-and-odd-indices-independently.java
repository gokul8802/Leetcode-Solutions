class Solution {
    public int[] sortEvenOdd(int[] nums) {
        PriorityQueue<Integer> a=new PriorityQueue<>();
      PriorityQueue<Integer> b=new PriorityQueue<>(Collections.reverseOrder());
        int i=0;
        while(i<nums.length)
        {
            a.add(nums[i]);
            i++;
            if(i<nums.length)
             {   b.add(nums[i]);
             }
             i++;
        }
        for( i=0;i<nums.length;i++)
        {
            if(i%2==0)
            {
                nums[i]=a.poll();
            }
            else{
                nums[i]=b.poll();
            }
        }
        return nums;
    }
}