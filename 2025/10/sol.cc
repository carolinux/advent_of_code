#include <bits/stdc++.h>
#include <bitset>
#include <map>
#include <chrono>
using namespace std;
using namespace chrono;


// up to 10 slots of {0, 255} values so 10 x 8 bit = 80
// and then up to say 16 moves -> 4 more bits
// so we store the 8 slots in one uint  = 64 bits
// the last 2 slots + 4 bits in another uint = 20 bits
// total = 84

const int N = 84;

// State: pair<uint64_t, uint32_t>
// - first (64 bits): values[0-7], 8 bits each
// - second (32 bits): values[8-9] (16 bits) + buttonIdx (4 bits)
using State = pair<uint64_t, uint32_t>;

struct StateHash {
    size_t operator()(const State& s) const {
        return s.first ^ ((size_t)s.second << 32);
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

int getCount(const State& s, int i) {
    if (i < 8) {
        // Extract from first 64 bits
        return (s.first >> (i * 8)) & 0xFF;
    } else if (i == 8) {
        // Extract from second, bits 0-7
        return s.second & 0xFF;
    } else if (i == 9) {
        // Extract from second, bits 8-15
        return (s.second >> 8) & 0xFF;
    }
    return 0;
}

int getButtonIndex(const State& s) {
    // Extract from second, bits 16-19
    return (s.second >> 16) & 0xF;
}

bool done(const State& s, Machine &m) {
    for (int i=0;i<m.targetJolts.size();i++) {
        auto cnt1 = getCount(s, i);
        if (cnt1 != m.targetJolts[i]) {
            return false;
        }
    }
    return true;
}


State getStateKey(int buttonIdx, vector<int> &values) {
    uint64_t part1 = 0;
    uint32_t part2 = 0;

    // Pack first 8 values into part1 (64 bits)
    for (int i = 0; i < 8 && i < values.size(); i++) {
        part1 |= ((uint64_t)values[i] << (i * 8));
    }

    // Pack values[8], values[9], and buttonIdx into part2 (32 bits)
    uint32_t elem8 = (values.size() > 8) ? values[8] : 0;
    uint32_t elem9 = (values.size() > 9) ? values[9] : 0;
    part2 = (buttonIdx << 16) | (elem9 << 8) | elem8;

    return {part1, part2};
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

tuple<State, bool, bool> tryy(Machine &m, const State &s, const vector<int> &button, int times, int currentOpIdx, const vector<int>& lastOpForButton) {
    vector<int> currCounts;
    for (int i=0;i<m.targetJolts.size();i++) {
        currCounts.push_back(getCount(s, i));
    }

    for (int j=0;j<button.size();j++) {
        int i = button[j];
        currCounts[i] += times;
        if (currCounts[i] > m.targetJolts[i]) {
            return {State(), false, false};  // exceeded, break
        }
    }

    // Check if this is last op for any button and we haven't reached target
    for (int i = 0; i < m.targetJolts.size(); i++) {
        if (currCounts[i] < m.targetJolts[i] && lastOpForButton[i] == currentOpIdx) {
            return {State(), false, true};  // too low, continue
        }
    }

    State new_s = getStateKey(getButtonIndex(s)+1, currCounts);
    return {new_s, true, true};  // valid, continue
}

int recur(Machine &m, State &s, unordered_map<State, int, StateHash> & ma, const vector<int>& lastOpForButton) {

    // if we have seen this state before
    if (ma.find(s) != ma.end()) {
        return ma[s];
    }

    if (done(s, m)) {
        return 0;
    }
    int buttonIdx = getButtonIndex(s);
    if (buttonIdx >= m.buttons.size()) {
        return 1e9;
    }
    int mincand = 1e9;

    for (int i=0;i<=m.maxIter;i++) {
        // try to apply buttonOrder[buttonIdx],  i times
        auto [new_s, valid, cont] = tryy(m, s, m.buttons[buttonIdx], i, buttonIdx, lastOpForButton);
        if (!cont) {
            break;
        }
        if (!valid) {
            continue;
        }
        int cand = recur(m, new_s, ma, lastOpForButton) + i;
        mincand = min(mincand, cand);

    }

    ma[s] = mincand;
    return mincand;


}


int solve(Machine &m) {

    unordered_map<State, int, StateHash> seen;
    vector<int> lastOpForButton = getLastOpForButton(m);

    State s = {0, 0};  // Initial state: all zeros
    return recur(m, s, seen, lastOpForButton);
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

        auto start = high_resolution_clock::now();
        int count = solve(machines[i]);
        auto end = high_resolution_clock::now();
        auto duration = duration_cast<milliseconds>(end - start).count();

        ans+= count;
        cout<<"Count for case "<<i+1<<" = "<<count << " (took " << duration << " ms)\n" << flush;



        //cout << "\n\n";
    }
    cout << ans << "\n";
    return 0;
}

