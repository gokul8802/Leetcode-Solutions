class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        int n = apple.size();
        int m = capacity.size();
        int total_apples = 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            total_apples += apple[i];
        }
        sort(capacity.begin(), capacity.end(), greater<int>());
        int i = 0;
        while (total_apples > 0 && i < m) {
            total_apples -= capacity[i];
            i++;
            count++;
        }
        return count;
    }
};