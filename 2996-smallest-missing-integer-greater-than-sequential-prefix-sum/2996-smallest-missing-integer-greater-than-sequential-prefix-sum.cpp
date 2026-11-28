class Solution {
public:
    int missingInteger(vector<int>& nums) {
        int sum=nums[0];
        for(int i=1;i<nums.size();i++){
            if(nums[i]-1==nums[i-1]){
                sum=sum+nums[i];
            }else{
                break;
            }
        }
        unordered_set<int> visit(nums.begin(),nums.end());
        while(visit.count(sum)){
            sum++;
        }
        return sum;
    }
};