t=int(input())

for i in range(1,t+1):
     n,s,e,k=map(int,input().split())
     nums=list(map(int,input().split()))
     new_nums=nums[s-1:e]
     new_nums.sort()
     print("#{} {}".format(i,new_nums[k-1]))
