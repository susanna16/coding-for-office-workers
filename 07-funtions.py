#함수 functions
    # 공통된 작업을 묶어서 하나로 만듬.
    # definition의 약자로 def를 사용
    # 수정에 용이
#입력값 parameters, 반환값 return
    #여기 예시에서 입력값은 있으나 반환값은 없다

def hello_friends(name):
    print("hi, {}".format(name))

name1="sujin"
name2="jane"
name3="john"
name4="tom"
name5="sujin"
name6="jane"
name7="john"
name8="tom"
# print("hello, {}".format(name1))
# print("hello, {}".format(name2))
# print("hello, {}".format(name3))
# print("hello, {}".format(name4))
# print("hello, {}".format(name5))
# print("hello, {}".format(name6))
# print("hello, {}".format(name7))
# print("hello, {}".format(name8))

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)

#네가지 경우의 수가 존재
    #1)입력값 o, 반환값 o
def sum(a, b):
    return a + b

    #2)입력값 o, 반환값 x
def hello_friends(name):
    print("hello, {}".format(name))

    #3)입력값 x, 반환값 o
def return_1():
    return 1

    #4)입력값 x, 반환값 x
def hello_world():
    print("hello world")

#반환값이 있다는 것은 return이 있다는 것
#return은 변수에 담아서 쓸 수 있다(예시3에 해당)
num_1=return_1()
print(num_1)

#점프투파이썬 04-1참고
