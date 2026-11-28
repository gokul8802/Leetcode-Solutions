class Solution {
public:
    
    int calculateCombinationsModM(int tota, int cont, int mod) {
        if (cont == 0)
            return 1;       
       
        vector<int> factorialArray(tota + 1);
        factorialArray[0] = 1;
        
        // Calculate factorial mod mod for each number up to tota
        for (int i = 1; i <= tota; i++)
            factorialArray[i] = (1LL * factorialArray[i - 1] * i) % mod;
        
        int result = factorialArray[tota];
        result = (1LL * result * calculateModularInverse(factorialArray[cont], mod)) % mod;
        result = (1LL * result * calculateModularInverse(factorialArray[tota - cont], mod)) % mod;
        
        return result;
    }

    int calculateModularInverse(int number, int mod) {
        int modulo0 = mod;
        int y = 0, x = 1;
        
        while (number > 1) {
            int quotient = number / mod;
            int temp = mod;
            mod = number % mod;
            number = temp;
            temp = y;
            y = x - quotient * y;
            x = temp;
        }
        
        if (x < 0)
            x += modulo0;
        
        return x;
    }
    
    int countKSubsequencesWithMaxBeauty(string inputString, int kValue) {
        int mod = 1e9 + 7;

        unordered_map<char, int> characterCountMap;
        
        for (auto character : inputString) {
            characterCountMap[character]++;
        }
        
        if (characterCountMap.size() < kValue) {
            return 0;
        }
        
        vector<int> characterCounts;
        for (auto characterCountPair : characterCountMap) {
            characterCounts.push_back(characterCountPair.second);
        }
        
        sort(characterCounts.begin(), characterCounts.end());
        reverse(characterCounts.begin(), characterCounts.end());
        
        int answer = 1;
        int tota = characterCounts.size();
        int lowestCount = characterCounts[kValue - 1];
        int totalLowestCount = 0, currentLowestCount = 0;
        
        for (int i = 0; i < tota; i++) {
            if (i < kValue) {
                answer = (1LL * answer * characterCounts[i]) % mod;
                if (characterCounts[i] == lowestCount) {
                    currentLowestCount++;
                }
            }
            
            if (characterCounts[i] == lowestCount) {
                totalLowestCount++;
            }
        }
        
        answer = (1LL * answer * calculateCombinationsModM(totalLowestCount, currentLowestCount, mod)) % mod;
        return answer;
    }
};