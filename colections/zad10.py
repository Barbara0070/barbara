napis = "huighiguigio"
slownik={}
#for a in range(len(napis)):
for a in napis:
    slownik[a] = slownik.get(a, 0)+1
print(slownik)
from collections import defaultdict
mydict=defaultdict(int)
lakocie=defaultdict(lambda: "cukierek")