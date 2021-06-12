
# List of friends is given like below. A is friend of B. B is friend of D. etc.,
# Calculate the Count of Friend each person has in descending order.

l = [['A','B'], ['B','D'],['E'],['F','A'],['A','X','Y','D']]

import collections

d = collections.defaultdict(list)

for item in l:
    if len(item)==1:
        d[item[0]]
    else:
        for i in range(len(item)):
            for j in range(i):
                if i != j:
                    d[item[i]].append(item[j])
                    d[item[j]].append(item[i])

frenz_cnt = {k:len(v) for k,v in sorted(d.items(), key=lambda x:x[1], reverse=True)}
            

[print(k,' has ','no' if v==0 else v,'friends') for k,v in frenz_cnt.items()]


## Output ####

"""
Sathish Manthani ran 24 lines of Python 3 (finished in 754ms):

A  has  5 friends
D  has  4 friends
X  has  3 friends
Y  has  3 friends
B  has  2 friends
F  has  1 friends
E  has  no friends
"""
