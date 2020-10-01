# Get the uncommon words between the given 2 sentenses
s1 = 'Python is an interpreted, high-level and general-purpose programming language'
s2 = 'Python is Created by Guido van Rossum and first released in 1991'

print(set(s1.split()).symmetric_difference(s2.split()))

# Remember that Symmetric_difference is a function of a Set and accepts any iterable. So its not necessary to convert the second list to Set.

# you can also write it like below
a = set(s1.split())
b = set(s2.split())

print((a-b).union(b-a))

