def danila_vot_vam_solution(a, b):
    return False if abs(len(a) - len(b)) > 1 else 2 > ((sum([1 if a[i] != b[i] else 0 for i in range(len(a)-1)]) + 1) if len(a) - len(b) else ((sum([1 if a[i] != b[i] else 0 for i in range(len(b) - 1)]) + 1) if len(b) > len(a) else sum([1 if a[i] != b[i] else 0 for i in range(len(a) - 1)])) )
    # if abs(len(a) - len(b)) > 1:
    #     return False
    # if len(a) > len(b):
    #     # c = 1
    #     # for i in range(len(a) - 1):
    #     #     if a[i] != b[i]:
    #     #         c += 1
    #     c = sum([1 if a[i] != b[i] else 0 for i in range(len(a)-1)]) + 1
    # elif len(b) > len(a):
    #     # c = 1
    #     # for i in range(len(b) - 1):
    #     #     if a[i] != b[i]:
    #     #         c += 1
    #     c = sum([1 if a[i] != b[i] else 0 for i in range(len(b) - 1)]) + 1
    # else:
    #     # c = 0
    #     # for i in range(len(a)):
    #     #     if a[i] != b[i]:
    #     #         c += 1
    #     c = sum([1 if a[i] != b[i] else 0 for i in range(len(a) - 1)])
    # return c < 2


print(danila_vot_vam_solution("cat", "cats"))
print(danila_vot_vam_solution("cats", "cat"))
print(danila_vot_vam_solution("cat", "cut"))
print(danila_vot_vam_solution("cat", "dog"))
