# Get the Nth highest value from key 

d = {'A':100, 'B':300, 'C':99, 'D':1, 'E':3455}

def nhigh(d,n):
    """Return n th highest value from given dictionary
    """
    sorted_list = sorted(d.items(),key=lambda x:x[1],reverse=True)
    return sorted_list[n-1][0]

# Get name with 2nd highest value

print(nhigh(d,1))
