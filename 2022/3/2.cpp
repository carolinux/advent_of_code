#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <set>
#include <vector>


#include <bits/stdc++.h>
using namespace std;

int main() {
	string line;
	int sum = 0;
	int i = 0;
	
	set<char> so_far;
	
	while (getline(cin, line))
	{
		i+=1;
    		set<char> curr(line.begin(), line.end());
    		if (i%3 == 1) {
    			so_far = curr;
    		}
    		
    		else {
    			vector<char> v; // why !?
    			set_intersection(curr.begin(), curr.end(), so_far.begin(), so_far.end(), back_inserter(v));
    			so_far = set<char>(v.begin(), v.end());
    		 }
    		if (i % 3 == 0) {
    			char ch2 = *so_far.begin();
    			cout<<"Char:"<<ch2<<endl;
    			
			int incr = 0;
			
			if (int(ch2) > int('Z') ) {incr = int(ch2)-int('a')+1;}
			else { incr = 26 + int(ch2) - int('A') + 1;}
			sum+=incr;
    		
    		
    		}

	}
    	cout<<"Total sum is "<<sum<<endl;
	return 0;
}
