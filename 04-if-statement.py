#참과 거짓 boolean
#if
#True, False
#and, or, not

# a=True
# b=False
#
# #A가 참이거나 혹은 B가 참이라면(A나 B중에서 하나라도 참이면 된다)
# print(a or b)
# #A가 참이고 그리고 B가 참이되면(A와 B가 둘다 참이여야 된다)
# print(a and b)

# a=True
# print(a == True)
# print(a is True)

d=7
if d>10:
     print("숫자는 5보다 큽니다.")
elif d>5 and d<=10:
    print("숫자는 10보다 작거나 같고, 5보다는 큽니다.")
else:
    print("숫자는 5보다 작거나 같습니다.")
