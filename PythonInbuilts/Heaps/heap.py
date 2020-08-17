import heapq
from collections import defaultdict
s = "tree"
d = defaultdict(int)
for c in s:
    d[c] += 1
h = []
for k,v in d.items():
    heapq.heappush(h,(-1*v, k))
res = ""
while len(h):
    t = heapq.heappop(h)
    ct = -1*t[0]
    while ct:
        res += t[1]
        ct -= 1

print(res)