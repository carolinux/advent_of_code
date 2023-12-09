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

	vector<char> crt;
	

	
	while (getline(cin, line)) {
		string op;
		stringstream ss(line);
		
		ss>>op;
		if (op == "noop") {

			cycles++;
			int cy = (cycles-1) % 40;
			if (cy == value || cy == value+1 || cy == value-1) {crt.push_back('#');}
			else {crt.push_back('.');}

		}
		else {
			int diff;
			ss>>diff;
			prev = value;
			for(int j=0;j<2;j++) {
				cycles++;
				int cy = (cycles-1) % 40;
				if (cy == value || cy == value+1 || cy == value-1) {crt.push_back('#');}
				else {crt.push_back('.');}
			}
			value += diff;

		}

	//cout<<value<<endl;



	}

	for (int i=0;i<crt.size();i++) {
		cout<<crt[i];
		if ((i+1)%40 == 0){cout<<endl;}
	}


	return 0;
}

