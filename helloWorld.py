a=[i for i in range(1,11)]

b=[0 for _ in range(6)]

for i in range(len(a)-1):
    for j in range(6):
        if (a[i]>>j) & 1:
            b[j]+=1

ans=0

for i in range(6):
    ans+=(len(a)-b[i])*b[i]*(1<<i)

print(ans)
