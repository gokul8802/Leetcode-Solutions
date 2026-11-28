class Solution {
public:
    // time/space: O(nk)/O(nk)
    vector<string> findHighAccessEmployees(vector<vector<string>>& access_times) {
        // record the access times for each person
        unordered_map<string, vector<int>> hash;
        for (auto& x : access_times) hash[x[0]].push_back(stoi(x[1]));
        
        // sort the access time for each person
        for (auto& [name, array] : hash) sort(array.begin(), array.end());

        // check the interval for each 3-access
        vector<string> result;
        for (auto& [name, array] : hash) {
            int k = array.size();
            for (int i = 2; i < k; i++) {
                if ((array[i] - array[i - 2]) < 100) {
                    result.push_back(name);
                    break;
                }
            } 
        }
        return result;
    }
};