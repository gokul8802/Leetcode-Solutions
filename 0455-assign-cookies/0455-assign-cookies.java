class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int ans = 0;
        
        Arrays.sort(g);
        Arrays.sort(s);
        
        int i = 0; // child pointer
        int j = 0; // cookie pointer
        
        while(i < g.length && j < s.length) {
            if(g[i] <= s[j]) {
                ans++;
                i++;  // move to next child
            }
            j++;  // always move cookie
        }
        
        return ans;
    }
}