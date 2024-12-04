#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;
#define ull unsigned long long

//read 140 strings
vector<string> mat;
int S = 140;

bool find_hor(string s, int i, int j) {
    int n = s.size();
    int ro = S, co = S;
    if (j + n -1 >= co) return false;
    for (int k = 0; k < n; k++) {
        //cout<<j+k<<endl;
        if (s[k] != mat[i][j + k]) return false;
    }
    return true;
}

bool find_vert(string s, int i, int j) {
    int n = s.size();
    int ro = S, co = S;
    if (i + n -1 >= ro) return false;
    for (int k = 0; k < n; k++) {
        if (s[k] != mat[i + k][j]) return false;
    }
    return true;
}

bool find_diagup(string s, int i, int j) {
    int n = s.size();
    int ro = S, co = S;
    if (i + n -1 >= ro || j + n -1 >= co) return false;
    for (int k = 0; k < n; k++) {
        if (s[k] != mat[i + k][j + k]) return false;
    }
    return true;
}

bool find_diagdown(string s, int i, int j) {
    int n = s.size();
    int ro = S, co = S;
    if (i - n + 1 < 0 || j + n - 1 >= co) return false;
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

            char ch = mat[i][j];
            int found1 = (find_hor("XMAS", i, j) + find_vert("XMAS", i, j) + find_diagup("XMAS", i, j) + find_diagdown("XMAS", i,j));
            int found2 = (find_hor("SAMX", i, j) + find_vert("SAMX", i, j) + find_diagup("SAMX", i, j) + find_diagdown("SAMX", i,j));
            if (found1 || found2) {
                ans+=found1+found2;
            }
            }
    }

    cout<<ans<<endl;

}
