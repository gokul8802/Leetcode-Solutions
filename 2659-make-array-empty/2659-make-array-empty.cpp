class Solution {
public:
    long long countOperationsToEmptyArray(vector<int>& nums) {
        int n = nums.size();
        vector<pair<int, int>> a(n, {0, 0});
        for(int i = 0; i < n; i++) {
            a[i].first = nums[i]; // value
            a[i].second = i; // index
        }

        sort(a.begin(), a.end());

        long long res = n; // first round surely take n step
        for(int i = 1; i < n; i++) 
            if(a[i].second < a[i-1].second){
                res += n - i; // new round and will take n - i step; i is number of elements was deleted
            }
        return res;    
    }
};