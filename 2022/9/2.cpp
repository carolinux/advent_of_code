#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <sstream>
#include <cstdlib>


#include <bits/stdc++.h>
using namespace std;


#define vc vector<char>
#define pt pair<int,int>
#define f first
#define s second



pt  get_dx(string dir, int steps, map<string, pt> &dirs) {
	return dirs.find(dir)->second;
}

int sign(int val) {
	if (val>=0) {return 1;}
	return -1;

}

pt adjust(pt& head, pt& tail) {

	int dx = head.f - tail.f;
	int dy = head.s - tail.s;

	if ( abs(dx)<=1 and abs(dy)<=1) {return pt(tail.f, tail.s);}

	if (dx == 0) {
		dy =  sign(dy);
		return pt(tail.f, tail.s + dy);
	}
	if (dy == 0) {
		dx =  sign(dx);
		return pt(tail.f + dx, tail.s);
	}
	// dy <> 0 and dx <> 0, need to move it closer diagonally
	
	if (head.f > tail.f) { dx = 1;}
	else { dx = -1;}
	if (head.s > tail.s) { dy = 1;}
	else { dy = -1;}

	return pt(tail.f + dx, tail.s + dy);



}

int main() {
	string line;
	map<string, pt> DIRS;
	DIRS["U"] = pt(0, 1);
	DIRS["D"] = pt(0, -1);
	DIRS["R"] = pt(1, 0);
	DIRS["L"] = pt(-1, 0);


	set<pt> seen;
	vector<pt> ts;
	pt h(0,0);
	for (int i=0;i<9;i++) {
		
		pt pt1(0, 0);
		ts.push_back(pt1);

	}

	seen.insert(ts[8]);
	
	while (getline(cin, line)) {
		string dir;
		stringstream ss(line);
		int steps;
		ss>>dir>>steps;
		cout<<line<<endl;
		cout<<"dir "<<dir<<"  and steps "<<steps<<endl;
		pt dx = get_dx(dir, steps, DIRS);

		for (int i=0;i<steps;i++) {
			h = pt(h.first + dx.first, h.second + dx.second);

			for (int j=0;j<9;j++) {
				pt prev, newt;
				
				if (j==0) {prev = h;}
				else {prev = ts[j-1];}

				newt = adjust(prev, ts[j]);
				if(j==8) {seen.insert(newt);}
				ts[j] = newt;

			}
		}

	}

	cout<<"Res:"<<seen.size()<<endl;

	return 0;
}

