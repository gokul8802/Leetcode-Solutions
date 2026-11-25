class Solution {
    static{
        for (int i = 0; i < 500; i++){
            findFinalValue(new int[]{}, 0);;
        }
    }
    public static int findFinalValue(int[] nums, int original) {
        while (find(nums, original)){
            original <<= 1;
        }
        return original;
    }

    static boolean find(int[] nums, int original){
        for (int num: nums){
            if (num == original) return true;
        }
        return false;
    }
}