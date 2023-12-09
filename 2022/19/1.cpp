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
#define f first
#define s second

set<pt> DS = {pt(1,0), pt(1,-1), pt(1,1)};


struct t8 {

	short int orebots;
	short int claybots;
	short int obsbots;
	short int geobots;
	short int ore;
	short int clay;
	short int obs;
	short int geo;

	t8(int orebots, int claybots, int obsbots, int geobots, int ore, int clay, int obs, int geo): orebots(orebots), claybots(claybots), obsbots(obsbots), geobots(geobots), ore(ore), clay(clay), obs(obs), geo(geo) {
	};

	void pp() {


		cout<<"ore:"<<ore<<", orebots"<<orebots<<endl;
		cout<<"caly:"<<clay<<", claybots"<<claybots<<endl;
		cout<<"obs:"<<obs<<", obsbots"<<obsbots<<endl;
		cout<<"geo:"<<geo<<", geo"<<geobots<<endl;

	}


	const bool operator == ( const t8 &o ) const{

		return (orebots == o.orebots && claybots == o.claybots && obsbots == o.obsbots && geobots == o.geobots && ore == o.ore && clay == o.clay && obs == o.obs && geo == o.geo); 
	}


	const bool operator < ( const t8 &o ) const{

		bool eq =  (orebots == o.orebots && claybots == o.claybots && obsbots == o.obsbots && geobots == o.geobots && ore == o.ore && clay == o.clay && obs == o.obs && geo == o.geo); 

		return !eq && (orebots <= o.orebots && claybots <= o.claybots && obsbots <= o.obsbots && geobots <= o.geobots && ore <= o.ore && clay <= o.clay && obs <= o.obs && geo <= o.geo); 
	}
	const bool operator > ( const t8 &o ) const{

		bool eq =  (orebots == o.orebots && claybots == o.claybots && obsbots == o.obsbots && geobots == o.geobots && ore == o.ore && clay == o.clay && obs == o.obs && geo == o.geo); 

		return !eq && (orebots >= o.orebots && claybots >= o.claybots && obsbots >= o.obsbots && geobots >= o.geobots && ore >= o.ore && clay >= o.clay && obs >= o.obs && geo >= o.geo); 
	}

	/*
	const bool operator < ( const t8 &o ) const{

		return (orebots < o.orebots) ||
			(orebots == o.orebots && claybots < o.claybots) || 
			(orebots == o.orebots && claybots == o.claybots && obsbots < o.obsbots) || 
			(orebots == o.orebots && claybots == o.claybots && obsbots == o.obsbots && geobots < o.geobots) || 
			(orebots == o.orebots && claybots == o.claybots && obsbots == o.obsbots && geobots == o.geobots && ore < o.ore) || 
			(orebots == o.orebots && claybots == o.claybots && obsbots == o.obsbots && geobots == o.geobots && ore == o.ore && clay < o.clay) || 
			(orebots == o.orebots && claybots == o.claybots && obsbots == o.obsbots && geobots == o.geobots && ore == o.ore && clay == o.clay && obs < o.obs) || 
			(orebots == o.orebots && claybots == o.claybots && obsbots == o.obsbots && geobots == o.geobots && ore == o.ore && clay == o.clay && obs == o.obs && geo < o.geo); 
		
		
    }*/


};
auto as_tuple(t8 const& v) -> decltype(auto)
{
    return std::tie(v.orebots, v.claybots, v.obsbots, v.geobots, v.ore, v.clay, v.obs, v.geo);
}



// hash_value implemented in terms of tuple, for consistency and simplicity
std::size_t hash_value(t8 const& v)
{
    using boost::hash_value;
    return hash_value(as_tuple(v));
}


namespace std {
    template<> struct hash<::t8> : boost::hash<::t8> {};
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

void try_insert(unordered_set<t8> & states, t8 state) {

	if (states.size() == 0) {
		//cout<<"inserted becuz empty"<<endl;
		states.insert(state);
		return;
	}
	vector<t8> to_remove;
	bool found_one_that_is_clearly_better = false;

	for(auto rival: states) {
		if (state<rival)
			found_one_that_is_clearly_better = true;

		if(state>rival)
			to_remove.push_back(rival);

	}
	for (auto rem: to_remove)
		states.erase(rem);
	
	if (!found_one_that_is_clearly_better)
		states.insert(state);
}

int main() {
	string line;
	
	int id, oreore, clayore, obsore, obsclay, geore, geobs;
	int sum = 0;
	while (getline(cin, line)) {


		const char* linestr = line.c_str();
		int reads = sscanf(linestr,"Blueprint %d: Each ore robot costs %d ore. Each clay robot costs %d ore. Each obsidian robot costs %d ore and %d clay. Each geode robot costs %d ore and %d obsidian.", &id,&oreore,&clayore,&obsore, &obsclay, &geore, &geobs);

	cout<<"id "<<id<<" oreore"<<oreore<<" "<<geobs<<endl;
	unordered_set<t8> states;
	t8 start(1, 0, 0, 0, 0, 0, 0, 0);
	states.insert(start);
	//return 0;
	short int maxgeo = 0;


	for (int steps=1;steps<=25;steps++) {
		cout<<"=========="<<endl<<"STEP "<<steps<<" with state size "<<states.size()<<" and maxgeo so far "<<maxgeo<<endl<<"================="<<endl;
		unordered_set<t8> states2;

		for (t8 curr: states) {
			maxgeo = max(curr.geo, maxgeo);
			if (steps==25)
				continue;

			//curr.pp();
			int dore = curr.orebots;
			int dclay = curr.claybots;
			int dobs = curr.obsbots;
			int dgeo = curr.geobots;			

			// 5 options
			// also choose to not create a bot
			
			if (curr.ore >=oreore) {
				t8 cand(curr);
				cand.ore-=oreore;
				cand.ore+=dore;
				cand.clay+=dclay;
				cand.obs+=dobs;
				cand.geo+=dgeo;
				cand.orebots++;
				try_insert(states2, cand);

			}
			if (curr.ore >=clayore) {
				t8 cand(curr);
				cand.ore-=clayore;
				cand.ore+=dore;
				cand.clay+=dclay;
				cand.obs+=dobs;
				cand.geo+=dgeo;
				cand.claybots++;
				try_insert(states2, cand);

			}
			if (curr.ore >=obsore && curr.clay >= obsclay) {

				t8 cand(curr);
				cand.ore-=obsore;
				cand.clay-=obsclay;
				cand.ore+=dore;
				cand.clay+=dclay;
				cand.obs+=dobs;
				cand.geo+=dgeo;
				cand.obsbots++;
				try_insert(states2, cand);

			}
			if (curr.ore >= geore && curr.obs >= geobs) {
				t8 cand(curr);
				cand.ore-=geore;
				cand.obs-=geobs;
				cand.ore+=dore;
				cand.clay+=dclay;
				cand.obs+=dobs;
				cand.geo+=dgeo;
				cand.geobots++;
				try_insert(states2, cand);

			}

			t8 cand(curr);
			cand.ore+=dore;
			cand.clay+=dclay;
			cand.obs+=dobs;
			cand.geo+=dgeo;
			try_insert(states2, cand);
		}
		states = states2;


	}
	cout<<"for id "<<id<<" we have max geo: "<<maxgeo<<endl;
	sum+= maxgeo * id;
	}

	cout<<"================"<<endl<<"Sum: "<<sum<<endl;

	return 0;
}

