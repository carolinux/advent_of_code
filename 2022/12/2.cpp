#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <sstream>
#include <queue>

#include <bits/stdc++.h>
using namespace std;


#define vc vector<char>
#define pt pair<int,int>
#define item pair<pair<int,int>, int>

set<pt> DS = {pt(1,0), pt(-1,0), pt(0,1), pt(0,-1)};
const int R = 41; 
const int C = 179;
int arr[R][C];

void get_neighs(pt curr, vector<pt> *v) {
	int x = curr.first;
	int y = curr.second;
	int val = arr[x][y];

	for (auto dd: DS){

		int dx = dd.first;
		int dy = dd.second;

		int candx,candy;
		candx = x + dx;
		candy = y + dy;

		if (candx>=0 && candx < R && candy >=0 && candy < C) {
			
			int new_val = arr[candx][candy];
			if (new_val<= val || new_val == val+1) {
				//cout<<" accepted new val"<<new_val<<" vs old val"<<val<<endl;
				v->push_back(pt(candx, candy));
			}

		}
	}

}

int bfs(pt start, pt end) {


	queue<item> q;
	set<pt> visited;
	q.push(item(start, 0));
	visited.insert(start);


	while (q.size()>0) {
		
		item curr = q.front();
		q.pop();
		int steps = curr.second;
		pt pos = curr.first;
		vector<pt> neighs;// get valid neighs
		//cout<<"steps "<<steps<<" at pos "<<pos.first<<","<<pos.second<<endl;
		if (pos == end) {
			return steps;

		}
		get_neighs(pos, &neighs);
	//	cout<<"steps "<<steps<<" at pos "<<pos.first<<","<<pos.second<<endl;
		for (int i=0;i<neighs.size();i++) {
			
			if (visited.find(neighs[i]) == visited.end()) {
				visited.insert(neighs[i]);
				q.push(item(neighs[i], steps+1));

			}	
		}
	}

	return -1;
}

int main() {
	string line;
	vector<pt> starts;
	pt end;
	
	int r = 0;

	set<pt> visibles; 

	// read teh matrix	
	while (getline(cin, line)) {
		int c = 0;
		for(char ch: line) {
			int num = ch - 'a';
			if (ch == 'S'){
				num = 0;
			}
			if (ch == 'E'){
				num = 25;
				end = pt(r,c);
			}
			arr[r][c] = num;
			if (num == 0)
				starts.emplace_back(r,c);
			c++;
		}
		cout<<"Cols "<<c<<" rows "<<r<<endl;
		r++;
	}


	int minres = R*C*2;
	for (auto start: starts) {
		int res = bfs(start, end);
		if (res !=-1)
			minres = min(res, minres);
	}
	cout<<"Res:"<<minres<<endl;
	return 0;
}

