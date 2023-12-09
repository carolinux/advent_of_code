#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <sstream>


#include <bits/stdc++.h>
using namespace std;


#define vc vector<char>
#define pt pair<int,int>

int main() {
	string line;
	int arr[99][99];
	int ro = 99;int co = 99;
	int mi = -1;
	
	int r = 0;

	int res = 0;
	set<pt> visibles; 
	vector<multiset<int>> rowsets;
	vector<multiset<int>> colsets;

	
	while (getline(cin, line)) {
		multiset<int> rowset; 
		for(int c=0;c<co;c++) {
			char ch = line[c];
			int num = ch - '0';
			arr[r][c] = num;
			cout<<num<<" vs "<<arr[r][c]<<endl;
			rowset.insert(num);
		}
		rowsets.push_back(rowset);
		r++;
	}

	for(int c=0;c<co;c++) {
		multiset<int> colset;
		for(int r=0;r<ro;r++) {
			colset.insert(arr[r][c]);

		}

		colsets.push_back(colset);
	}
	for(int r=0;r<ro;r++) {
		multiset<int> right = rowsets[r];
		multiset<int> left;
		for(int c=0;c<co;c++) {
			int curr = arr[r][c];
			//remove current from right
			// do lower_bound
			// add current to left
			auto it = right.find(curr);
			bool present = it != right.end();
			right.erase(it);
			pt point(r,c);
			
			// if there's nothing larger or equal, the pt is visible from that side
			if (left.lower_bound(curr) == left.end()) {
				visibles.insert(point);
			}
			if (right.lower_bound(curr) == right.end()) {
				visibles.insert(point);
			}

			left.insert(curr);

		}

	}
	for(int c=0;c<co;c++) {
		multiset<int> right = colsets[c];
		multiset<int> left;
		for(int r=0;r<ro;r++) {
			int curr = arr[r][c];
			//remove current from right
			// do lower_bound
			// add current to left
			auto it = right.find(curr);
			right.erase(it);
			pt point(r,c);
			
			// if there's nothing larger or equal, the pt is visible from that side
			if (left.lower_bound(curr) == left.end()) {
				visibles.insert(point);
			}
			if (right.lower_bound(curr) == right.end()) {
				visibles.insert(point);
			}

			left.insert(curr);

		}

	}



	



	cout<<"Res:"<<visibles.size()<<endl;



	return 0;
}

