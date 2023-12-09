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

int main() {
	string line;

	vector<vector<char>> vv;
	vv.push_back(vector<char>());
	vv.push_back(vc({'J','H','P','M','S', 'F','N','V'}));
	vv.push_back(vc({'S','R','L','M','J', 'D','Q'}));
	vv.push_back(vc({'N','Q','D','H','C', 'S','W','B'}));
	
	vv.push_back(vc({'R','S','C','L'}));
	vv.push_back(vc({'M','V','T','P','F', 'B'}));
	vv.push_back(vc({'T','R','Q','N','C'}));
	
	vv.push_back(vc({'G','V','R'}));
	vv.push_back(vc({'C','Z','S','P','D', 'L','R'}));
	vv.push_back(vc({'D','S','J','V','G', 'P','B','F'}));
	
	while (getline(cin, line))
	{
	
	if (line[0] != 'm') {
	
		continue;
	}
	
	stringstream s(line);
	//move x for a to b
	string tmp1, tmp2, tmp3;
	int num, src, tgt;
	s>>tmp1>>num>>tmp2>>src>>tmp3>>tgt;
	/*cout<<line<<endl;
	//cout<<num<" "<<src<<" "<<tgt<<endl;
	cout<<src<<endl;*/

	for(int i=0;i<num;i++) {

		char elem = vv[src].back(); vv[src].pop_back();
		vv[tgt].push_back(elem);


	}
	

	

	}
	for (int i=1;i<=9;i++) {
		int len = vv[i].size();
		cout<<vv[i][len-1];
	}
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
