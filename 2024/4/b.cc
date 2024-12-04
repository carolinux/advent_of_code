#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;
#define ull unsigned long long

//read 140 strings
vector<string> mat;
int S = 140;

bool find_diagdown(string s, int i, int j) {
    int n = s.size();
    int ro = S, co = S;
    if (i + n -1 >= ro || j + n -1 >= co) return false;
    for (int k = 0; k < n; k++) {
        if (s[k] != mat[i + k][j + k]) return false;
    }
    return true;
}

bool find_diagup(string s, int i, int j) {
    int n = s.size();
    int ro = S, co = S;
    if (i - n + 1 < 0 || j + n - 1 >= co || i >=ro) return false;
    for (int k = 0; k < n; k++) {
        if (s[k] != mat[i - k][j + k]) return false;
    }
    return true;
}



signed main() {

    for (int i = 0; i < S; i++) {
        string s;
        cin >> s;
        mat.push_back(s);
    }
    //cout<<mat[30][139]<<endl;
    //return 0;

    int ans = 0;
    for (int i = 0; i < S; i++) {
        for (int j = 0; j < S; j++) {

            //cout<<"looking at char "<<mat[i][j]<<endl;

            bool f1 = find_diagdown("SAM", i, j) || find_diagdown("MAS", i, j);
            bool f2 = find_diagup("SAM", i+2, j) || find_diagup("MAS", i+2, j);
            if (f1 && f2) {
                ans++;
            }
            cout<<"for "<<i<<" "<<j<<" f1 "<<f1<<" "<<"f2 "<<f2<<endl;
            }

    }

    cout<<ans<<endl;

}
