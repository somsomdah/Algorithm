
n,k=map(int,input().split())
#print(n,k)

nums=list(map(int,input().split()))
nums.sort()

res=[]

for i in range(n):
     for j in range(i+1,n):
          for k2 in range(j+1,n):
               res.append(nums[i]+nums[j]+nums[k2])


res=list(set(res))
res.sort(reverse=True)

print(res[k-1])
