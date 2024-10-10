def sol(a, b):
    return a != b and abs(len(a) - len(b)) <= 1 and 2 > ((sum([1 if a[i] != b[i] else 0 for i in range(len(a)-1)]) + 1) if len(a) - len(b) else ((sum([1 if a[i] != b[i] else 0 for i in range(len(b) - 1)]) + 1) if len(b) > len(a) else sum([1 if a[i] != b[i] else 0 for i in range(len(a) - 1)])) )


print(sol("cat", "cats"))
print(sol("cats", "cat"))
print(sol("cat", "cut"))
print(sol("cat", "dog"))
print()
print(sol("abcde", "abcde"))
print(sol("abcde", "abcdef"))
print(sol("abcde", "abcdefg"))
print(sol("abcde", "abcdf"))
print(sol("abcde", "abcd"))
print(sol("abcde", "abc"))
