class Solution {
    public int minMoves2(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);

        int mid = nums[n / 2];
        int moves = 0, i = 0;

        while (i < n / 2) {
            moves+=Math.abs(nums[i]-mid);
            moves+=Math.abs(nums[n-1-i]-mid);
            i++;
        }
        if (n%2!=0) {
            moves+=Math.abs(nums[n/2]-mid);
        }
        return moves;
    }
}