#include <boost/functional/hash.hpp>
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
#include <stdio.h>
#include <tuple>

#include <bits/stdc++.h>
using namespace std;


#define vc vector<char>
#define vsi vector<set<int>>
#define pt pair<int,int>
#define edge pair<pair<int,int>, pair<int,int>>
#define fi first
#define se second
#define t4 tuple<short int, short int, short int, short int>
set<pt> DIRS = {pt(1,0), pt(-1, 0), pt(0,1), pt(0, -1)};




/*
auto as_tuple(t8 const& v) -> decltype(auto)
{
	return std::tie(v.orebots, v.claybots, v.obsbots, v.geobots, v.ore, v.clay, v.obs, v.geo);
}

*/

// hash_value implemented in terms of tuple, for consistency and simplicity
 /*
std::size_t hash_value(t8 const& v)
{
	using boost::hash_value;
	return hash_value(as_tuple(v));
}*/


namespace std {
	template<> struct hash<::t4> : boost::hash<::t4> {};
}


void prr(const t4& t){


	cout<<get<0>(t)<<","<<get<1>(t)<<","<<get<2>(t)<<","<<get<3>(t)<<endl;

}


pt find_new(pt curr, pt d, int minr, int maxr, int minc, int maxc) {

	pt cand = pt(curr.fi + d.fi, curr.se + d.se);

	if (cand.fi > maxr)
		cand.fi = minr;
	if (cand.fi < minr)
		cand.fi = maxr;
	if (cand.se > maxc)
		cand.se = minc;
	if (cand.se < minc)
		cand.se = maxc;
	return cand;

}

pt add(pt& pt1, pt& d) {
	return pt(pt1.fi+d.fi, pt1.se+d.se);}

int main() {
	string line;
	int rows = 0;
	int cols;
	int blizz = 0;
	pt start(-1,-1);
	pt end(-1,-1);
	vector<pt> blipos; // positions of the blizzards (map for blizzard idx to its position)
	vector<pt> dirs; // directions of the blizzards
	set<pt> occ;
	set<pt> walls;

	// at every tick we can go up, down, left, right or wait
	// we will comput the new blizzard positions before making a decision where to go
	// if curr point then is covered by blizzard, we can't wait
	// if the other 4 are covered by blizzard, we also can't go there

	while (getline(cin, line)) {
		cols = line.length();
		for(int i=0;i<line.length();i++){
			char ch = line[i];
			pt curr = pt(rows, i);
			if (ch == '.'){
				end = curr;
				if (start == pt(-1,-1))
					start = curr;
				continue;
			}
			if (ch == '#') {
				walls.insert(curr);
				continue;
			}
			blipos.push_back(curr);
			if (ch=='>')
				dirs.push_back(pt(0, 1));
			if (ch=='<')
				dirs.push_back(pt(0, -1));
			// reversed here so that I can keep (0,0) as the top right instead...
			if (ch=='^')
				dirs.push_back(pt(-1, 0));
			if (ch=='v')
				dirs.push_back(pt(1, 0));
			blizz++;
		}
		rows++;

	}
	cout<<"Rows "<<rows<<" and cols "<<cols<<endl;
	cout<<"Start: "<<start.fi<<","<<start.se<<endl;
	cout<<"End: "<<end.fi<<","<<end.se<<endl;
	int maxrow = rows - 2;
	int minrow = 1;
	int maxcol = cols - 2;
	int mincol = 1;

	int steps = 0;
	vector<pt> options;
	options.push_back(start);
	pt goal = end;
	while (true) {
		vector<pt> options2;
		occ.clear();
		bool do_break = false;
	//	cout<<"At step "<<steps<<" with options: "<<options.size()<<endl;

		for(int bli=0;bli<blizz;bli++) {

			pt& curr = blipos[bli];
			pt new_pos = find_new(curr, dirs[bli], minrow, maxrow, mincol, maxcol);
			blipos[bli] = new_pos;
			occ.insert(new_pos);

		}
		sort(options.begin(), options.end());
		options.erase(unique(options.begin(), options.end()), options.end());
		for(pt &curr: options) {

			if (curr == goal) {
				cout<<"Reached end in "<<steps<<" steps."<<endl;
				do_break = true;
				break;
			}
			// we assume that we are not standing in an occupied pos
			// this will update occupied pos
			if (!occ.contains(curr)) {
				// add the current position also to next time tick (ie we wait)
				options2.push_back(curr);

			}

			for (pt d: DIRS) {
				pt cand = add(curr, d);
				if (cand.fi>=0 && !occ.contains(cand) && !walls.contains(cand))
					options2.push_back(cand);


			}


			
		}
		if (do_break)
			break;
		options = options2;

		steps++;

	}
	options.clear();
	options.push_back(end);
	goal = start;
	steps = 1;
	
	while (true) {
		vector<pt> options2;
		occ.clear();
		bool do_break = false;
	//	cout<<"At step "<<steps<<" with options: "<<options.size()<<endl;

		for(int bli=0;bli<blizz;bli++) {

			pt& curr = blipos[bli];
			pt new_pos = find_new(curr, dirs[bli], minrow, maxrow, mincol, maxcol);
			blipos[bli] = new_pos;
			occ.insert(new_pos);

		}
		sort(options.begin(), options.end());
		options.erase(unique(options.begin(), options.end()), options.end());
		for(pt &curr: options) {

			if (curr == goal) {
				cout<<"Reached goal in "<<steps<<" steps."<<endl;
				do_break = true;
				break;
			}
			// we assume that we are not standing in an occupied pos
			// this will update occupied pos
			if (!occ.contains(curr)) {
				// add the current position also to next time tick (ie we wait)
				options2.push_back(curr);

			}

			for (pt d: DIRS) {
				pt cand = add(curr, d);
				if (cand.fi>=0 && !occ.contains(cand) && !walls.contains(cand))
					options2.push_back(cand);


			}


			
		}
		if (do_break)
			break;
		options = options2;

		steps++;

	}


	options.clear();
	options.push_back(start);
	goal = end;
	steps = 1;
	
	while (true) {
		vector<pt> options2;
		occ.clear();
	//	cout<<"At step "<<steps<<" with options: "<<options.size()<<endl;

		for(int bli=0;bli<blizz;bli++) {

			pt& curr = blipos[bli];
			pt new_pos = find_new(curr, dirs[bli], minrow, maxrow, mincol, maxcol);
			blipos[bli] = new_pos;
			occ.insert(new_pos);

		}
		sort(options.begin(), options.end());
		options.erase(unique(options.begin(), options.end()), options.end());
		for(pt &curr: options) {

			if (curr == goal) {
				cout<<"Reached goal in "<<steps<<" steps."<<endl;
				return 0;
			}
			// we assume that we are not standing in an occupied pos
			// this will update occupied pos
			if (!occ.contains(curr)) {
				// add the current position also to next time tick (ie we wait)
				options2.push_back(curr);

			}

			for (pt d: DIRS) {
				pt cand = add(curr, d);
				if (cand.fi>=0 && !occ.contains(cand) && !walls.contains(cand))
					options2.push_back(cand);


			}


			
		}
		options = options2;

		steps++;

	}




	return 0;
}

