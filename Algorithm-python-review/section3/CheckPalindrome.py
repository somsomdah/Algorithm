n=int(input())

def reverse_string(string):
     string_list=[c for c in string]
     string_list.reverse()
     res=""
     for c in string_list:
          res+=c
     return res


for i in range(1,n+1):
     string=input().lower()
     if string==reverse_string(string):
          print('#{} YES'.format(i))
     else:
          print('#{} NO'.format(i))
