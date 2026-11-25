class Solution {
    int n;
    List<List<Integer>> result = new ArrayList<>();

    void solve(Map<Integer, Integer> freq, List<Integer> permutation) {
        if (permutation.size() == n) {
            result.add(new ArrayList<>(permutation));
            return;
        }

        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            int num = entry.getKey();
            int count = entry.getValue();

            if (count != 0) {
                permutation.add(num);
                freq.put(num, count - 1);

                solve(freq, permutation);

                permutation.remove(permutation.size() - 1);
                freq.put(num, count);
            }
        }
    }

    public List<List<Integer>> permuteUnique(int[] nums) {
        n = nums.length;

        List<Integer> permutation = new ArrayList<>();
        Map<Integer, Integer> freq = new HashMap<>();

        for (int num : nums)
            freq.put(num, freq.getOrDefault(num, 0) + 1);

        solve(freq, permutation);

        return result;
    }
}