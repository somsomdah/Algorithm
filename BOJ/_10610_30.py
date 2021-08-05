<<<<<<< HEAD
import sys

inpt=sys.stdin.readline()
inpt_num=list(map(int,[n for n in inpt if n!='\n']))
inpt_num.sort(reverse=True)

num=""
for i in inpt_num:
     num+=str(i)
num=int(num)
#print(num)

if sum(inpt_num)%3==0 and num%10==0:
     print(num)
else:
     print(-1)
=======
import sys

inpt=sys.stdin.readline()
inpt_num=list(map(int,[n for n in inpt if n!='\n']))
inpt_num.sort(reverse=True)

num=""
for i in inpt_num:
     num+=str(i)
num=int(num)
#print(num)

if sum(inpt_num)%3==0 and num%10==0:
     print(num)
else:
     print(-1)
>>>>>>> 4acc6d3e3f0c7294e97481adc3209f2a884bf1ef
