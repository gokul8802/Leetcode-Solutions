class Solution {
public:
    long long minimumMoney(vector<vector<int>>& transactions) {
        int n=transactions.size();
        long long ans=0;
        long long t1=0;

        for(int i=0; i<n; i++){
            long long diff=0LL+-transactions[i][0]+transactions[i][1];
            if(diff<0){
                ans+=abs(diff);
                t1=max(t1, (long long)transactions[i][1]);
            }
            else{
                t1=max(t1, (long long)transactions[i][0]);
            }
        }
        return ans+t1;
    }
};