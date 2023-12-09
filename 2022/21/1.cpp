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
#define f first
#define s second
#define ll long long

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

triplet mk_triplet(int a, int b, int c) {
	return pair(pair(a,b), c); 

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


struct Node {

	string node;
	string left;
	string right;
	bool processed;
	char op;
	ll val;
	Node(string node, ll val):node(node), val(val), op('!'), left(""), right(""), processed(false) {};
	Node(string node, string left, string right, char op):node(node), val(-1), op(op), left(left), right(right), processed(false) {};

	bool is_leaf() {return op=='!';}

	ll get_result(ll op1, ll op2) {

	if (op=='+')
		return op1+op2;
	if (op=='-')
		return op1-op2;
	if (op=='*')
		return op1*op2;
	if (op=='/')
		return op1/op2;
	throw exception();


	}

};


ll dfs(Node* curr, map<string, Node*> &nodes) {

	if (curr->is_leaf() || curr->processed)
		return curr->val;


	Node * left = nodes[curr->left];
	Node * right = nodes[curr->right];

	ll leftres = dfs(left, nodes);
	ll rightres = dfs(right, nodes);

	ll res = curr->get_result(leftres, rightres);
	curr->val = res;
	curr->processed = true;
	return res;

}

int main() {
	string line;
	

	map<string, Node*> nodes;
	while (getline(cin, line)) {

		stringstream s(line);
		string nodestr;
		string is_leaf;
		s>>nodestr>>is_leaf;
		Node * node;


		if (is_leaf=="leaf") {
			ll val;
			s>>val;
			node = new Node(nodestr, val);


		}
		else {
			string left, right;
			char op;
			s>>left>>op>>right;
			node = new Node(nodestr, left, right, op);


		}
		nodes.insert({nodestr, node});
	}

	Node * root = nodes["root"];
	ll res = dfs(root, nodes);
	cout<<"result:"<<res<<endl;

	return 0;
}

