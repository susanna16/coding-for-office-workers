#list-대괄호사용/수정가능
print("list")
print([1,2,3])
print(type([1,2,3]))
list_a=[1,2,3]
print(list_a)
print(list_a[0])

#slice-인덱스를 0에서부터 2전까지 잘라서 출력
print("slice")
print(list_a[0:2])

#a.clear
# print("a.clear")
# list_a.clear()
# print(list_a)

#a.remove
print("a.remove")
list_a.remove(2)
print(list_a)

#a.append-리스트에 새로운 항목을 추가해준다
print("a.append")
list_a.append(4)
print(list_a)

#duple-소괄호사용/수정불가
print("tuple")
print((1,2,3))
print(type((1,2,3)))
