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


vi expand(vi a, int blinks) {

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
    }
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

    a = expand(a, 35);
    /* this works but takes about 30 mins for the answer
    map<int, int> cache;

    int ans = 0;
    for (int j = 0; j < a.size(); j++) {
        cout<<j<<" out of "<<a.size()<<" num= "<<a[j]<<endl;
        if (cache.find(a[j]) != cache.end()){
            ans+=cache[a[j]];
            cout<<"cache hit for "<<a[j]<<endl;
            continue;
        }
        vi b;
        b.push_back(a[j]);
        b = expand(b, 40);
        cache[a[j]] = b.size();
        ans+=b.size();
        b.clear();

    }*/



    cout << ans<<endl;
    return 0;
   }
