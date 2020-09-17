def printDigit(num):
     if num==1:
          print(1,end="")
          return
     printDigit(num//2)
     print(num%2,end='')
     

if __name__=="__main__":
     printDigit(int(input()))
