import sys

n=int(sys.stdin.readline())

books=[int(sys.stdin.readline()) for _ in range(n)]
#books.insert(0,0) 

#print(books)
'''
def sortBooks(books,count):         
     for i in range(n):
          if books[i]>books[i+1]:
               books.insert(0,books.pop(books.index(books[i+1]-1)))
               count+=1
               break
     sortBooks(books,count)
     return count

print(sortBooks(books,0))
'''
'''
#count=0
#while
for i in range(n):
     if books[i]<books[i-1]:
          #books.insert(0,books.pop(books.index(books[i+1]-1)))
          #count+=1
          #break
          print(books[i]-1)
          break;
else:
     print(0)
'''   



















