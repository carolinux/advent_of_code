#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <sstream>
#include <thread>
#include <chrono>
#include <map>

using namespace std;
#define int unsigned long long
#define vi vector<unsigned long long>


int uniqueCount(std::vector<int> vec) {
    // Sort the vector
    std::sort(vec.begin(), vec.end());
    // Remove duplicates
    auto last = std::unique(vec.begin(), vec.end());
    // Resize the vector to remove undefined elements
    vec.erase(last, vec.end());
    // The size of the modified vector gives the unique count
    return vec.size();
}


vi expand(vi a, int blinks, bool print) {

    for (int i = 0; i < blinks; i++) {
       vector<int> newa;
       //cout<<"Before blink "<<i+1<<": "<<a.size()<<endl;

       /*for (int j = 0; j < a.size(); j++) {
        cout<<a[j]<<" ";
       }
       cout<<endl;
std::this_thread::sleep_for(std::chrono::seconds(2));*/

       for (int j = 0; j < a.size(); j++) {
           int num = a[j];
           if (num == 0) {
               newa.push_back(1);
               continue;
           }
           // cast to string
           string numStr = to_string(num);
           if (numStr.size() % 2 == 0) {
               int num1 = stoll(numStr.substr(0, numStr.size() / 2));
                int num2 = stoll(numStr.substr(numStr.size() / 2, numStr.size()));
               newa.push_back(num1);
               newa.push_back(num2);
               continue;
           }
           newa.push_back(2024 * num);
       }
       a = newa;
       if (print) {
        int uniq = uniqueCount(a);
        cout<<"at iteration "<<i+1<<"we have "<<uniq<<" unique elements"<<endl;
       }
    }
    //print number of unique


    return a;

}

signed main() {

    string inputLine;
    getline(std::cin, inputLine);
    istringstream inputStream(inputLine);
    vi a;
    int number;

    while (inputStream >> number) {
        a.push_back(number);
    }

    a = expand(a, 25, false);
    map<int, int> cache;

    int ans = 0;
    for (int j = 0; j < a.size(); j++) {
        cout<<j<<" out of "<<a.size()<<endl;
        vi b;
        b.push_back(a[j]);
        b = expand(b, 25, false);
        for (int k=0;k<b.size();k++) {
            vi c;
            if (cache.find(b[k]) != cache.end()) {
                ans+=cache[b[k]];
                continue;
            }
            c.push_back(b[k]);
            c = expand(c, 25, false);
            ans+=c.size();
            cache[b[k]] = c.size();
            c.clear();

        }
        b.clear();

    }



    cout << ans<<endl;
    return 0;
   }
