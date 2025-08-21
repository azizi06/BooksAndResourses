#include<iostream>
#include<algorithm>
#include <string>
#include<vector>
#include<ranges>
using namespace std;

class Solution {
    public:
        int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
            int remaining_fruits = fruits.size();
            cout << "\nremaining fruits : " << remaining_fruits << endl ;
            auto is_avaible = vector<int>(baskets.size(),1);
            ranges::for_each(is_avaible,[](auto i){cout << i << "   ";});
            cout << "\n";
            for(int i = 0;i< fruits.size();i++){ 
                int j = 0;
                while(j < baskets.size()){
                    cout << "fruits : " << fruits[i] << "   baskets  " << baskets[j] << endl;
                    if(is_avaible[j] == 1 &&  baskets[j] >= fruits[i]){
                        remaining_fruits-=1;
                        is_avaible[j] = 0;
                        break;
                    }
                    j++;
                }
            }
            return remaining_fruits;
        }
    };

    int main(void){
        auto a = vector<int>{4,2,5};
        auto  b =vector<int>{3,5,4};
        cout << "num Of Unplaced Fruit start ..\n";
        
       
        auto s = Solution().numOfUnplacedFruits(a,b);
        cout << "num Of Unplaced Fruit :  " << s ;
    
        return EXIT_SUCCESS;
    }