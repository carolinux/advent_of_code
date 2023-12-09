#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <set>
//#include <multiset>
#include <vector>
#include <string>
#include <sstream>


#include <bits/stdc++.h>
using namespace std;


#define vc vector<char>

int main() {
	string line;
	int wsize = 14;
	int mi = -1;
	getline(cin, line);
	multiset<char> chars;

	for (int i=0;i<line.length();i++) {
		set<char> tmp;
		char ch = line[i];
		int ci = i+1;
		// remove previous
		if (i>=wsize) {
			char to_del = line[i-wsize];
			auto it = chars.find(to_del);
			chars.erase(it);

		}
		// add curr
		chars.insert(ch);
		for (auto x: chars) {

			tmp.insert(x);
		}

		if (tmp.size() == wsize) {

			mi = ci;
			break;
		}


	}


	cout<<"First marker index:"<<mi<<endl;
	return 0;
}

/*
#include <iostream>
#include <string>
#include <stringstream>

int main() {
    std::string my_string = " Hello   world!  ";
    std::string str1, str2;
    std::stringstream s(my_string);

    s>>str1>>str2;

    std::cout<<str1<<std::endl;
    std::cout<<str2<<std::endl;
    return 0;
}*/
