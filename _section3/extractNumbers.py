'''
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만
듭니다. 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이
됩니다. 즉 첫 자리 0은 자연수화 할 때 무시합니다. 출력은 120를 출력하고, 다음 줄에 120
의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.
'''

import sys

string=sys.stdin.readline()

resnum=0
for c in string:
     if c.isdecimal():
          resnum=resnum*10+int(c)
print(resnum)

count=0
for i in range(2,resnum//2+1):
     if resnum%i==0:
          count+=1
print(count+2) # 1과 자기자신

'''
strnum=[0,1,2,3,4,5,6,7,8,9]
strnum=list(map(str,strnum))

resnum=""
for c in string:
     if c in strnum:         # if c.isdigit() or isdecimal()
          resnum+=c       #res=res*10+c ### 중요

resnum=int(resnum)
print(resnum)
'''

