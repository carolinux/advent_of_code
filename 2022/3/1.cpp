#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <set>

using namespace std;

int main() {
	string line;
	int sum = 0;
	while (getline(cin, line))
	{
    		//std::cout << line << std::endl;
    		int l = line.length();
    		int hl = l>>1;
    		set<char> first(line.begin(), line.begin() + hl);
    		//for (auto i: first)
    		//cout<<i<<endl;
    		//cout<<"Line length:"<<l<<endl;
    		//cout<<"half len:"<<first.size()<<endl;
    		for(int i=hl;i<l;i++) {
    			char ch2 = line[i];
    			if (first.find(ch2) != first.end()) {
    			
    				//cout<<"Extra char is "<<ch2<<int(ch2)<<endl;
    				
    				int incr = 0;
    				
    				if (int(ch2) > int('Z') ) {incr = int(ch2)-int('a')+1;}
    				else { incr = 26 + int(ch2) - int('A') + 1;}
    				
    				
    				
    				
    				sum+=incr;
    				break;
    			}
    		}
    		
    		
    	//cout<<"Total sum is "<<sum<<endl;
    	//cout<<int('a')<<endl;
    	//cout<<int('A')<<endl;
	}
    	cout<<"Total sum is "<<sum<<endl;
	return 0;
}
