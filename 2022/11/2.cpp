#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <sstream>
#include <deque>


#include <bits/stdc++.h>
using namespace std;


#define vc vector<char>
#define vi vector<int>
#define pp pair<string, Node*>
#define ll unsigned long long

int MOD = 9699690;

class Monkey {

	public:
	deque<ll> items;
	vector<Monkey*> * monkeys;
	long cnt;
	Monkey(deque<ll> items, vector<Monkey*>* monkeys) : items(items), monkeys(monkeys), cnt(0) {}

	virtual bool test(ll value){};
	virtual ll op(ll val){};
	virtual void true_op(ll val){};
	virtual void false_op(ll val){};

	void throow(ll mi, ll elem) {
		//cout<<"prev size"<<this->monkeys->at(mi)->items.size()<<endl;
		this->monkeys->at(mi)->push_back(elem);
		//cout<<"new size"<<this->monkeys->at(mi)->items.size()<<endl;
		return;
	}

	void push_back(ll elem) {
		this->items.push_back(elem);

	}

	void process() {

		ll ni = this->items.size();
		//cout<<"items:"<<ni<<endl;
		for(ll i=0;i<ni;i++) {

			ll item = this->items.front();this->items.pop_front();
			ll new_item = this->op(item) % MOD;

			if (new_item < item) {

				cout<<"overflo from "<<item<<" to "<<new_item<<endl;
			}
			bool test_res = this->test(new_item);
			if (test_res){ this->true_op(new_item);}
			else {this->false_op(new_item);};
			this->cnt++;
		}
	//cout<<"cnt:"<<this->cnt<<endl;
	}
};

class Monkey0 : public Monkey {
	public:
	Monkey0(deque<ll> items, vector<Monkey*>* monkeys) : Monkey(items, monkeys) {}
	bool test(ll value)  {return value % 13 == 0;}
	ll op(ll val) override {return val * 11;}
	void true_op(ll val) override {this->throow(4, val);}
	void false_op(ll val) override {this->throow(7, val);}
};
class Monkey1 : public Monkey {
	public:
	Monkey1(deque<ll> items, vector<Monkey*>* monkeys) : Monkey(items, monkeys) {}
	bool test(ll value)override{return value % 11 == 0;}
	ll op(ll val)override{return val + 4;}
	void true_op(ll val)override{this->throow(5, val);}
	void false_op(ll val)override{this->throow(3, val);}
};
class Monkey2 : public Monkey {
	public:
	Monkey2(deque<ll> items, vector<Monkey*>* monkeys) : Monkey(items, monkeys) {}
	bool test(ll value)override{return value % 2 == 0;}
	ll op(ll val)override{return val * val;}
	void true_op(ll val)override{this->throow(3, val);}
	void false_op(ll val)override{this->throow(1, val);}
};
class Monkey3 : public Monkey {
	public:
	Monkey3(deque<ll> items, vector<Monkey*>* monkeys) : Monkey(items, monkeys) {}
	bool test(ll value)override{return value % 5 == 0;}
	ll op(ll val)override{return val + 2;}
	void true_op(ll val)override{this->throow(5, val);}
	void false_op(ll val)override{this->throow(6, val);}
};


class Monkey4 : public Monkey {
	public:
	Monkey4(deque<ll> items, vector<Monkey*>* monkeys) : Monkey(items, monkeys) {}
	bool test(ll value)override{return value % 7 == 0;}
	ll op(ll val)override{return val + 3;}
	void true_op(ll val)override{this->throow(7, val);}
	void false_op(ll val)override{this->throow(2, val);}
};
class Monkey5 : public Monkey {
	public:
	Monkey5(deque<ll> items, vector<Monkey*>* monkeys) : Monkey(items, monkeys) {}
	bool test(ll value)override{return value % 3 == 0;}
	ll op(ll val)override{return val + 1;}
	void true_op(ll val)override{this->throow(0, val);}
	void false_op(ll val)override{this->throow(6, val);}
};
class Monkey6 : public Monkey {
	public:
	Monkey6(deque<ll> items, vector<Monkey*>* monkeys) : Monkey(items, monkeys) {}
	bool test(ll value)override{return value % 19 == 0;}
	ll op(ll val)override{return val + 5;}
	void true_op(ll val)override{this->throow(4, val);}
	void false_op(ll val)override{this->throow(0, val);}
};
class Monkey7 : public Monkey {
	public:
	Monkey7(deque<ll> items, vector<Monkey*>* monkeys) : Monkey(items, monkeys) {}
	bool test(ll value)override{return value % 17 == 0;}
	ll op(ll val)override{return val * 19;}
	void true_op(ll val)override{this->throow(2, val);}
	void false_op(ll val)override{this->throow(1, val);}
};


int main() {

	vector<Monkey*> ms;

	deque<ll> v0 = {63, 84, 80, 83, 84, 53, 88, 72};
	ms.push_back(new Monkey0(v0, &ms));

	deque<ll> v1 = {67, 56, 92, 88, 84};
	ms.push_back(new Monkey1(v1, &ms));

	deque<ll> v2 = {52};
	ms.push_back(new Monkey2(v2, &ms));

	deque<ll> v3 = {59, 53, 60, 92, 69, 72};
	ms.push_back(new Monkey3(v3, &ms));

	deque<ll> v4 = {61, 52, 55, 61};
	ms.push_back(new Monkey4(v4, &ms));

	deque<ll> v5 = {79, 53};
	ms.push_back(new Monkey5(v5, &ms));

	deque<ll> v6 = { 59, 86, 67, 95, 92, 77, 91};
	ms.push_back(new Monkey6(v6, &ms));

	deque<ll> v7 = {58, 83, 89};
	ms.push_back(new Monkey7(v7, &ms));

	
	for(ll i=0;i<10000;i++) {

//		cout<<"round "<<i<<endl;
		for(ll j=0;j<8;j++) {
			ms[j]->process();

		}
//		cout<<"---------------------"<<endl;

	}
	for (Monkey* m: ms) {

		cout<<"Monkey count: "<<m->cnt<<endl;
	}
	
	return 0;
}

