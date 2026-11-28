class Solution {
public:
    long long maxSpending(vector<vector<int>>& values) {
        const int m = values.size(), n = values[0].size(), total = m * n;
        vector<int> val(total);
        for(int i = 0; i < m; ++i){
            for(int j = 0; j < n; ++j) val[i * n + j] = values[i][j];
        }
        sort(val.begin() , val.end());
        long long res = 0;
        for(int v = 0; v < total; ++v) res += 1LL * val[v] * (v + 1);
        return res;
    }
};