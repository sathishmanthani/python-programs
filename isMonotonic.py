#Given an array of integers, we would like to determine whether the array is monotonic (non-decreasing/non-increasing) or not.
#Examples:
#// 1 2 5 5 8 --> true
#// 9 4 4 2 2 --> true
#// 1 4 6 3 -->  false


a = [1, 2, 5, 5, 8]
b = [9, 4, 4, 2, 2]
c = [1, 4, 6, 3]
def is_monotonic(ln):
    return sorted(ln)==ln or sorted(ln,reverse=True)==ln

print(is_monotonic(a))
print(is_monotonic(b))
print(is_monotonic(c))
