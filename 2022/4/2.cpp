#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <set>
#include <vector>


#include <bits/stdc++.h>
using namespace std;


bool disjoint(int x1, int y1, int x2, int y2) {

	return y1 < x2 || y2 < x1;

}

int main() {
	string line;
	int sum = 0;
	int i = 0;
	
	set<char> so_far;
	
	while (getline(cin, line))
	{
	
	vector<int> arr;
	int curr = 0;
	for (auto ch: line) {
		
		if (ch == '-' || ch == ',') {
			arr.push_back(curr);
			curr = 0;
			continue;
		
		}
		int digit = ch - '0';
		curr = curr * 10 + digit;
	
	}
	arr.push_back(curr);
	
	int a,b,c,d;
	a = arr[0];b=arr[1];c=arr[2];d=arr[3];
	
	//cout<<a<<"-"<<b<<" vs "<<c<<"-"<<d<<"at "<<line<<endl;
	
	
	if (!disjoint(a,b,c,d)) {
	
		sum+=1;
	}	

	

	}
    	cout<<"Total sum is "<<sum<<endl;
	return 0;
}
