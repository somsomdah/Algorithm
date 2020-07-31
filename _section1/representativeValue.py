'''
N명의 학생의 수학성적이 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
답이 2개일 경우 성적이 높은 학생의 번호를 출력하세요. 만약 답이 되는 점수가 여러 개일 경우 번호가 빠른 학생의 번호를 답으로 한다
'''

import sys

N=int(sys.stdin.readline())
scores=list(map(int,sys.stdin.readline().split()))
#average=round(sum(scores)/N) # round_half_even : 정확히 half 일 때 짝수쪽으로 근사값을 가짐
average=int(sum(scores)/N+0.5)



print(average,end=" ")

min=average+1 # 평균과의 거리의 최소값
score=-1 # 평균과 가장 가까운 점수
res=0 #학생 number
for idx,x in enumerate(scores):
     temp=abs(x-average) # 평균까지의 거리

     if temp<min:
          min=temp
          score=x # 점수
          res=idx+1
     elif temp==min:
          if x > score: #score
               score=x
               res=idx+1

print(res)

'''
average=int(sum(scores)/len(scores))
print(average,end=' ')
temp=[abs(t-average) for t in scores]

if temp[-1]==temp[-2]:
     print(scores.index(average+temp[-1])+1)
else:
     if temp[-1]+average in scores:
          print(scores.index(temp[-1]+average)+1)
     elif average-temp[-1] in scores:
                print(scores.index(average-temp[-1])+1)
'''
