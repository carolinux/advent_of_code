#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>
#include <queue>
#include <map>
#include <utility>

using namespace std;
#define ull unsigned long long

//read 140 strings
vector<string> mat;
int E = 1176;
int Q = 223;



bool reachable(int a , int b, vector<set<int>> &g) {

    vector<bool> visited = vector<bool>(100, false);
    queue<int> q;
    q.push(a);
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        if (cur == b) {
            return true;
        }
        for (int next : g[cur]) {
            if (!visited[next]) {
                visited[next] = true;
                q.push(next);
            }
        }
    }
    return false;
}

typedef pair<int, int> pii;


signed main() {
    // small
    // E = 21;
    // Q = 6;
    set<pii> edges = set<pii>();
    map<int, int> indeg = map<int, int>();

    for (int i = 0; i < E; i++) {
        string s;
        cin >> s;
        // split the string on | and get the two numbers
        stringstream ss(s);
        string token;
        vector<int> tokens;
        while (getline(ss, token, '|')) {
            //cout<<token<<endl;
            tokens.push_back(stoi(token));
        }

        edges.insert({tokens[0], tokens[1]});
        //cout<<tokens[0]<<" "<<tokens[1]<<endl;
    }


    int ans = 0;

    for (int i = 0; i < Q; i++) {
        string s;
        cin >> s;
        // split the string on , and get all the numbers
        stringstream ss(s);
        string token;
        vector<int> tokens;
        while (getline(ss, token, ',')) {
            tokens.push_back(stoi(token));
        }
        if (tokens.size() == 1) {
            ans+=tokens[0];
            continue;
        }

        vector<set<int>> gg = vector<set<int>>(100);
        // iterate over edges set
        for (pii edge : edges) {
            int a = edge.first;
            int b = edge.second;
            if (find(tokens.begin(), tokens.end(), a) != tokens.end() && find(tokens.begin(), tokens.end(), b) != tokens.end()) {
                gg[a].insert(b);
            }
        }

        bool add = true;
        for (int i=1;i<tokens.size();i++) {
            int a = tokens[i-1];
            int b = tokens[i];
            bool rab = reachable(a, b, gg);
            bool rba = reachable(b, a , gg);
            //cout<<a<<" "<<b<<" "<<rab<<" "<<rba<<endl;
            bool good = (rab && !rba) || (!rab && !rba);
            //bool good = rab; // also works
            if (!good) {
                add = false;
                break;
            }
        }
        if (add) {
            ans+=tokens[tokens.size()>>1];
        }
        // print tokens
        /*for (int token : tokens) {
            cout << token << " ";
            }
        cout << endl;*/
    }



    cout<<ans<<endl;

}
