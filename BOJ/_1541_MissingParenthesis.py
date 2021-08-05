<<<<<<< HEAD
import sys

e0=sys.stdin.readline().split('\n')
e1=e0[0].split('-')

e2=[]
for e in e1:
     e2.append(e.split('+'))

e3=[]
for e in e2:
     e=list(map(int,e))
     e=sum(e)
     e3.append(e)

print(e3[0]-sum(e3[1:]))
=======
import sys

e0=sys.stdin.readline().split('\n')
e1=e0[0].split('-')

e2=[]
for e in e1:
     e2.append(e.split('+'))

e3=[]
for e in e2:
     e=list(map(int,e))
     e=sum(e)
     e3.append(e)

print(e3[0]-sum(e3[1:]))
>>>>>>> 4acc6d3e3f0c7294e97481adc3209f2a884bf1ef
