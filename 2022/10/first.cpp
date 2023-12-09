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


int main() {
	string line;

	int sum = 0;
	int cycles = 0;
	int value = 1;
	int prev = 1;

	vector<int> ticks;
	int ti = 0; // idx of next tick
	
	ticks.push_back(19);

	for (int i=60;i<=220;i+=40) {
		ticks.push_back(i-1);
	}
	
	while (getline(cin, line)) {
		string op;
		stringstream ss(line);
		cout<<"Cycle "<<cycles<<" value:"<<value<<endl;
		
		ss>>op;
		if (op == "noop") {

			cycles++;
		}
		else {
			int diff;
			ss>>diff;
			prev = value;
			cout<<"diff :"<<diff<<endl;
			value += diff;
			cycles+=2;

		}

		// check if we exceeded a tick
		int incr = 0;
		int next_tick = ticks[ti];

		if (cycles == next_tick) { incr = (next_tick+1) * value; ti++; cout<<"Used value "<<value<<endl;}
		if (cycles > next_tick) { incr = (next_tick+1) * prev; ti++; cout<<"Used value "<<prev<<" while curr="<<value<<endl;}
		if (cycles < next_tick) { incr = 0;}

		if (incr!=0)
		{cout<<"incr by "<<incr<<" at cycle "<<cycles<<endl;}


		sum+=incr;


		if (ti>= ticks.size()) {break;}


	}

	cout<<"Res:"<<sum<<endl;

	return 0;
}

