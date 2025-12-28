#include <bits/stdc++.h>
#include <bitset>
#include <map>
using namespace std;


// up to 10 slots of {0, 255} values so 10 x 8 bit = 80
// and then up to say 16 moves -> 4 more bits
// so we store the 8 slots in one uint  = 64 bits
// the last 2 slots + 4 bits in another uint = 20 bits
// total = 84

const int N = 84;

struct BitsetCompare {
    bool operator()(const bitset<N>& a, const bitset<N>& b) const {
        for (int i = N-1; i >= 0; i--) {
            if (a[i] != b[i]) return a[i] < b[i];
        }
        return false;
    }
};

struct Machine {
    vector<vector<int>> buttons;
    vector<int> targetJolts;
    int maxIter;
};

vector<vector<int>> getSortedButtons(Machine &m) {
    vector<int> res1;
    map<int, int> freq;
    for (auto &button: m.buttons) {
        for (int val : button) {
                freq[val]++;
            }
    }
    // sort by frequency, break ties by target joltage in m.targetJolts
    vector<pair<int, int>> freqVec(freq.begin(), freq.end());
    sort(freqVec.begin(), freqVec.end(), [&](const pair<int, int> &a, const pair<int, int> &b) {
        if (a.second != b.second) {
            return a.second < b.second; // lower frequency first
        } else {
            return m.targetJolts[a.first] < m.targetJolts[b.first]; // lower value first;
        }
    });

    for (auto &p : freqVec) {
        res1.push_back(p.first);
    }

    // print the frequency sorted buttons
    cout << "Frequency sorted buttons: ";
    for (int btn : res1) {
        cout << btn << " (freq: " << freq[btn] << "), ";
    }

    // Create priority map: button index -> priority (lower is higher priority)
    map<int, int> priority;
    for (int i = 0; i < res1.size(); i++) {
        priority[res1[i]] = i;
    }

    // Sort operations by minimum priority of buttons they affect
    vector<vector<int>> res = m.buttons;
    sort(res.begin(), res.end(), [&](const vector<int> &a, const vector<int> &b) {
        int minPriorityA = INT_MAX;
        for (int btn : a) {
            if (priority.count(btn)) {
                minPriorityA = min(minPriorityA, priority[btn]);
            }
        }

        int minPriorityB = INT_MAX;
        for (int btn : b) {
            if (priority.count(btn)) {
                minPriorityB = min(minPriorityB, priority[btn]);
            }
        }

        return minPriorityA < minPriorityB;
    });

    return res;
}


/*unsigned long long getBitsInRange(const bitset<N>& b, int start, int end) {
  bitset<N> temp = b >> start;  // Shift so start is at position 0
  int len = end - start;
  unsigned long long mask = (1ULL << len) - 1;  // Create mask of 'len' ones
  return temp.to_ullong() & mask;
}*/

int getCount(const bitset<N>& b, int i) {
    int val = 0;
    int start = i * 8;
    for (int j = 0; j < 8; j++) {
        val |= (b[start + j] << j);
    }
    return val;
}

int getButtonIndex(const bitset<N>& b) {
    int val = 0;
    for (int j = 0; j < 4; j++) {
        val |= (b[80 + j] << j);
    }
    return val;
}

bool done(const bitset<N> &b, Machine &m) {

    for (int i=0;i<m.targetJolts.size();i++) {
        auto cnt1 = getCount(b, i);
        if (cnt1 != m.targetJolts[i]) {
            return false;
        }
    }
    return true;
}


bitset<N> getStateKey(int buttonIdx, vector<int> &values) {

    bitset<N> b;
    long unsigned int part1 = 0;
    unsigned int part2 = 0;

    unsigned int elem9 = 0;
    unsigned int elem10 = 0;

    for (int i =0;i< values.size();i++) {
        if (i == 8) {
            elem9 = values[i];
            continue;
        }
        if (i == 9) {
            elem10 = values[i];
            continue;
        }
        part1 |= ((unsigned long long)values[i] << (i * 8));
    }

    part2 = (buttonIdx<<16) | (elem10 << 8) | elem9;

    bitset<N> p1(part1);
    bitset<N> p2(part2);

    b = (p2 << 64) | p1;
    return b;
}

vector<int> parseVector(const string &s, char open, char close) {
    vector<int> result;
    string content = s;
    content.erase(remove(content.begin(), content.end(), open), content.end());
    content.erase(remove(content.begin(), content.end(), close), content.end());
    stringstream ss(content);
    string num;
    while (getline(ss, num, ',')) {
        if (!num.empty()) result.push_back(stoi(num));
    }
    return result;
}



