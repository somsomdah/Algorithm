'''
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)
이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.
'''
import sys

n=int(sys.stdin.readline())


def  isPalindrome(string):
     for i in range(len(string)-1):          
          if string[i]!=string[-i-2]:
               return "NO"
     else:
          return "YES"
     
        
for i in range(n):
     string=sys.stdin.readline()
     string=string.lower()
     print("#"+str(i+1)+" "+isPalindrome(string))

'''
# string 끝에 공백때문에 작동하지 않음
for i in range(n):
     string=sys.stdin.readline().lower()
     if string==string[::-1]:
          print("#"+str(i+1)+" Yes")
     else:
          print("#"+str(i+1)+"NO")
'''


     
