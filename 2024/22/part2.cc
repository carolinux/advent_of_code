#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <tuple>
#include <algorithm>
#include <string>
#include <sstream>
#include <functional>

using namespace std;
#define ull unsigned long long


// Custom hash function for std::tuple<int, int, int, int>
struct TupleHash {
    size_t operator()(const tuple<int, int, int, int>& t) const {
        size_t hash1 = hash<int>{}(get<0>(t));
        size_t hash2 = hash<int>{}(get<1>(t));
        size_t hash3 = hash<int>{}(get<2>(t));
        size_t hash4 = hash<int>{}(get<3>(t));
        return hash1 ^ (hash2 << 1) ^ (hash3 << 2) ^ (hash4 << 3);
    }
};

// Function to perform the mutation
ull mutat(ull num) {
    ull num2 = num;
    ull tmp = num << 6;
    num2 = (num2 ^ tmp) % 16777216;
    tmp = num2 >> 5;
    num2 = (num2 ^ tmp) % 16777216;
    tmp = num2 << 11;
    num2 = (num2 ^ tmp) % 16777216;
    return num2;
}

// Function to process numbers through mutation
vector<ull> process(int num1, int iter) {
    vector<ull> nums;
    nums.push_back((ull)num1);
    ull num = (ull)num1;
    for (int i = 0; i < iter; ++i) {
        num = mutat(num);
        nums.push_back(num);
    }
    return nums;
}

// Function to read numbers from standard input
vector<int> read_numbers_from_stdin() {
    vector<int> numbers;
    string line;
    while (getline(cin, line)) {
        try {
            numbers.push_back(stoi(line));
        } catch (const invalid_argument&) {
            cerr << "Skipping invalid input: " << line << endl;
        }
    }
    return numbers;
}

// Function to calculate differences and sequences
unordered_map<tuple<int, int, int, int>, int, TupleHash> diffy(const vector<ull>& nums) {
    vector<int> diffs;
    unordered_map<tuple<int, int, int, int>, int, TupleHash> mseq;

    for (size_t i = 1; i < nums.size(); ++i) {
        diffs.push_back((int)(nums[i] % 10) - (int)(nums[i - 1] % 10));
    }

    for (size_t i = 3; i < diffs.size(); ++i) {
        tuple<int, int, int, int> seq4 = make_tuple(diffs[i - 3], diffs[i - 2], diffs[i - 1], diffs[i]);
        int next_value = (int) (nums[i + 1] % 10);
        if (mseq.find(seq4) == mseq.end()) {
            mseq[seq4] = next_value;
        }
    }

    return mseq;
}

signed main() {
    vector<int> nums = read_numbers_from_stdin();
    int ans = 0;
    vector<vector<int>> allnums;
    unordered_set<tuple<int, int, int, int>, TupleHash> changes;
    vector<unordered_map<tuple<int, int, int, int>, int, TupleHash>> diffs;

    for (int num : nums) {
        auto curr = process(num, 2000);
        //cout << curr.back()<<" <- last num"<<endl;
        auto diff = diffy(curr);
        diffs.push_back(diff);
        for (const auto& seq4 : diff) {
            changes.insert(seq4.first);
        }
    }

    size_t j = 0;
    for (const auto& cand : changes) {
        /*cout << "Looking at sequence (" << get<0>(cand) << ", " << get<1>(cand)
             << ", " << get<2>(cand) << ", " << get<3>(cand)
             << ") (" << j << " out of " << changes.size() << ")" << endl;*/
        ++j;

        int candprice = 0;
        for (const auto& diff : diffs) {
            auto it = diff.find(cand);
            if (it != diff.end()) {
                candprice += it->second;
            }
        }

        if (candprice > ans) {
            ans = candprice;
        }
    }

    cout << ans << endl;
    return 0;
}
