
a,b,v=map(int,input().split())



if v<=a:
     print(1)
else:
     if (v-b)%(a-b)==0:
          print((v-b)//(a-b))
     else:
          print((v-b)//(a-b)+1)
