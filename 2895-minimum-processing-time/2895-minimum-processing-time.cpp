class Solution {
public:
    int minProcessingTime(vector<int>& processorTime, vector<int>& tasks) {
        int m = processorTime.size();
        int n = tasks.size();
        sort(processorTime.begin(), processorTime.end());
        sort(tasks.begin(), tasks.end(), greater<int>());
        int j = 0;
        int maxi = INT_MIN;
        int ans = 0;
        for (int i = 0; i < m; i++) {
            int count = 0;
            while (count < 4 && j < n) {
                ans = max(ans, processorTime[i] + tasks[j]);
                count++;
                j++;
            }
        }
        return ans;
    }
};