class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        cout.tie(nullptr);

        vector<pair<int, int>> jobs;
        for (int i = 0; i < difficulty.size(); ++i) {
            jobs.emplace_back(difficulty[i], profit[i]);
        }
        sort(jobs.begin(), jobs.end());
        sort(worker.begin(), worker.end());

        int maxProfit = 0, i = 0, bestProfit = 0;
        for (int w : worker) {
            while (i < jobs.size() && jobs[i].first <= w) {
                bestProfit = max(bestProfit, jobs[i].second);
                ++i;
            }
            maxProfit += bestProfit;
        }

        return maxProfit;
    }
};
// if you upvote this you will hear a good news in 10mins