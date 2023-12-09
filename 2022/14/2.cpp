#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <cassert>

#include <bits/stdc++.h>
using namespace std;


#define vc vector<char>
#define vsi vector<set<int>>
#define pt pair<int,int>
#define edge pair<pair<int,int>, pair<int,int>>

set<pt> DS = {pt(1,0), pt(1,-1), pt(1,1)};

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

bool is_free(int row, int col, vsi & colsets) {
	if (col<0 || col>= colsets.size())
		return true;

	return colsets[col].find(row) == colsets[col].end();

}

pt find_down(int row, int col, vsi& colsets) {

	auto it = colsets[col].upper_bound(row);

	if (it == colsets[col].end()) {

		return pt(-1, -1);
	}

	return pt((*it) - 1, col);


}


bool place_sand(vector<set<int>>& colsets) {

	int row = 0;
	int col = 500;
	bool fell = false;

//	assert(0==2);

	while (1) {

		pt next_down_pos = find_down(row, col, colsets);
		int new_row = next_down_pos.first;
		int new_col = next_down_pos.second;
		cout<<"Curr:"<<row<<","<<col<<endl;
		cout<<"Cand:"<<new_row<<","<<new_col<<endl;

		if (new_row == -1) {
			fell = true;
			break;

		}

		if (new_row != row) {
			// remember to update state in each if case in the loops
			// or break. but usually you'll need to do at least one of the two
			row = new_row;
			col = new_col;
			continue;
		}

		assert(new_row == row);

		// if we reach here, it means new_row == row

		if (is_free(row + 1, col - 1, colsets)) {
			row = row + 1;
			col = col -1;
		}
		else if (is_free(row + 1, col + 1, colsets)) {
			row = row + 1;
			col = col + 1;
		}

		else {

			colsets[new_col].insert(new_row);
			break;
		}


	}

	return fell; // into the abyss



}


int main() {
	string line;
	


	vector<set<int>> colsets(1000);	
	int maxr = 0;



	// read teh lines
	// 551,136 -> 555,136 where it's col2,row2 -> col2,row2	
	while (getline(cin, line)) {
		vector<string> parts = split(line, " -> ");

		string prev = parts[0];
		cout<<"Prev:"<<prev<<endl;

		for(int i =1;i<parts.size();i++) {


			vector<string> start_coords = split(prev, ",");
			vector<string> end_coords = split(parts[i], ",");

			int r1,c1,r2,c2;
			c1 = stoi(start_coords[0]);
			r1 = stoi(start_coords[1]);
			c2 = stoi(end_coords[0]);
			r2 = stoi(end_coords[1]);

			cout<<c1<<","<<r1<<"   "<<c2<<","<<r2<<endl;
			prev = parts[i];
			maxr = max(r1, maxr);
			maxr = max(r2, maxr);

			if (c1==c2) {
				int min_ = min(r1,r2);
				int max_ = max(r1,r2);
				for (int rr=min_;rr<=max_;rr++) 
					colsets[c1].insert(rr);
				continue;

			}
			if (r1==r2) {
				int min_ = min(c1,c2);
				int max_ = max(c1,c2);
				for (int cc=min_;cc<=max_;cc++) 
					colsets[cc].insert(r1);

				continue;
			}
			cout<<":(sad"<<endl;
			throw 400;


		}



	}
	for(set<int>& colset: colsets)
		colset.insert(168);


	int sands = 0;

	while(1) {

		bool fell = place_sand(colsets);
		if (fell)
			break;
		sands++;
		if (!is_free(0, 500, colsets))
			break;

	}



	cout<<"Res:"<<sands<<endl;
	return 0;
}

