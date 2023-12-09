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


struct Entry {

	int num;
	int idx;
	
	Entry(int num, int idx):num(num), idx(idx) {
	
	}


	};


/*
void swap(int idx1, int idx2, map<int, Entry*>& idx2entry) {
	Entry * tmp = idx2entry[idx1];
	idx2entry[idx1] = idx2entry[idx2];
	idx2entry[idx2] = entry;
	idx2entry[idx2]->idx = idx2;
	idx2entry[idx1]->idx = idx1;

}*/


void move_back(int idx, map<int, Entry*> &idx2entry, int vsize) {

	int previ = idx -1;
	if (previ<0)
		previ = vsize -1;
	Entry * entry = idx2entry[idx];
	entry->idx = previ;
	idx2entry[previ] = entry;

}

void move_front(int idx, map<int, Entry*> &idx2entry, int vsize) {

	int previ = idx + 1;
	if (previ>=vsize)
		previ = 0;
	Entry * entry = idx2entry[idx];
	entry->idx = previ;
	idx2entry[previ] = entry;

}

void debug_print(map<int, Entry*> &idx2entry, int vsize) {

	for (int i=0;i<vsize;i++)
		cout<<idx2entry[i]->num<<",";

	cout<<endl;

}

int main() {
	string line;

	int idxi = 0;
	vector<Entry*> to_process;
	map<int, Entry*> idx2entry;

	while (getline(cin, line)) {
		int num = stoi(line);
		Entry * entry = new Entry(num, idxi);
		to_process.push_back(entry);
		idx2entry.insert({idxi, entry});
		idxi++;

	}
	int vsize = to_process.size();
	//cout<<-2%7<<endl;
	//return 0;

	//debug_print(idx2entry, vsize);
	for (Entry * entry: to_process) {


		int num = entry->num;
		if (num==0)
			continue;
		int idx1 = entry->idx;
		int idx2 = (idx1 + num) % (vsize);
		if (idx2<0)
			idx2 = vsize + idx2;

		// wrapped around zero
		if (num<0 && (idx2>idx1)) {
			idx2--;
			
		}
		if (num<0 && idx2==0) {
			idx2 = vsize-1;
		}
		if (num>0 && idx2==vsize-1) {
			idx2 = 0;
		}
		// wrapped around the end
		if (num>0 && (idx2<idx1)) {
			idx2++;
		}
			


		/*
		if (num<0){
			idx2--;
			if (idx2<0)
				idx2 = vsize-1;

		}*/

		int diff = idx2 - idx1;
		cout<<"initial idx of "<<num<<"="<<idx1<<" new idx "<<idx2<<" diff:"<<diff<<endl;
		if (diff == 0)
			continue;
		if (diff>0) {

			//cout<<"positive diff "<<(idx+1<=idx2)<<endl;
			for (int i=idx1+1;i<=idx2;i++) {
				assert(idx2entry[i]->idx == i);
		//		cout<<"Moving "<<idx2entry[i]->num<<" from "<<i<<" to "<<i-1<<endl;
				move_back(i, idx2entry, vsize);
				// the entry at idx i needs to move to i-1

			}

		}
		else {
			/*
			for(int i=idx1+1;i<vsize;i++){
				move_back(i, idx2entry, vsize);
			}
			for(int i=0;i<=idx2;i++){
				move_back(i, idx2entry, vsize);
			}*/
			for (int i=idx1-1;i>=idx2;i--) {
				assert(idx2entry[i]->idx == i);
		//		cout<<"Moving "<<idx2entry[i]->num<<" from "<<i<<" to "<<i-1<<endl;
				move_front(i, idx2entry, vsize);
			}


		}

		entry->idx = idx2;
		idx2entry[idx2] = entry;

		debug_print(idx2entry, vsize);

	}

	int zeroi = 0;

	for(int i=0;i<idx2entry.size();i++) {

		if (idx2entry[i]->num==0) {

			zeroi = i;
			break;
		}

	}

	int sum = 0;

	int counter = 1;
	int i = zeroi + 1;
	while(true) {
		i = i % vsize;
		if (counter == 1000 || counter == 2000 || counter == 3000)
		{
			cout<<idx2entry[i]->num<<endl;
			sum+=idx2entry[i]->num;
		}

		if (counter == 3000)
			break;
		
		counter++;
		i++;

	}


	cout<<"res:"<<sum<<endl;
	return 0;
}

