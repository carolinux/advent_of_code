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
#define fi first
#define se second

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


bool legal(set<pt> board, pt pt1) {

	// if out of bounds wrt the columns
	if (pt1.fi < 0)
		return false;
	if (pt1.se<0 || pt1.se >=7)
		return false;
	return !board.contains(pt1);

}


struct Rock {

	pt bottomleft; // 0, 0
	int bboxwidth;
	int bboxheight;
	vector<pt> pos;
	
	Rock(vector<pt> pos):bottomleft(0,0), pos(pos) {
	
		bboxwidth  = 0;
		bboxheight = 0;
		for(pt &pt1: pos) {
			bboxheight = max(pt1.fi +1, bboxheight);
			bboxwidth = max(pt1.se +1, bboxwidth);

		}
	
		cout<<"Created rock with height "<<bboxheight<<" and width"<<bboxwidth<<endl;
	}

	void place_on_top(set<pt> & board, int prev_max_height) {

		pt delta(prev_max_height + 3, 2);
		move_bottomleft(board, delta, false);

	}

	int max_height() {
		return bottomleft.fi;
	}
	void finalize_pos(set<pt> & board) {
		for (pt &pt1: pos)
			board.insert(make_pair(pt1.fi + bottomleft.fi, pt1.se + bottomleft.se));
	}
	
	bool move_bottomleft(set<pt> & board, pt delta, bool place) {
		
		pt cand_delta(bottomleft.fi+delta.fi, bottomleft.se+delta.se);
		bool can_move = adjust_to_board(board, cand_delta);

		if (!can_move)
		{	// if moving downwards and could not move further, just place the thing in the board
			if (place)
				finalize_pos(board);

			return false;
		}

			bottomleft.fi+=delta.fi;
			bottomleft.se+=delta.se;
			return true;
		}

		bool adjust_to_board(set<pt> & board, pt delta) {

			for (pt &pt1: pos) {
				if (!legal(board, make_pair(pt1.fi+delta.fi, pt1.se+delta.se)))
						return false;
			}
			return true;
		}


	};

	int main() {
		string line;
		getline(cin, line);
		vector<Rock> shapes;

		vector<pt> dashv{pt(0,0), pt(0,1), pt(0,2), pt(0,3)};
		Rock dash(dashv); 
		vector<pt> crossv{pt(0,1), pt(1,0), pt(1,1), pt(1,2), pt(2,1)};
		Rock cross(crossv); 
		vector<pt> elv{pt(2,2), pt(1,2), pt(0,0), pt(0,1), pt(0,2)};
		Rock el(elv); 
		vector<pt> vertv{pt(0,0), pt(1,0), pt(2,0), pt(3,0)};
		Rock vert(vertv); 
		vector<pt> sqv{pt(0,0), pt(0,1), pt(1,0), pt(1,1)};
		Rock square(sqv); 

		shapes.push_back(dash);
		shapes.push_back(cross);
		shapes.push_back(el);
		shapes.push_back(vert);
		shapes.push_back(square);

		int si = 0;
		int rocki = 0;

		set<pt> board;
		int max_height = 0;
		int llen = line.length();
		Rock curr = shapes[rocki];
		curr.place_on_top(board, max_height);

		while (true) {
			char c = line[si % llen];
			if (c == '<')
				curr.move_bottomleft(board, pt(0, -1), false);
			if (c == '>')
				curr.move_bottomleft(board, pt(0, 1), false);

			bool can_move = curr.move_bottomleft(board, pt(-1, 0), true);

			//cout<<"bottomleft"<<curr.bottomleft.fi<<","<<curr.bottomleft.se<<endl;

			if(!can_move) {
				//cout<<"finished rock "<<rocki<<endl;

				max_height = max(curr.bottomleft.fi + curr.bboxheight, max_height);
				bool fline = true;
				for (int j=0;j<7;j++) {

					if (!board.contains(pt(max_height-1, j)))
								fline = false;

				}
				if (fline)
					cout<<"ZOMG!!!"<<fline<<endl;
				rocki++;
				if (rocki == 2022){
					cout<<max_height<<endl;
					return 0;
				}
				curr = shapes[rocki % 5];
				curr.place_on_top(board, max_height);
			}
		

		si++;
	}

	return 0;
}

