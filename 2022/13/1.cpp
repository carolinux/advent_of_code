#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <sstream>
#include <queue>

#include <bits/stdc++.h>
using namespace std;


#define vc vector<char>
#define pt pair<int,int>
#define item pair<pair<int,int>, int>
class Elem {

	public:
	string * text;
	vector<Elem*>  children;
	int si;
	int ei;
	bool numeric = false;
	int num = 0;
	
	Elem(string* text, int si, bool numeric) : text(text), si(si), ei(-1), numeric(numeric), num(0) {}

	void print() {

		if (this->numeric) {

			cout<<"|"<<this->num<<"|";
		}
		else {
			cout<<"[";
			for( Elem* e: this->children) {
				e->print();


			}
			cout<<"]";
		}

	}

	// STRICTLY smaller
	bool smaller(Elem* right) {

		if (this->numeric && right->numeric) {
			cout<<"compare "<<this->num<<" vs "<<right->num<<endl;
			return this->num < right->num;


		}

		if (!this->numeric && !right->numeric) {
			
			int idx = 0;

			while (true) {
				cout<<this->children.size()<<" vs "<<right->children.size()<<" at idx "<<idx<<endl;
				int len_so_far = idx + 1;
				if (this->children.size() < len_so_far && right->children.size() >= len_so_far)
					return true;
				if (this->children.size() >= len_so_far && right->children.size() < len_so_far)
					return false;
				if (this->children.size() < len_so_far && right->children.size() < len_so_far)
					return false;

				Elem * lc = this->children.at(idx);
				Elem * rc = right->children.at(idx);
				if (lc->smaller(rc))
					return true;
				if (rc->smaller(lc))
					return false;
				// otherwise continue comparing
				idx++;

			}

		}

		if (this->numeric && !right->numeric) {

			Elem * conv = new Elem(this->text, this->si, false);
			conv->children.push_back(this);
			bool res =  conv->smaller(right);
			delete conv;
			return res;
		}
		if (!this->numeric && right->numeric) {

			Elem * conv = new Elem(right->text, right->si, false);
			conv->children.push_back(right);
			bool res =  this->smaller(conv);
			delete conv;
			return res;
		}

		



	}


	void build() {

		int maxi = (*text).length();
		int i = this->si;

		// what happens at end of string in both?
		
		if (this->numeric) {
			cout<<"numeric!"<<endl;
			while (i < maxi) {
				char ch = (*text)[i];
				if(ch -'0' >=0 && ch - '0' <=9) {
					int digit = ch -'0';
					this->num = (this->num * 10) + digit;
					i++;
				} 
				else {

					this->ei=i-1;
					return;


				}



			}
			this->ei = maxi - 1;

			return;
		}
		
		
		while (i<maxi) {

			char ch = (*text)[i];
			cout<<ch<<endl;
			if (ch == ',') {
				i++;
			}
			if (ch == ']') {
				this->ei = i;
				return;
			}
			if (ch=='[') {

				Elem * le = new Elem(this->text, i+1, false);
				le->build();
				this->children.push_back(le);
				i = le->ei + 1;
			}

			if(ch -'0' >=0 && ch - '0' <=9) {
				Elem * le = new Elem(this->text, i, true);
				le->build();
				this->children.push_back(le);
				i = le->ei + 1;

			}


		}
		return;
	}



};

const int NUM = 150;

int main() {
	/*string text = "[[1,24,3],4,5,[[2],[3,4,52]]]";
	//string text1 = "[[1],[2,3,4]]";
	//string text2 ="[[1],4]";
	string text1 = "[[[]]]";
	string text2 ="[[]]";
	Elem * elem1 = new Elem(&text1,0,false);
	elem1->build();
	elem1->print();
	
	Elem * elem2 = new Elem(&text2,0,false);
	elem2->build();
	elem2->print();
	cout<<"hellooo"<<endl;

	cout<<elem1->smaller(elem2)<<endl;
	/**/
	int sum = 0;
	for(int i=1;i<=150;i++) {
		string text1,text2,blank;
		getline(cin, text1);
		getline(cin, text2);
		getline(cin, blank);
		Elem * elem1 = new Elem(&text1,0,false);
		elem1->build();
		
		Elem * elem2 = new Elem(&text2,0,false);
		elem2->build();

		bool sm = elem1->smaller(elem2);
		if (sm)
			sum+=i;


	}

	cout<<"Res:"<<sum<<endl;
	return 0;
}

