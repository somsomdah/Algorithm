

string=input()
res=""

for c in string:
     if c.isdecimal():
          res+=c

res=int(res)


count=0

for i in range(1,res+1):
     if res%i==0:
          count+=1


print(res)
print(count)
