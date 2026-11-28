class Solution {
public:
    int maxIncreasingCells(vector<vector<int>>& mat) {
        int n = mat.size(), m = mat[0].size();
        vector<int> row_max(n), col_max(m);
        
        map<int, vector<pair<int, int>>, greater<int>> pos;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                pos[mat[i][j]].push_back({i, j});
            }
        }
        
        int ans = 0;
        for (auto& [num, cells]: pos) {
            int k = cells.size();
            vector<int> next(k);
            for (int i = 0; i < k; ++i) {
                int r = cells[i].first, c = cells[i].second;
                next[i] = max(row_max[r], col_max[c]) + 1;
                ans = max(ans, next[i]);
            }
            for (int i = 0; i < k; ++i) {
                int r = cells[i].first, c = cells[i].second;
                row_max[r] = max(row_max[r], next[i]);
                col_max[c] = max(col_max[c], next[i]);
            }
        }
        return ans;
    }
};