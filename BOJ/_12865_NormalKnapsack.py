n,k=map(int,input().split())

D=[[0]*(n+1) for _ in range(k+1)] # D[i][j]- 버틸 수 있는 무게가 i이고 j번째 물건까지 고려할 때 최대 가치

products=[(0,0)] # products[i]->i번째 물품임을 맞추기 위함

for _ in range(n):
     w,v=map(int,input().split())
     products.append((w,v))



for i in range(k+1): # 버틸 수 있는 무게
     for j in range(1,n+1): # 몇번째 물품까지 고려하는지
          w,v=products[j] # j번째 물품
          if i<w: # 버틸 수 있는 무게가 j번째 물품 무게보다 작을 때 -> j번째 물품을 안넣는 걸로
               D[i][j]=D[i][j-1] # 버틸 수 있는 무게가 i이고 j-1번째 무게까지만 고려하는 것
          else:
               D[i][j]=max(D[i-w][j-1]+v,D[i][j-1]) # j번째 물품을 넣는 경우, 안넣는 경우
          


print(D[k][n])
