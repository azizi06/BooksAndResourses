#include<iostream>
#include<algorithm>
#include <string>
using namespace std;
class Solution {
    public:
        string addBinary(string a, string b) {
            
            string result = "";
            int carry = 0;
            int i = a.size() - 1, j = b.size() - 1;
    
            while (i >= 0 || j >= 0 || carry) {
                int sum = carry;
    
                if (i >= 0) sum += a[i] - '0';
                if (j >= 0) sum += b[j] - '0';
    
                result += (sum % 2) + '0';  // Append binary digit convert from int t0 ascii
                cout << "\n  " <<result ;
                carry = sum / 2;            // Update carry
                i--;
                j--;
            }
    
            reverse(result.begin(), result.end());
            return result;
        }
    };
int main(void){
    string a,b;
    cout << "binary addition start ..\n";
    cout << "Enter two numbers :\t";
    cin >> a >>b;
    auto s = Solution().addBinary(a,b);
    cout << "\n" << a << " + " << b <<"  =  " << s ;

    return EXIT_SUCCESS;
}