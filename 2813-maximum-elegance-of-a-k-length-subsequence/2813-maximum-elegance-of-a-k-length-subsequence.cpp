class Solution {
public:
    long long findMaximumElegance(vector<vector<int>>& items, int k) {
        int n = items.size();
        sort(items.begin(), items.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] > b[0];
        });

        long long total_profit = 0;
        long long max_elegance = 0;
        vector<int> duplicate_profits;
        vector<bool> seen(n + 1, false);
        long long distinct_categories = 0;

        for (int i = 0; i < n; i++) {
            long long profit = items[i][0];
            int category = items[i][1];

            if (i < k) {
                total_profit += profit;
                if (!seen[category]) {
                    seen[category] = true;
                    distinct_categories++;
                } else {
                    duplicate_profits.push_back(profit);
                }
            } else {
                if (!seen[category] && !duplicate_profits.empty()) {
                    seen[category] = true;
                    distinct_categories++;
                    total_profit += profit - duplicate_profits.back();
                    duplicate_profits.pop_back();
                }
            }
            max_elegance = max(max_elegance, total_profit + distinct_categories * distinct_categories);
        }

        return max_elegance;
    }
};