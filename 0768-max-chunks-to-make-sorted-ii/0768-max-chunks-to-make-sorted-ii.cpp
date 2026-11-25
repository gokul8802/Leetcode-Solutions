class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        vector<int> rmin(arr.size() + 1);
        rmin[rmin.size() - 1] = INT_MAX;

        for(int i = arr.size() - 1; i >= 0; i--) {
            rmin[i] = min(rmin[i + 1], arr[i]);
        }

        int lmax = INT_MIN;
        int count = 0;

        for(int i = 0; i < arr.size(); i++) {
            lmax = max(lmax, arr[i]);

            if(lmax <= rmin[i + 1]) {
                count++;
            }
        }

        return count;
    }
};