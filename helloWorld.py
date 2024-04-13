

def check(mid,k,work:list)->bool:
    count=0
    s=0
    i=len(work)-1
    while i >=0:
        if (count+work[i])<=mid:
            count+=work[i]
            i-=1
            continue
        else:
            count=0
            count+=work[i]
            s+=1
            i-=1
            continue
    if s< k-1:
        return True
    return False
    
def main():
    left=0
    right=12
    ans=0
    t,k=map(int,input().split())
    work=[int(i) for i in input().split()]

    while left < right:
        mid=(left+right)//2
        if check(mid,k,work):
            right=mid
            ans=mid
        else:
            left=mid+1
    ans_list=[[0,0] for _ in range(k)]
    #员工代号
    count=k-1
    su=0
    a=0
    for i in range(t-1,-1,-1):
        a=i
        #员工没有分配完，同时每个员工的配额小于ans
        if count >=0 and (su+work[i])<=ans:
            #第一次分配的话，结束置此刻的任务代号,结果要＋1
            if su==0:
                ans_list[count][1]=i+1
            su+=work[i]
        #如果有一个配额即将大于，给下一个员工分配，
        elif (su+work[i])>ans:
            ans_list[count][0]=i+1+1
            count-=1
            su=0
            #如果上一个员工分不了，同时下一个也分不了，那么就是数据的问题.
            if (su+work[i])>ans:
                raise ValueError
            else:
                su+=work[i]
                ans_list[count][1]=i+1
    ans_list[count][0]=a+1
    for i in range(k):
        start, end = ans_list[i]
        print(f"{start} {end}")


    pass

    for i in range(0,4,-1):
        print(i)

if __name__ == '__main__':
    main();