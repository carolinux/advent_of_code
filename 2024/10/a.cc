#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;
#define ull unsigned long long
#define vi vector<int>

void explore(int origi, int origj, int i, int j, vector<set<int>> &dp, vector<vi> &mat, int curr) {
    if (i < 0 || i >= mat.size() || j < 0 || j >= mat.size()) {
        return;
    }
    int n = int(mat.size());
    if (mat[i][j] != curr) {
        return ;
    }
    if (mat[i][j] == 9 && curr == 9 ){
        dp[origi*n + origj].insert(i*n + j);
        //cout<<"inserted"<<endl;
    }

    //cout<<"exploring inside "<<curr<<endl;

    explore(origi, origj, i+1, j, dp, mat, curr+1);
    explore(origi, origj, i-1, j, dp, mat, curr+1);
    explore(origi, origj, i, j+1, dp, mat, curr+1);
    explore(origi, origj, i, j-1, dp, mat, curr+1);


    return;

}

int main() {

    vector<vi> mat;

    int n = 52;
    int j = n;
    // read the matrix
    while (j--) {
        string s;
        cin >> s;
        vi row;
        // split s into chars and cast to int using atoi
        for (int i = 0; i < s.size(); i++) {
            row.push_back(s[i] - '0');
        }
        mat.push_back(row);

    }
    int ans = 0;
    // create a vector of sets
    vector<set<int>> dp(n*n, set<int>());
    // iterate over matrix
    //cout<<n<<endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < mat[i].size(); j++) {

            //cout<<mat[i][j]<<" ";

            if (mat[i][j] != 0) {
                continue;
            }
            //cout<<"exploring"<<endl;
            explore(i, j, i, j, dp, mat, 0);
            auto ss = dp[i*n + j];
            ans+=int(ss.size());

        }
    }

    cout<<ans<<endl;
    return 0;
   }
