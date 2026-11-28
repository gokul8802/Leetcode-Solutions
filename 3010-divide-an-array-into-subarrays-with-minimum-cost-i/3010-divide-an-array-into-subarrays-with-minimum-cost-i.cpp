class Solution {
public:
    int minimumCost(vector<int>& nums) {
        int a=51,b=51; //see the constraints
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i]<a || nums[i]<b)
            {
                if(a<b) b=a;
                a=nums[i];
            }
        }
        return nums[0]+a+b;
    }
};