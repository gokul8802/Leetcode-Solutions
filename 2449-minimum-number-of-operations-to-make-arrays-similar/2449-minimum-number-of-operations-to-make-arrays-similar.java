class Solution {
    public long makeSimilar(int[] nums, int[] target) {
        long count = 0;

        List<Integer> eNum = new ArrayList<>();
        List<Integer> eTarget = new ArrayList<>();
        List<Integer> oNum = new ArrayList<>();
        List<Integer> oTarget = new ArrayList<>();

        Arrays.sort(nums);
        Arrays.sort(target);

        for(int i = 0; i < nums.length; i++) {
            if(nums[i] % 2 == 0) eNum.add(nums[i]);
            else oNum.add(nums[i]);

            if(target[i] % 2 == 0) eTarget.add(target[i]);
            else oTarget.add(target[i]);
        }

        for(int i = 0; i < eNum.size(); i++) {
            if(eNum.get(i) > eTarget.get(i)) count += eNum.get(i) - eTarget.get(i);
        }

        for(int i = 0; i < oNum.size(); i++) {
            if(oNum.get(i) > oTarget.get(i)) count += oNum.get(i) - oTarget.get(i);
        }

        return count / 2;

    }
}