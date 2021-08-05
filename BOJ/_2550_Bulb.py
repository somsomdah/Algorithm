import sys

n=int(sys.stdin.readline())
in1=list(map(int,sys.stdin.readline().split()))
in2=list(map(int,sys.stdin.readline().split()))


# 수열 만들기
seq=[]
for i in range(n):
     seq.append(in2.index(in1[i]))

print(seq)

# 최장부분증가수열 찾기 (이분탐색 이용)

def binarySearch(seq,s,e,k): # 탑색 범위 : [s,e), s,e는 수열의 인덱스,
                                   # k는 수열에서 그 위치를 탐색하고자 하는 원소
                                   # return 값은 k의 위치                                   
     if s==e: # 더이상 탐색할 게 없음
          return s
     
     m=(s+e)//2 # 중간 인덱스
     if seq[m]<k: # k가 수열의 중간에 있는 값보다 크면
          return binarySearch(seq,m+1,e,k) # 오른쪽 탐색
     elif seq[m]>k: # k가 수열의 중간에 있는 값보다 작으면
          return binarySearch(seq,s,m,k) # 왼쪽 탐색
     else: # if seq[m]==key
          return m

LIS=[-1]*(n+1)
for i in range(n):
     p=binarySearch(seq,0,n,seq[i]) #seq[i]의 위치
     print(p,end="")
     
print(LIS)
     
