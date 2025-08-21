#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <ranges>
#include<algorithm>

using namespace std;

class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> phrase;

        for (auto it = words.begin(); it < words.end(); ) {
            auto start = it;
            auto end = it;
            int width = 0;

            // Build the line (greedy word packing)
            while (end != words.end() && width + end->size() + (end - start) <= maxWidth) {
                width += end->size();
                ++end;
            }

            int gaps = end - start - 1;
            string line;

            // Check if it's the last line
            if (end == words.end() || gaps == 0) {
                // Left-justified
                for (auto sit = start; sit != end; ++sit) {
                    line += *sit;
                    if (sit + 1 != end) line += ' ';
                }
                line += string(maxWidth - line.size(), ' ');
            } else {
                // Full-justified
                int total_spaces = maxWidth - width;
                int space_per_gap = total_spaces / gaps;
                int extra_spaces = total_spaces % gaps;

                for (int i = 0; i <= gaps; ++i) {
                    line += *(start + i);
                    if (i < gaps) {
                        line += string(space_per_gap + (i < extra_spaces ? 1 : 0), ' ');
                    }
                }
            }

            phrase.push_back(line);
            it = end; // advance to next line
        }

        return phrase;
    }
};

int main(int argc,char*  argv[]) {
    cout << "Program start\n";
    if(argc <= 2){
        cerr << "EROOR Require more arguments : file_name  max_width";
        return EXIT_FAILURE;
    }
    fstream f;
    int maxWidth = stoi(argv[2]);
    f.open(argv[1], ios::in  ); // trunc to overwrite

/*     vector<string> words = {
        "Science", "is", "what", "we", "understand", "well", "enough",
        "to", "explain", "to", "a", "computer.", "Art", "is",
        "everything", "else", "we", "do"
    }; */
    vector<string> words;
    string word;
    while (f >> word) {
        words.push_back(word);
    }
    f.clear(); // clear EOF flag before seeking
    f.seekg(0, ios::beg);
    f.seekp(0, ios::beg);
    f.close(); 
    
    auto print = [&f](const auto& s) {
        cout << '"' << s << '"' << endl;
    };
   
    for_each(words.begin(),words.end(),print);
    cout << "\n------------------------------------------------------" << endl;

    auto result = Solution().fullJustify(words, maxWidth);
    cout << "Solution:\n";
    for_each(result.begin(), result.end(), print);
    // write to a file ;
    f.open(argv[1], ios::out | ios::trunc  );
     auto write = [&f](const auto& s) {
        f << s << "\n";
    };
    for_each(result.begin(), result.end(), write);
    f.close();

    return EXIT_SUCCESS;
}
