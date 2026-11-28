class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        int n = nums.size();

        // Pre-calculate sum
        long sum = 0;
        for(int num : nums) {
            sum += num;
        }

        for(int i = n - 1; i > 1; --i) {
            long ans = findSolution(nums, i, sum);
            sum -= nums[i];  // Reduce maximum element
            if(ans != -1) return ans;
        }
        return -1;
    }

    long findSolution(vector<int>& nums, int end, long sum) {
        int maxIndex = 0;
        for(int i = 0; i <= end; ++i) {
            if(nums[maxIndex] < nums[i]) maxIndex = i;
        }

        // Move maximum to end
        swap(nums[maxIndex], nums[end]);

        if(sum > 2 * nums[end]) return sum;
        return -1;
    }
};