## Flatten a dictionary 

d = {'a':{'a1':100}, 'b':{'b1':{'c1':200}}}

def flatten(d,l=[]):
    for k, v in d.items():
        l.append(k)
        print(k,v)
        if type(v)==dict:
            flatten(v,l)
        else:
            l.append(v)
    return l
print(flatten(d))
