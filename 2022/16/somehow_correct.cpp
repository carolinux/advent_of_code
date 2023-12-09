#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <unordered_map>
#include <set>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <cassert>
#include <stdio.h>

#include <bits/stdc++.h>
using namespace std;


#define vc vector<char>
#define vs vector<string>
#define vi vector<int>
#define vsi vector<set<int>>
#define pt pair<int,int>
#define edge pair<pair<int,int>, pair<int,int>>
#define f first
#define s second

#define FOR(k,a,b) for(auto k=(a); k < (b); ++k)

set<pt> DS = {pt(1,0), pt(1,-1), pt(1,1)};

void printv(vi & v) {
	for(auto &e:v)
		cout<<e<<", ";
	cout<<endl;

}

void prints(vs & v) {
	for(auto &e:v)
		cout<<e<<", ";
	cout<<endl;
}


vector<string> split(const string& i_str, const string& i_delim)
{
    vector<string> result;
    size_t startIndex = 0;

    for (size_t found = i_str.find(i_delim); found != string::npos; found = i_str.find(i_delim, startIndex))
    {
        result.emplace_back(i_str.begin()+startIndex, i_str.begin()+found);
        startIndex = found + i_delim.size();
    }
    if (startIndex != i_str.size())
        result.emplace_back(i_str.begin()+startIndex, i_str.end());
    return result;      
}


struct Info {

	short int node;
	short int prev;
	int elapsed;
	int flow;
	int flowps;
	set<short int> used;
//	vector<string> seq;

};


short int canonize(string node) {

	int n1 = 26 * ( node[0] - 'A');
	int n2 = node[1] - 'A';
	return n1 + n2;
}	


int main() {
	string line;
	
	unordered_map<short int, vector<short int>> g; // node to neighbours	
	unordered_map<short int, int> vals; // node to flow rate
	int maxflow = 0;

	while (getline(cin, line)) {

		stringstream s(line);
		string nodestr;
		int rate,children;
		s>>nodestr>>rate>>children;
		cout<<"node "<<nodestr<<" "<<rate<<" "<<children<<endl;
		short int node = canonize(nodestr);
		string ch;
		getline(cin, ch);
		vector<short int> neighs;
		stringstream s2(ch);
		FOR(k,0,children)
		{
			string childstr;
			s2>>childstr;
			neighs.push_back(canonize(childstr));
		}
		g.insert({node, neighs});
		vals.insert({node, rate});
	}


	queue<Info> q;
	Info start;
	start.node = canonize("AA");
	start.prev = -1;
	start.elapsed = 1;
	start.flowps = 0; // flow per second
	start.flow = 0; //total flow released
	int limit = 31;
	vector<int> mflows(31, 0);

	q.push(start);

	while (q.size()>0) {

		Info curr = q.front(); // this makes a copy of the struct
		if (curr.elapsed >5 && curr.flowps < (mflows[curr.elapsed] >>1))
		cout<<"We are at steps "<<curr.elapsed-1<<" at node "<<curr.node<<" with total flow released "<<curr.flow<<" and flow per min="<<curr.flowps<<endl;

		q.pop();
		if (curr.elapsed >8 && curr.flowps < (mflows[curr.elapsed] >>2))
			continue;
		mflows[curr.elapsed] = max(mflows[curr.elapsed], curr.flowps);
		if (true) {

			// move to a neighbouring node
			short int previous = curr.prev;
			curr.flow += curr.flowps;
			maxflow = max(curr.flow, maxflow);
			if (curr.elapsed + 1 == limit) {
				continue;
			}
			for (auto child: g[curr.node]) {

				Info cand(curr);
				cand.node = child;
				if (child == previous && g[curr.node].size()>1) {
					continue;
				}
				cand.elapsed = curr.elapsed + 1;
				cand.used = set(curr.used);
				cand.prev = curr.node;
				//cand.seq = vector(curr.seq);
				//cand.seq.push_back(curr.node);
				q.push(cand);

			}

		}

		if (vals[curr.node] > 0 && curr.used.find(curr.node)== curr.used.end()) {
			// open teh current valve
			//curr.flow += curr.flowps;
			//maxflow = max(curr.flow, maxflow);
			curr.flowps+= vals[curr.node];
			curr.used = set(curr.used); // copy constructor?
			curr.used.insert(curr.node);
			curr.elapsed++;
			if (curr.elapsed == limit) {
				continue;
			}
			q.push(curr);

		}

	}
	cout<<"max flow"<<maxflow<<endl;

	return 0;
}

