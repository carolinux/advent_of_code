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

#include <bits/stdc++.h>
using namespace std;


#define vc vector<char>
#define vi vector<int>
#define vsi vector<set<int>>
#define pt pair<int,int>
#define edge pair<pair<int,int>, pair<int,int>>
#define f first
#define s second

#define FOR(k,a,b) for(auto k=(a); k < (b); ++k)

set<pt> DS = {pt(1,0), pt(1,-1), pt(1,1)};

void printv(vi & v) {
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

int main() {
	string line;
	
	vector<set<int>> colsets(600);	
	set<pt> beacons;
	set<pt> ss;
	vector<pt> sensors;
	vector<int> mindist;
	int minx = 10000000;
	int miny = 10000000;
	int maxx = 0;
	int maxy = 0;
	int maxdist = 0;

	while (getline(cin, line)) {

		const char* linestr = line.c_str();
		int x1,y1,x2,y2;
		//Sensor at x=2543342, y=3938: closest beacon is at x=2646619, y=229757
		int reads = sscanf(linestr,"Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d", &x1,&y1,&x2,&y2);
		sensors.push_back(pt(x1,y1));
		ss.insert(pt(x1,y1));
		beacons.insert(pt(x2,y2));
		int dist = abs(x2-x1) + abs(y2-y1);
		maxdist = max(dist, maxdist);
		mindist.push_back(dist);
		maxx = max(x1, maxx);
		maxx = max(x2, maxx);
		maxy = max(y1, maxy);
		maxy = max(y2, maxy);
		minx = min(x1, minx);
		minx = min(x2, minx);
		miny = min(y1, miny);
		miny = min(y2, miny);
	}
	int res = 0;
	cout<<"sensors "<<sensors.size()<<endl;
	printv(mindist);
	return 0;
	for (int x=minx-2*maxdist;x<=maxx+2*maxdist;x++) {

		int y = 2000000;
		if (beacons.find(pt(x,y)) != beacons.end())
		{
			continue;}
		bool impossible_beacon = false;
		for (int i=0;i<sensors.size();i++) {

			int curr_dist = abs(x - sensors[i].f) + abs(y-sensors[i].s);
			//cout<<curr_dist<<" vs "<<mindist[i]<<"current position is closer to sensor than closest beacon?"<<bool(curr_dist<mindist[0])<<endl;;
			if (curr_dist <= mindist[i]) {
				impossible_beacon=true;
				break;
			}
			else { continue;}
		}
		if (impossible_beacon)
			res++;
		else{
			if (x>=0 && x <=4000000)
				cout<<"Found possible beacon at "<<x<<","<<y<<endl;
		}
				

	}

	cout<<"res:"<<res<<endl;
	return 0;
}

