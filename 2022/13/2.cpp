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
	int marker = 0;
	
	Elem(string* text, int si, bool numeric, int marker=0) : text(text), si(si), ei(-1), numeric(numeric), num(0), marker(marker) {}

	void print(bool cmp=false) {

		if (this->numeric) {

			cout<<"|"<<this->num<<"|";
		}
		else {
			if(!cmp)
				cout<<"[";

			for( Elem* e: this->children) {
				e->print();


			}
			if(!cmp)
				cout<<"]";
		}

		if (cmp)
			cout<<" compared to "<<*(this->text)<<endl;
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

// iz ok to use a ref here 
bool compare(Elem& left, Elem& right) {
	return left.smaller(&right);

}

const int NUM = 150;

int main() {
	string text1 = "[[8,10,4,[[],1,2,8,8],8]]";
	string text2 ="[[]]";
	Elem * elem1 = new Elem(&text1,0,false);
	elem1->build();
	elem1->print();
	
	//return 0;

	//cout<<elem1->smaller(elem2)<<endl;
	/**/

	vector<Elem> elems;

	int sum = 0;
	for(int i=1;i<=150;i++) {
		string blank;
		string * text1 = new string;
		string * text2 = new string;
		getline(cin, *text1);
		getline(cin, *text2);
		getline(cin, blank);
		Elem * elem1 = new Elem(text1,0,false);
		elem1->build();
		
		Elem * elem2 = new Elem(text2,0,false);
		elem2->build();
		elems.push_back(*elem1);
		elems.push_back(*elem2);



	}
	string string2 = "[[2]]";
	string string6 = "[[6]]";
	Elem * elem2 = new Elem(&string2, 0, false, 2);
	elem2->build();
	Elem * elem6 = new Elem(&string6, 0, false, 6);
	elem6->build();
	elems.push_back(*elem2);
	elems.push_back(*elem6);
	int pos2 = -1;
	int pos6 = -1;
	sort(elems.begin(), elems.end(), compare);
	int ix = 1;
	for(Elem& elem: elems){

		elem.print(true);
		cout<<endl;
		//
		if (elem.marker == 2)
			pos2 = ix;
		if (elem.marker == 6)
			pos6 = ix;
		ix++;
	}

	cout<<"Res:"<<pos2 * pos6<<endl;
	cout<<ix<<endl;
	elem2->print();
	elem6->print();
	return 0;
}

