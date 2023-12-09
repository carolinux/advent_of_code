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

void try_insert(pt candpt, Info& cand, map<pt, map<int, Info>> &agg) {
	if (!agg.contains(candpt)){

			map<int, Info> map2;
			map2.insert({cand.flowps, cand});
			agg.insert({candpt, map2});
		}

	else {

		map<int, Info> &m2 = agg.find(candpt)->second;
		if (m2.contains(cand.flowps)) {
			auto &rival = m2.find(cand.flowps)->second;
			if (cand.flow> rival.flow || (cand.flow==rival.flow && cand.used.size()>rival.used.size())){
				cout<<"replaced previous flow/flowps "<<rival.flow<<","<<rival.flowps<<" with currflow/flowps"<<cand.flow<<","<<cand.flowps<<endl;
				m2[cand.flowps] = cand;
				if(rival.flow == cand.flow) {
					cout<<"SAME FLOW!"<<endl;
					//assert(cand.used.size() != rival.used.size()); // this is by reference here so now its comparing itself to itself <o:)
					printst(cand);
					printst(rival);

				}

			}
		}
		else{
			m2.insert({cand.flowps, cand});
		}


	}	
}


int main() {
	string line;
	
	map<short int, vector<short int>> g; // node to neighbours	
	map<short int, int> vals; // node to flow rate
	int maxflow = 0;
	set<short int> nodes;

	while (getline(cin, line)) {

		stringstream s(line);
		string nodestr;
		int rate,children;
		s>>nodestr>>rate>>children;
		cout<<"node "<<nodestr<<" "<<rate<<" "<<children<<endl;
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


	map<pt, map<int, Info>> agg;
	queue<Info> q;
	Info start;
	start.node = canonize("AA");
	start.prev = -1;
	start.elapsed = 1;
	start.flowps = 0; // flow per second
	start.flow = 0; //total flow released
	int limit = 31;
	

	map<int, Info> map1;
	map1.insert({0, start});
	agg.insert({pt(start.node, 1), map1});


	int steps = 1;
	while (steps < limit) {

		cout<<"We are at step "<<steps<<endl;
		for (short int node: nodes) {
			pt currpt (node, steps);
			cout<<"Exammining node "<<node<<endl;
			bool inmap = agg.contains(currpt);
			if (!inmap)
				continue;
			cout<<"Node is reachable at step "<<steps<<endl;

			map<int, Info> &m = agg.find(currpt)->second;

			for(auto it = m.begin(); it != m.end();it++) {

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
					pt candpt (child, steps+1);
					try_insert(candpt, cand, agg);

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
					pt candpt (cand.node, steps+1);
					try_insert(candpt, cand, agg);

				}




			}

		}
		steps++;
	}

				/*
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

		}*/

	cout<<"max flow"<<maxflow<<endl;

	return 0;
}

