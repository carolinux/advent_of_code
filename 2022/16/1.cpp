#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <map>
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
#define triplet pair<pair<int, int>, int>
#define t1 first.first
#define t2 first.second
#define t3 second
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

triplet mk_triplet(int a, int b, int c) {
	return pair(pair(a,b), c); 

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

};

// CPP program to demonstrate implementation of
// unordered_map for a pair.
#include <bits/stdc++.h>
using namespace std;

// A hash function used to hash a pair of any kind
struct hash_triplet {
	template <class T1, class T2, class T3>
	size_t operator()(const pair<pair<T1, T2>, T3> & p) const
	{
		auto hash1 = hash<T1>{}(p.first.first);
		auto hash2 = hash<T2>{}(p.first.second);
		auto hash3 = hash<T3>{}(p.second);
		

		if (hash1 != hash2 || hash2 != hash3) {
			return hash1 ^ hash2 ^ hash3;			
		}
		
		// If hash1 == hash2, their XOR is zero.
		return hash1;
	}
};


short int canonize(string node) {

	int n1 = 26 * ( node[0] - 'A');
	int n2 = node[1] - 'A';
	return n1 + n2;
}	

string dec(short int n) {

	return "";
}

void printst(Info n) {

	cout<<"total flow:"<<n.flow<<" fps:"<<n.flowps<<"used:"<<n.used.size()<<" curr"<<n.node<<"steps:"<<n.elapsed<<" prev:"<<n.prev<<endl;
	for (auto j: n.used)
		cout<<j<<endl;
	cout<<"-------------"<<endl;



}

// teh key hash function is part of the type :o 
void try_insert(triplet key, Info& cand, unordered_map<triplet, Info, hash_triplet> &agg) {
	if (!agg.contains(key)){

			agg.insert({key, cand});
		}

	else {

		auto& rival = agg.find(key)->second;
		if (cand.flow> rival.flow || (cand.flow==rival.flow && cand.used.size()>rival.used.size())){
			//cout<<"replaced previous flow/flowps "<<rival.flow<<","<<rival.flowps<<" with currflow/flowps"<<cand.flow<<","<<cand.flowps<<endl;
			agg[key] = cand;
		/*	if(rival.flow == cand.flow) {
				cout<<"SAME FLOW!"<<endl;
				assert(cand.used.size() != rival.used.size()); // this is by reference here so now its comparing itself to itself <o:)
				printst(cand);
				printst(rival);

			}*/

		}
	}


}


int main() {
	string line;
	
	unordered_map<short int, vector<short int>> g; // node to neighbours	
	unordered_map<short int, int> vals; // node to flow rate
	int maxflow = 0;
	set<short int> nodes;

	while (getline(cin, line)) {

		stringstream s(line);
		string nodestr;
		int rate,children;
		s>>nodestr>>rate>>children;
		short int node = canonize(nodestr);

		nodes.insert(node);
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


	unordered_map<triplet, Info, hash_triplet> agg;
	Info start;
	start.node = canonize("AA");
	start.prev = -1;
	start.elapsed = 1;
	start.flowps = 0; // flow per second
	start.flow = 0; //total flow released
	int limit = 31;
	

	agg.insert({mk_triplet(start.node, 1, start.flowps), start});


	int steps = 1;
	while (steps < limit) {

		cout<<"We are at step "<<steps<<endl;
		unordered_map<triplet, Info, hash_triplet> agg2;
		for (auto it = agg.begin(); it!=agg.end();it++) {

			auto &map_elem = *it;

			// pointer flow_ps to the info node
			Info curr = map_elem.second; // copy

			short int previous = curr.prev;
			curr.flow += curr.flowps;
			maxflow = max(curr.flow, maxflow);
			if (curr.elapsed + 1 == limit) {
				continue;
			}
			// try to move to a new node from here
			for (auto child: g[curr.node]) {

				Info cand(curr);
				cand.node = child;
				/*if (child == previous && g[curr.node].size()>1) {
					continue;
				}*/
				cand.elapsed = curr.elapsed + 1;
				cand.used = set(curr.used);
				cand.prev = curr.node;
				triplet key = mk_triplet(child, steps+1, cand.flowps);
				try_insert(key, cand, agg2);

			}

			// try to open teh thing
			if (vals[curr.node] > 0 && curr.used.find(curr.node)== curr.used.end()) {
				// open teh current valve
				//curr.flow += curr.flowps;
				//maxflow = max(curr.flow, maxflow);
				Info cand(curr);
				cand.flowps+= vals[curr.node];
				cand.used = set(curr.used); // copy constructor?
				cand.used.insert(curr.node);
				cand.elapsed++;
				if (cand.elapsed == limit) {
					continue;
				}
				triplet key = mk_triplet(cand.node, steps+1, cand.flowps);
				try_insert(key, cand, agg2);
			}

		}
		steps++;
		agg = agg2;
	}
	cout<<"max flow"<<maxflow<<endl;

	return 0;
}

