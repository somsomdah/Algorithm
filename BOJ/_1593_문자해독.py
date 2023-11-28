g, s = map(int, input().split())

W = input()
S = input()

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
abc_dict = {}

for a in abc:
    abc_dict[a] = 0
    abc_dict[a.lower()] = 0

tmp_dict = abc_dict.copy()
for w in W:
    abc_dict[w] += 1

        

l, r = 0, g-1

for i in range(l, r+1):
    ch = S[i]
    tmp_dict[ch] += 1
    
cnt = 0
while r <= s:
    
            for i in range(l, r+1):
                ch = S[i]
                if tmp_dict[ch] != abc_dict[ch]:
                    break
            else:
                cnt += 1
                
            if r + 1 == s:
                break
            
            tmp_dict[S[l]]  -= 1
            tmp_dict[S[r+1]] += 1
            l += 1
            r += 1


            
print(cnt)
                

    
