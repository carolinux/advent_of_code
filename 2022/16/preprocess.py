import re

num = 0
with open('small.txt','r') as f:
    for line in f:
        #print(line)
        parts = line.split(";")
        first = parts[0]
        sec= parts[1]
        res = re.search("Valve (.*) has flow rate=(\d*)", first)
        valve = res.group(1)
        rate = res.group(2)
        res = re.search("tunnel(s*) lead(s*) to valve(s*) (.*)", sec)
        valvestr = res.group(4)
        valves = [v.strip() for v in valvestr.split(",")]
        
        line1 = f"{valve} {rate} {len(valves)}"
        line2 = " ".join(valves)
        print(line1)
        print(line2)
        num+=1

#print(num)


