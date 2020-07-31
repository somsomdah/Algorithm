'''
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다
'''
import sys
'''
# 입력을 받음
N,M=map(int,sys.stdin.readline().split())

#두 정다면체의 눈의 값을 합한 결과의 리스트 (중복 허용)
sum=[i+j for i in range(1,N+1) for j in range(1,M+1)]

# 최대 빈도를 찾기 위한 과정
temp=sorted([sum.count(i) for i in sum])
count=list(set(temp))
max=max(count)

# 최대 빈도와 count가 같으면 res에 들어감 (중복 허용)
res=sorted([i for i in sum if sum.count(i)==max])

for i in set(res): #중복 비허용 해서 최대 빈도의 합을 출력
     print(i,end=" ")
     
'''
N,M=map(int,sys.stdin.readline().split())

count=[0]*(N+M+1) # index==sum count

for i in range(1,N+1):
     for j in range(1,M+1):
         count[i+j]+=1

max=max(count)

for i in range(N+M+1):
     if count[i]==max:
          print(i,end=" ")
