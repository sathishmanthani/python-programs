#find s in missisipi

s1 = 'missisipi'

def findchar(s1,char):
    l = []
    idx=-1
    for i in range(len(s1)):
        idx = s1.find(char,idx+1,len(s1)+1)
        if idx == -1:
            break
        else:
            l.append(idx)
    return l

print(findchar(s1,'s'))
