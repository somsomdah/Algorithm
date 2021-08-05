def find_number(list,p,q,k):
     if p<q :
          temp_idx=(p+q)//2
          temp_val=list[temp_idx]

          if temp_val==k :
               return 1
          elif k < temp_val :
               return find_number(list,p,temp_idx,k)
          else : # if temp_val < k
               return find_number(list,temp_idx+1,q,k)
     else:
          return 0

if __name__=="__main__":
     n=int(input())
     card_list=list(map(int,input().split()))
     m=int(input());
     given_list=list(map(int,input().split()))

     card_list.sort()
     result_string=""

     for num in given_list:
          result=find_number(card_list,0,n,num)
          result_string+=str(result)+" "

     print(result_string)
