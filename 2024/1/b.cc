#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;
#define ull unsigned long long
int main() {

    vector<int> a;
    unordered_map<int, int> b_map;
    // read lines in the file until eof
    int n = 1000;
    while (n--) {
        int ai, bi;
        std::cin >> ai >> bi;
        a.push_back(ai);

        if (b_map.find(ai) == b_map.end()) {
            b_map[ai] = 0;
        }
        if (b_map.find(bi) == b_map.end()) {
            b_map[bi] = 0;
        }
        b_map[bi]++;
    }


    ull s = 0;
    for (int i = 0; i < a.size(); i++) {
        s += (ull) (a[i] * b_map[a[i]]);
    }
    cout << s << endl;

    return 0;
   }
