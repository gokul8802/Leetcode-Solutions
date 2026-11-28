class Solution {
public:
    vector<int> relocateMarbles(vector<int>& nums, vector<int>& moveFrom, vector<int>& moveTo) {
        map<int,int>m;
        for(int i=0;i<nums.size();i++)
        {
            m[nums[i]]++;
        }
        for(int i=0;i<moveFrom.size();i++)
        {
            if(m.find(moveFrom[i])!=m.end())
            {
                m.erase(moveFrom[i]);
                m[moveTo[i]]++;
            }
        }
        vector<int>v;
        for(auto x:m)
        {
            v.push_back(x.first);
        }
        return v;
    }
};