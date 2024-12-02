#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;
#define ull unsigned long long

bool isgood(vector<int>&a, int skipi) {
        bool good = 1;
        int sign = 0;
        int start = 1;
        if (skipi == 0) {
            start = 2;
        }
        for(int i=start;i<a.size();i++) {
            if (i == skipi) {
                continue;
            }
            int prev = i-1;
            if (prev == skipi) {
                prev--;
            }
            int diff = a[i] - a[prev];
            if (abs(diff) > 3 || abs(diff) < 1) {
                good = 0;
                break;
            }
            if (i ==start) {
                sign = 1 ? diff > 0 : -1;
                continue;
            }
            int sign2 = 1 ? diff > 0 : -1;
            if (sign != sign2) {
                good = 0;
                break;
            }
            sign = sign2;
        }
        return good;
}

int main() {

    int ans = 0;
    int n = 1000;
    while (n--) {
        vector<int> a;
        string line;
        getline(cin, line);
        istringstream stream(line);
        int number;

        while (stream >> number) {
            a.push_back(number);
        }
        int incr = 0;
        if (isgood(a, -1)) {
            incr = 1;
        }

        for (int i=0;i<a.size();i++) {
            vector<int> b;
            for (int j=0;j<a.size();j++) {
                if (j == i) {
                    continue;
                }
                b.push_back(a[j]);
            }
            if (isgood(b, -1)) {
                incr = 1;
                break;
            }
        }
        /*
        for (int i=0;i<a.size();i++) {
            if (isgood(a, i)) {
                incr = 1;
                break;
            }

        }
        */
        ans += incr;
        /*
         for(int i=0;i<a.size();i++) {
             cout << a[i] << " ";
         }
        cout<<"good: "<<good<<" ans: "<<ans<<endl;*/
    }

    cout << ans << endl;

    return 0;
   }
