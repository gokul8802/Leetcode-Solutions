class Solution {
public:
    int minimumTime(vector<int>& nums1, vector<int>& nums2, int x) {
        int s1 = accumulate(nums1.begin(), nums1.end(), 0), s2 = accumulate(nums2.begin(), nums2.end(), 0), n = nums1.size();
        vector<int> dp(n + 1, 0);
        vector<pair<int, int>> nums;

        for(int i = 0; i < n; i++)
            nums.push_back({nums2[i], nums1[i]});
        sort(nums.begin(), nums.end());

        for(int i = 0; i < n; i++)
            for(int j = i + 1; j > 0; j--)
                // clear the ith element or not
                dp[j] = max(dp[j], dp[j-1] + nums[i].second + j * nums[i].first);

        for(int t = 0; t <= n; t++)
            if(s1 + t * s2 - dp[t] <= x)
                return t;
        return -1;
    }
};