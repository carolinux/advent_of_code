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
#define pt pair<int,int>

int main() {
	string line;
	int arr[99][99];
	int ro = 99;int co = 99;
	int mi = -1;
	
	int r = 0;

	int res = 0;

	
	while (getline(cin, line)) {
		for(int c=0;c<co;c++) {
			char ch = line[c];
			int num = ch - '0';
			arr[r][c] = num;
		}
		r++;
	}

	int maxs = 0;

	for(int r=0;r<ro;r++) {
		for(int c=0;c<co;c++) {

			int height = arr[r][c];

			int ls = 0;
			int rs = 0;
			int us = 0;
			int ds=0;

			int i = c-1;

			while(i>=0) {
				ls++;

				if (arr[r][i]>=height) {
					break;

				}
				i--;
			}

			i = c+1;

			while(i<co) {
				rs++;

				if (arr[r][i]>=height) {
					break;

				}
				i++;
			}
			i = r-1;

			while(i>=0) {
				ds++;

				if (arr[i][c]>=height) {
					break;

				}
				i--;
			}

			i = r+1;

			while(i<ro) {
				us++;

				if (arr[i][c]>=height) {
					break;

				}
				i++;
			}



			int score = ls * rs * us * ds;


			maxs = max(score, maxs);
		}

	}


	cout<<"Res:"<<maxs<<endl;



	return 0;
}

