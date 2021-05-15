# def add(parm1, param2):
#     return parm1 + param2
#
# #result = add(1,2)
#
# #print(result)
#
#
# def divide(a,b):
#     if b == 0:
#         return "Nie może być zero!😇"
#
#     return  a / b
# result = divide(15,5)
# print(result)


l = [1, 2, 3]
l2 = []

for item in l:
    if item * 3 % 2 == 0:
        l2.append(item * 3)
    print(item)

