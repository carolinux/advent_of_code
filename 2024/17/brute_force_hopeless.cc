#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <stdexcept>
#include <cmath>
using namespace std;



map<string, unsigned long long> registers;
vector<unsigned long long> program;


// Function to parse input
void parse_input(const string &input_text) {
    istringstream input_stream(input_text);
    string line;

    while (getline(input_stream, line)) {
        if (line.find("Register") == 0) {
            auto colon_pos = line.find(":");
            string register_name = line.substr(9, colon_pos - 9); // Extract Register name
            unsigned long long value = stoi(line.substr(colon_pos + 1)); // Extract value
            registers[register_name] = value;
        } else if (line.find("Program") == 0) {
            auto colon_pos = line.find(":");
            string program_str = line.substr(colon_pos + 1);
            istringstream program_stream(program_str);
            string num;
            while (getline(program_stream, num, ',')) {
                program.push_back(stoi(num));
            }
        }
    }
}

// Function to parse second operand
unsigned long long parse_2nd_operand(unsigned long long ix) {
    if (ix == 7) {
        throw runtime_error("something went wrong");
    } else if (ix <= 3) {
        return ix;
    } else if (ix == 4) {
        return registers["A"];
    } else if (ix == 5) {
        return registers["B"];
    } else if (ix == 6) {
        return registers["C"];
    }
    return 0;
}

vector<unsigned long long> compute(vector<unsigned long long> &program , map<string, unsigned long long> &registers) {
    vector<unsigned long long> out;
    size_t i = 0;
    while (i < program.size()) {
        unsigned long long op = program[i];
        unsigned long long operand = program[i + 1];

        switch (op) {
            case 0: {
                unsigned long long val = registers["A"];
                unsigned long long pow = parse_2nd_operand(operand);
                registers["A"] = val / (1 << pow);
                break;
            }
            case 1: {
                unsigned long long val = registers["B"];
                unsigned long long val2 = operand;
                registers["B"] = val ^ val2;
                break;
            }
            case 2: {
                unsigned long long val = parse_2nd_operand(operand) % 8;
                registers["B"] = val;
                break;
            }
            case 3: {
                if (registers["A"] == 0) {
                    i += 2;
                    continue;
                } else {
                    i = operand;
                    continue;
                }
            }
            case 4: {
                registers["B"] = registers["B"] ^ registers["C"];
                break;
            }
            case 5: {
                unsigned long long val = parse_2nd_operand(operand) % 8;
                if (val != program[out.size()]) {
                    return vector<unsigned long long>();
                    }
                out.push_back(val);
                break;
            }
            case 6: {
                unsigned long long val = registers["A"];
                unsigned long long pow = parse_2nd_operand(operand);
                registers["B"] = val / (1 << pow);
                break;
            }
            case 7: {
                unsigned long long val = registers["A"];
                unsigned long long pow = parse_2nd_operand(operand);
                registers["C"] = val / (1 << pow);
                break;
            }
        }
        i += 2;
    }
    return out;

}


signed main() {
    // Read input
    string input_text;
    string line;
    while (getline(cin, line)) {
        input_text += line + "\n";
    }

    parse_input(input_text);

    cout << "Initial Registers:\n";
    unsigned long long lim1 = 1ULL<<46;
    unsigned long long lim2 = 1ULL<<47;
    for (const auto &reg : registers) {
        cout << reg.first << ": " << reg.second << "\n";
    }
    unsigned long long a = registers["A"];
    unsigned long long b = 0;
    unsigned long long c = 0;
    for (unsigned long long i = lim1; i < lim2; ++i) {

    bool good = true;
    int j = 0;

    while(1) {

        b = a & 7;
        //cout<<"bbb:"<< b <<" "<<a<<endl;
        b ^=6;
        c = a >>b;
        b = b ^c ^ 4;
        b = b&7;
        if (b != program[j]) {
            good = false;
            break;
         }

        if (a==0) {
            break;
        }
        a = a >> 3;
        j++;
        }

    }



    return 0;
}
