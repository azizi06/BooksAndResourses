#include<iostream>
// leetcode unique paths :
#include<math.h>

class Solution {
    public:
        int uniquePaths(int m, int n) {
            return  combination(m-1,m+n-2); 
        }
        int _countUniquePaths(int i,int j,int m,int n){
            if(i == (m-1) && j ==(n-1)){
                return 1;
            }
            else if (i >= m || j >= n){
                return 0;
            }
            else {
                int _left = _countUniquePaths(i+1,j,m,n);
                int _down = _countUniquePaths(i,j+1,m,n);
                return _left + _down ;
            }
        }
        int  combination(int a, int b) {
            // Compute C(b, a) iteratively
            if (a > b - a) a = b - a;  // Use symmetry: C(b, a) == C(b, b - a)
            unsigned long long res = 1;
            for (int i = 1; i <= a; ++i) {
                res = res * (b - a + i) / i;
            }
            return static_cast<int>( res);
        }
        
    

    };
int main(){
    Solution s;
    
    
    std::cout << "The Number of unique Paths is " << s.uniquePaths(13,19);
    
    return EXIT_SUCCESS;
}