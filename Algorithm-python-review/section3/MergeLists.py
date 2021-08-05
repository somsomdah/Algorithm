n=int(input())
list1=list(map(int,input().split()))
m=int(input())
list2=list(map(int,input().split()))

result=[]

while True:
    a=list1[0]
    b=list2[0]

    if a<b:
        result.append(a)
        list1.pop(0)
        if not list1:
            break
    else:
        result.append(b)
        list2.pop(0)
        if not list2:
            break


if list1:
    result.extend(list1)
else:
    result.extend(list2)


for r in result:
    print (r,end=" ")
