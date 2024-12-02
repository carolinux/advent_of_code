#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define ull unsigned long long
int main() {

    vector<int> a;
    vector<int> b;
    // read lines in the file until eof
    int n = 1000;
    while (n--) {
        int ai, bi;
        std::cin >> ai >> bi;
        a.push_back(ai);
        b.push_back(bi);
    }

    // sort the vectors
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    ull s = 0;
    for (int i = 0; i < a.size(); i++) {
        s+= (ull) abs(a[i] - b[i]);
    }
    cout << s << endl;
    //cout <<a.size()<< endl;

    return 0;
   }
