class Solution {
public:
	vector<long long> minOperations(vector<int>& a, vector<int>& queries) {
		sort(a.begin(), a.end());
		vector dp(1, 0ll);
		for(auto &x: a) dp.push_back(dp.back() + x);

		vector <pair <long long, int>> q;
		for(int i = 0; i < queries.size(); i++) q.push_back({queries[i], i});
		sort(q.begin(), q.end());

		vector ans(q.size(), 0ll);
		long long i = 0, n = a.size(), ln = 0, rn = n, ls = 0, rs = dp[n];
		for(auto &[x, idx]: q) {
			for( ; i < n && a[i] <= x; i++) {
				ln = i + 1, rn = n - (i + 1);
				ls = dp[i + 1], rs = dp[n] - dp[i + 1];
			}
			ans[idx] = (x * ln - ls) + (rs - x * rn);
		}
		return ans;
	}
};