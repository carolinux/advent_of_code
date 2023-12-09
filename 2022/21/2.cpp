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
	bool mark;
	char op;
	ll val;
	Node(string node, ll val):node(node), val(val), op('!'), left(""), right(""), processed(false), mark(false) {};
	Node(string node, string left, string right, char op):node(node), val(-1), op(op), left(left), right(right), processed(false), mark(false){};

	void pp() {

		cout<<"Node "<<node<<"with precomp val="<<val<<" procesed="<<processed<<", mark="<<mark<<" op="<<op<<endl;

	}

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


ll dfs(Node* curr, map<string, Node*> &nodes, unordered_set<string> &seen) {

	seen.insert(curr->node);
	if (curr->is_leaf() || curr->processed){
		curr->processed= true;
		return curr->val;
	}


	Node * left = nodes[curr->left];
	Node * right = nodes[curr->right];

	ll leftres = dfs(left, nodes, seen);
	ll rightres = dfs(right, nodes, seen);

	ll res = curr->get_result(leftres, rightres);
	curr->val = res;
	curr->processed = true;
	if (curr->node == "root"){
		assert(curr->processed);
		cout<<"root addr"<<curr<<endl;
	}
	return res;

}


bool find_path(Node * curr, map<string, Node*> & nodes, string& target) {

	if (curr->node==target) {

		curr->mark = true;
		return true;
	}

	if (curr->is_leaf())
		return false;

	bool res1 = find_path(nodes[curr->left], nodes, target);
	bool res2 = find_path(nodes[curr->right], nodes, target);

	bool res = res1 || res2;
	assert(res1 == false  || res2 == false);
	//assert(res1 == true  || res2 == true);

	if (res)
		curr->mark = true;
	return res;

}


ll get_left_val(ll target, char op, ll rhs) {

	if (op=='+')
		return target - rhs;
	if (op=='*')
		return target / rhs;
	if (op=='-')
		return target + rhs;
	if (op=='/')
		return target * rhs;
	throw exception();

}

ll get_right_val(ll target, char op, ll lhs) {

	if (op=='+')
		return target - lhs;
	if (op=='*')
		return target / lhs;
	if (op=='-')
		return lhs - target;
	if (op=='/')
		return lhs/target;
	throw exception();

}
void dfs2(Node * curr, map<string, Node*> & nodes, ll target) {

	if (curr->is_leaf()) {

		assert(curr->node=="humn");
		cout<<"We should shout the value "<<target<<endl;
		return;
	}

	Node * left = nodes[curr->left];
	Node * right = nodes[curr->right];
	assert(left->mark || right->mark);
	assert(!left->mark || !right->mark);
	curr->pp();
	left->pp();
	right->pp();
	
	assert(left->processed);
	assert(right->processed);

	bool go_left = left->mark;
	Node * next;
	ll new_target;
	if(go_left) {
		next = left;
		new_target = get_left_val(target, curr->op, right->val);}
		

	else {
		next=right;
		new_target = get_right_val(target, curr->op, left->val);

	}



	return dfs2(next, nodes, new_target);


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
	unordered_set<string> seen;
	ll resl = dfs(root, nodes, seen);
	cout<<"rout address 2 "<<root<<endl; 
	assert(root->processed);
	string hooman = "humn";
	find_path(root, nodes, hooman);
	assert(root->mark);
	root->op = '-';
	dfs2(root, nodes, 0);
//	cout<<"result:"<<res<<endl;

	return 0;
}

