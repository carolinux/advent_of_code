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
#define t4 tuple<short int, short int, short int, short int>
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
    template<> struct hash<::t4> : boost::hash<::t4> {};
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


void prr(const t4& t){


	cout<<get<0>(t)<<","<<get<1>(t)<<","<<get<2>(t)<<","<<get<3>(t)<<endl;

}
void try_insert(unordered_map<t4, unordered_set<t4>> & states, t4& key, t4& val) {

	 auto it = states.find(key);
	 /*cout<<"Trying to insert ";
	 prr(key);prr(val);
	 cout<<"States size now "<<states.size()<<endl;
	 cout<<"States contains key "<<states.contains(key)<<endl;
	 */
	 if (!states.contains(key)) {
		 unordered_set<t4> sset;
		 sset.insert(val);
		 states.insert({key, sset}); 
		 //cout<<"Inserted key, now size="<<states.size()<<endl;
		 return;
	 }
	 // check vals
	// cout<<"inserting"<<endl;
	 bool skip_cand = false;

	 for(auto it2=it->second.begin();it2!=it->second.end();) {

		 const t4& rhs = *it2;
		 /*cout<<"we have "<<endl;
		 prr(val);
		 cout<<"comparing with"<<endl;
		 const t4& rhs = *it2;
		 */
		 //cout<<"hello"<<endl;
		 if (val == rhs){
			 ++it2;
			 continue;
		 }

		 if(get<0>(val) <= get<0>(rhs) && get<1>(val)<=get<1>(rhs) && get<2>(val) <= get<2>(rhs) && get<3>(val)<=get<3>(rhs)){

			skip_cand = true;
			break;
		 }
		 if(get<0>(val) >= get<0>(rhs) && get<1>(val)>=get<1>(rhs) && get<2>(val) >= get<2>(rhs) && get<3>(val)>=get<3>(rhs)){
			 it2 = it->second.erase(it2);

			 continue;
		 }
		 ++it2;

	}
	//cout<<"??"<<endl;
	
	if (!skip_cand)
	{
		it->second.insert(val);

	}



	/*
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
		states.insert(state);*/
}

int main() {
	string line;
	
	int id, oreore, clayore, obsore, obsclay, geore, geobs;
	int sum = 0;
	while (getline(cin, line)) {


		const char* linestr = line.c_str();
		int reads = sscanf(linestr,"Blueprint %d: Each ore robot costs %d ore. Each clay robot costs %d ore. Each obsidian robot costs %d ore and %d clay. Each geode robot costs %d ore and %d obsidian.", &id,&oreore,&clayore,&obsore, &obsclay, &geore, &geobs);

	cout<<"id "<<id<<" oreore"<<oreore<<" "<<geobs<<endl;
	unordered_map<t4, unordered_set<t4>> states;
	unordered_set<t4> sset;
	sset.insert(make_tuple(0,0,0,0));
	states.insert({make_tuple(1,0,0,0), sset});
	short int maxgeo = 0;


	for (int steps=1;steps<=25;steps++) {
		cout<<"=========="<<endl<<"STEP "<<steps<<" with state size "<<states.size()<<" and maxgeo so far "<<maxgeo<<endl<<"================="<<endl;
		unordered_map<t4, unordered_set<t4>> states2;

		for (auto it=states.begin();it!=states.end();it++) {

			auto key = it->first;
			auto valset = it->second;

			for (auto val : valset) {

			maxgeo = max(get<3>(val), maxgeo);
			if (steps==25)
				continue;

			//curr.pp();
			int dore = get<0>(key);
			int dclay = get<1>(key);
			int dobs = get<2>(key);
			int dgeo = get<3>(key);			

			// 5 options
			// also choose to not create a bot
			
			if (get<0>(val) >=oreore) {
				t4 ckey(key);
				t4 cval(val);
				get<0>(cval)= get<0>(cval) - oreore;
				get<0>(cval)= dore + get<0>(cval);
				get<1>(cval)= dclay + get<1>(cval);
				get<2>(cval)= dobs + get<2>(cval);
				get<3>(cval)= dgeo + get<3>(cval);

				get<0>(ckey)= get<0>(ckey) + 1;
				try_insert(states2, ckey, cval);

			}
			if (get<0>(val) >=clayore) {
				t4 ckey(key);
				t4 cval(val);
				get<0>(cval)= get<0>(cval) - clayore;
				get<0>(cval)= dore + get<0>(cval);
				get<1>(cval)= dclay + get<1>(cval);
				get<2>(cval)= dobs + get<2>(cval);
				get<3>(cval)= dgeo + get<3>(cval);

				get<1>(ckey) = get<1>(ckey) + 1;
				try_insert(states2, ckey, cval);

			}
			if (get<0>(val) >=obsore && get<1>(val) >= obsclay) {
				t4 ckey(key);
				t4 cval(val);

				get<0>(cval)= get<0>(cval) - obsore;
				get<1>(cval)= get<1>(cval) - obsclay;
				get<0>(cval)= dore + get<0>(cval);
				get<1>(cval)= dclay + get<1>(cval);
				get<2>(cval)= dobs + get<2>(cval);
				get<3>(cval)= dgeo + get<3>(cval);

				get<2>(ckey) = get<2>(ckey) + 1;

				try_insert(states2, ckey, cval);

			}
			if (get<0>(val) >= geore && get<2>(val) >= geobs) {
				t4 ckey(key);
				t4 cval(val);

				get<0>(cval)= get<0>(cval) - geore;
				get<2>(cval)= get<2>(cval) - geobs;
				get<0>(cval)= dore + get<0>(cval);
				get<1>(cval)= dclay + get<1>(cval);
				get<2>(cval)= dobs + get<2>(cval);
				get<3>(cval)= dgeo + get<3>(cval);

				get<3>(ckey) = get<3>(ckey) + 1;

				try_insert(states2, ckey, cval);

			}

			t4 ckey(key);
			t4 cval(val);
			get<0>(cval)=dore + get<0>(cval);
			get<1>(cval)=dclay + get<1>(cval);
			get<2>(cval)=dobs + get<2>(cval);
			get<3>(cval)=dgeo + get<3>(cval);
			//assert(dore>0);
			//assert(get<0>(ckey)>0);
			try_insert(states2, ckey, cval);
		}
		}
		states = states2;


	}
	cout<<"for id "<<id<<" we have max geo: "<<maxgeo<<endl;
	sum+= maxgeo * id;
	}

	cout<<"================"<<endl<<"Sum: "<<sum<<endl;

	return 0;
}

