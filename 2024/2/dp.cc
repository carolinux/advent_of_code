#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;
#define ull unsigned long long

bool isgood(vector<int>&a) {

    vector<vector<int> > inc = vector<vector<int> >(a.size(), vector<int>(2, 0));
    vector<vector<int> > dec = vector<vector<int> >(a.size(), vector<int>(2, 0));
    //finish at index i, [0] no skips, [1] having skipped its previous
    inc[0][0] = 1;
    dec[0][0] = 1;
    for (int i=1;i<a.size();i++) {
        int diff = a[i] - a[i-1];
        dec[i][0] = (diff<0) && abs(diff)<=3 && abs(diff) >=1 && dec[i-1][0];
        inc[i][0] = (diff>0) && abs(diff)<=3 && abs(diff) >=1 && inc[i-1][0];

        bool dec1 = (diff<0) && abs(diff)<=3 && abs(diff) >=1 && (dec[i-1][1]);
        bool inc1 = (diff>0) && abs(diff)<=3 && abs(diff) >=1 && (inc[i-1][1]);
        bool dec2 = 0;
        bool inc2 = 0;
        if (i<=1) {
            dec2 = 1;
            inc2 = 1;
        } else {
            int diff2 = a[i] - a[i-2];
            dec2 = (diff2<0) && abs(diff2)<=3 && abs(diff2) >=1 && (dec[i-2][0]);
            inc2 = (diff2>0) && abs(diff2)<=3 && abs(diff2) >=1 && (inc[i-2][0]);

        }
        dec[i][1] = dec1 || dec2;
        inc[i][1] = inc1 || inc2;

    }
    int n = int(a.size());
    return inc[n-1][1] || inc[n-1][0] || dec[n-1][0] || dec[n-1][1] || inc[n-2][0] || dec[n-2][0]; // the last two ors are necessary

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

        ans += isgood(a);
        /*
         for(int i=0;i<a.size();i++) {
             cout << a[i] << " ";
         }
        cout<<"good: "<<good<<" ans: "<<ans<<endl;*/
    }

    cout << ans << endl;

    return 0;
   }
