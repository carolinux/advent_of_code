#include <bits/stdc++.h>
#include <bitset>
#include <map>
#include <chrono>
using namespace std;
using namespace chrono;


// Optimized State: Direct array access (like Python tuple!)
// - values[10]: 10 bytes (each value 0-255)
// - buttonIdx: 1 byte
// Total: 11 bytes (vs 16 bytes with bit-packing!)

struct State {
    uint8_t values[10];  // Values 0-9
    uint8_t buttonIdx;   // Current button index

    bool operator==(const State& o) const {
        return buttonIdx == o.buttonIdx &&
               memcmp(values, o.values, 10) == 0;
    }
};

struct StateHash {
    size_t operator()(const State& s) const {
        // Better hash than simple XOR - like Python/Java
        size_t h = s.buttonIdx;
        for (int i = 0; i < 10; i++) {
            h = h * 31 + s.values[i];
        }
        return h;
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


// FAST: Direct array access (no bit operations!)
int getCount(const State& s, int i) {
    return s.values[i];
}

// FAST: Direct field access (no bit operations!)
int getButtonIndex(const State& s) {
    return s.buttonIdx;
}

bool done(const State& s, Machine &m) {
    for (int i=0;i<m.targetJolts.size();i++) {
        if (s.values[i] != m.targetJolts[i]) {
            return false;
        }
    }
    return true;
}


// FAST: Direct assignment (no bit packing!)
State getStateKey(int buttonIdx, vector<int> &values) {
    State s;
    s.buttonIdx = buttonIdx;
    for (int i = 0; i < 10 && i < values.size(); i++) {
        s.values[i] = values[i];
    }
    // Zero remaining if values.size() < 10
    for (int i = values.size(); i < 10; i++) {
        s.values[i] = 0;
    }
    return s;
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
    int currCounts[10] = {};  // Stack-allocated, zero-initialized
    for (int i=0;i<m.targetJolts.size();i++) {
        currCounts[i] = s.values[i];  // Direct assignment
    }

    for (int j=0;j<button.size();j++) {
        int i = button[j];
        currCounts[i] += times;
        if (currCounts[i] > m.targetJolts[i]) {
            return {State{}, false, false};  // exceeded, break
        }
    }

    // Check if this is last op for any button and we haven't reached target
    for (int i = 0; i < m.targetJolts.size(); i++) {
        if (currCounts[i] < m.targetJolts[i] && lastOpForButton[i] == currentOpIdx) {
            return {State{}, false, true};  // too low, continue
        }
    }

    // Create state directly from array (no vector allocation!)
    State new_s = {};
    new_s.buttonIdx = s.buttonIdx + 1;
    for (int i = 0; i < m.targetJolts.size(); i++) {
        new_s.values[i] = currCounts[i];
    }
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
    int buttonIdx = s.buttonIdx;  // Direct access!
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
    // NOTE: Don't reserve! Causes OOM due to rehashing memory spikes.
    // The bit-packed version worked without reserve, so we don't use it here either.

    vector<int> lastOpForButton = getLastOpForButton(m);

    State s = {};  // Initial state: all zeros
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
