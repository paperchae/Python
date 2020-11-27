# 10871
N,X = map(int,input().split())
a = list(map(int,input().split()))
b=list(0 for _ in range(N))
cnt=0
for num in a:
    if(num<X):
        b[cnt]=num
        cnt+=1
        
for i in range(cnt):
    print(b[i])