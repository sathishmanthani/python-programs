# Fill the None values in a list with its previous value

l = [1,None,2,None,56,678,6,7,None]

def fillNulls(l):
    for i in range(len(l)):
        if not l:
            return None
        elif not l[i]:
            l[i]=l[i-1]
    return l

print(fillNulls(l))
