n=int(input())

a=[]
for i in range(n):
     age,name=input().split()
     age=int(age)
     a.append((i,age,name))


a.sort(key=lambda x:(x[1],x[0]))

for p in a:
     print(p[1],p[2])
