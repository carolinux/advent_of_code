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
#define pp pair<string, Node*>

class Node {

	public:
	long bytes;
	Node * parent;
	string name;
	set<string> fnames;
	map<string, Node*> dirnames;
	vector<Node*> children;

	// constructor
	//
	Node(Node* parent, string name) : parent(parent), name(name) {}

	bool contains_file(string fname) {
		return fnames.find(fname) != fnames.end();
	}

	void add_file(string fname) {
		fnames.insert(fname);
		return;
	}
	bool contains_dir(string dname) {
		return dirnames.find(dname) != dirnames.end();
	}
	Node* get_dir(string dname) {
		return dirnames.find(dname)->second;
	}
	void add_dir(string dname) {
		Node * child = new Node(this, dname);
		dirnames.insert(pp(dname, child));
		return;
	}
	~Node() {

		cout<<"destroying "<<this->name<<endl;
	}
};


long search(Node* curr, vector<long> &res) {
	//cout<<"Now at "<<curr->name<<endl;

	if (curr->dirnames.size() == 0) {

		res.push_back(curr->bytes);		
		return curr->bytes;

	}

	long sum = curr->bytes;

	for (auto me: curr->dirnames) {

		long to_add = search(me.second, res);
		sum+=to_add;

	}


	res.push_back(sum);
	return sum;
	}



int main() {
	string line;
	int sum = 0;


	Node* curr = nullptr;
	Node* root = nullptr;
	
	while (getline(cin, line))
	{
	
	
	stringstream s(line);
	string first;
	s>>first;

	if (first[0] == '$') {

		// parse command
		string op1, op2;
		s>>op1;

		if (op1 == "cd"){
			s>>op2;
//			cout<<"op2:"<<op2<<endl;

			if (op2 == "/") {

				root = new Node(nullptr, op2);
				curr = root;
			}
			else if (op2 == "..") {

				curr = curr->parent;
			}
			else {

				curr = curr->get_dir(op2);

			}

		}

//		cout<<"op1:"<<op1<<endl;
			


	}
	else if (first == "dir") {
		string dirname;
		s>>dirname;
		if(! curr->contains_dir(dirname)) {
			curr->add_dir(dirname);
		}

	}
	else {
		// first is a number of bytes of a file..
		string fname;
		s>>fname;
		long bytes = stoi(first);
		if(! curr->contains_file(fname)) {
			curr->bytes+=bytes;
			curr->add_file(fname);
		}
	}


	//cout<<"After: "<<line<<" i am at "<<curr->name<<endl;
	

	

	}


	vector<long> res;

	search(root, res);

	cout<<"total size of fs:"<<res.back()<<endl;
	long free_space = 70000000 - res.back();
	long to_exceed = 30000000 - free_space;
	cout<<"Must find smallest dir that exceeds "<<to_exceed<<endl;
	long min_diff = 30000000;
	for (auto dsize: res) {

		if (dsize<to_exceed) {
			continue;
		}
		long diff = dsize - to_exceed;
		min_diff = min(min_diff, diff);
	}

	cout<<"Sum: "<<to_exceed + min_diff<<endl;
	
	return 0;
}

