'''
소수(에라토스테네스 체)
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다. 제한시간은 1초입니다. 
'''

import sys

N=int(sys.stdin.readline())


'''
# fail
def prime_num(num_list,num,max_num):
     if num>=max_num:
          print(len(num_list))
          return;
     for i in num_list:
          if num%i==0:
               prime_num(num_list,num+1,max_num)
               break;
     else:
          num_list.append(num)
          prime_num(num_list,num+1,max_num)

          

prime_num([2],2,N)
'''
