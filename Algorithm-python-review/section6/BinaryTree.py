def prefix(v):
     if v<=7:
          print(v,end=" ")
          prefix(2*v)
          prefix(2*v+1)


def infix(v):
     if v<=7:
          infix(2*v)
          print(v,end=" ")
          infix(2*v+1)

def postfix(v):
     if v<=7:
          postfix(2*v)
          postfix(2*v+1)
          print(v,end=" ")



prefix(1)
print()
infix(1)
print()
postfix(1)
