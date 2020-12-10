#Calculate the average word length.
#For the given set of words return the average word length.  

s1 = 'Python is an interpreted programming language'
s2 = 'hello world'

def avgWordLength(s1):
    return round(len(''.join(s1.split()))/len(s1.split()),2)

print(avgWordLength(s1))
print(avgWordLength(s2))