/*
    @ft.lru_cache(maxsize=15000000)
    def recur(i, curr):
        #print(f"{curr} vs {target}")
        if curr == target:
            return 0
        if i >= len(togs):
            return math.inf
        minans = math.inf
        for j in range(iters):
            new_state, cont = apply(curr, i, togs, last, target, j)
            if cont is False:
                break
            if new_state is None:
                continue
            cand = recur(i+1, new_state) + j
            minans = min(cand, minans)

        return minans

    return recur(0, start)
*/

vector<int> getLastOpForButton(Machine &m) {
    vector<int> lastOp(m.targetJolts.size(), -1);
    for (int opIdx = m.buttons.size() - 1; opIdx >= 0; opIdx--) {
        for (int btn : m.buttons[opIdx]) {
            if (lastOp[btn] == -1) {
                lastOp[btn] = opIdx;
            }
        }
    }
    return lastOp;
}

tuple<bitset<N>, bool, bool> tryy(Machine &m, const bitset<N> &b, const vector<int> &button, int times, int currentOpIdx, const vector<int>& lastOpForButton) {
    vector<int> currCounts;
    for (int i=0;i<m.targetJolts.size();i++) {
        currCounts.push_back(getCount(b, i));
    }

    for (int j=0;j<button.size();j++) {
        int i = button[j];
        currCounts[i] += times;
        if (currCounts[i] > m.targetJolts[i]) {
            return {bitset<N>(), false, false};  // exceeded, break
        }
    }

    // Check if this is last op for any button and we haven't reached target
    for (int i = 0; i < m.targetJolts.size(); i++) {
        if (currCounts[i] < m.targetJolts[i] && lastOpForButton[i] == currentOpIdx) {
            return {bitset<N>(), false, true};  // too low, continue
        }
    }

    bitset<N> new_b = getStateKey(getButtonIndex(b)+1, currCounts);
    return {new_b, true, true};  // valid, continue
}

int recur(Machine &m, bitset<N> &b, map<bitset<N>, int, BitsetCompare> & ma, const vector<int>& lastOpForButton) {

    // if we have seen this state before
    if (ma.find(b) != ma.end()) {
        return ma[b];
    }

    if (done(b, m)) {
        return 0;
    }
    int buttonIdx = getButtonIndex(b);
    if (buttonIdx >= m.buttons.size()) {
        return 1e9;
    }
    int mincand = 1e9;

    for (int i=0;i<=m.maxIter;i++) {
        // try to apply buttonOrder[buttonIdx],  i times
        auto [new_b, valid, cont] = tryy(m, b, m.buttons[buttonIdx], i, buttonIdx, lastOpForButton);
        if (!cont) {
            break;
        }
        if (!valid) {
            continue;
        }
        int cand = recur(m, new_b, ma, lastOpForButton) + i;
        mincand = min(mincand, cand);

    }

    ma[b] = mincand;
    return mincand;


}


int solve(Machine &m) {

    map<bitset<N>, int, BitsetCompare> seen;
    vector<int> lastOpForButton = getLastOpForButton(m);

    bitset<N> b;
    return recur(m, b, seen, lastOpForButton);
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string line;
    vector<Machine> machines;

    while (getline(cin, line)) {
        if (line.empty()) continue;
        Machine m;
        stringstream ss(line);
        string token;

        // Ignore the first token (diagram) which starts with [
        ss >> token;

        // Read button schematics until we reach the target set {..}
        while (ss >> token) {
            if (token[0] == '{') break; // reached target joltage set
            m.buttons.push_back(parseVector(token, '(', ')'));
        }

        // The last token is the target joltage set
        m.targetJolts = parseVector(token, '{', '}');
        m.maxIter = *max_element(m.targetJolts.begin(), m.targetJolts.end());

        machines.push_back(m);
    }

    int ans = 0;
    // Print parsed data for verification
    for (int i = 0; i < machines.size(); i++) {
        /*cout << "Machine " << i+1 << ":\n";
        cout << " Buttons:\n";
        for (auto &b : machines[i].buttons) {
            for (int x : b) cout << x << " ";
            cout << "\n";
        }
        cout << " Target Jolts: ";
        for (int x : machines[i].targetJolts) cout << x << " ";
        cout << " \nLeast Frequent Buttons: ";*/

        vector<vector<int>> freqButtons = getSortedButtons(machines[i]);
        machines[i].buttons = freqButtons;

        cout << "Machine " << i+1 << " buttons:\n";
        for (auto& btn : machines[i].buttons) {
            cout << "  [";
            for (int j = 0; j < btn.size(); j++) {
                cout << btn[j];
                if (j < btn.size() - 1) cout << ", ";
            }
            cout << "]\n";
        }
        cout << flush;

        int count = solve(machines[i]);
        ans+= count;
        cout<<"Count for case "<<i+1<<" = "<<count << "\n" << flush;



        //cout << "\n\n";
    }
    cout << ans << "\n";
    return 0;
}

