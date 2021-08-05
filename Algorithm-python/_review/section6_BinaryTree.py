def prefix(v):
     if v>7:
          return
     else:
          print(v, end=" ")
          prefix(2*v)
          prefix(2*v+1)


def infix(v):
     if v>7:
          return
     else:
          infix(2*v)
          print(v, end=" ")
          infix(2*v+1)

def postfix(v):
     if v>7:
          return
     else:
          postfix(2*v)
          postfix(2*v+1)
          print(v, end=" ")


if __name__=="__main__":
     prefix(1)
     print()
     infix(1)
     print()
     postfix(1)
