class Solution {
public:
    int minimumPushes(string word) {
        unordered_map<char,int>mp;
        for(char  c : word)mp[c]++;
        vector<pair<int,char>>vp;
        for(auto i : mp){
            vp.push_back({i.second,i.first});
        }
        sort(vp.rbegin(),vp.rend());
        long long ans = 0;
        int n = vp.size();
        int c = 1;
        for(int i=0;i<n;i++){
            int freq = vp[i].first;
            if(i == c*8){
                c++;
            }
            ans += c * freq;
            
        }
        return ans;
    }
};