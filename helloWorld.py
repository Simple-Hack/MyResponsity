

def check(mid,k:int ,work:list)->bool:
    mid_staff_number=0
    real_staff_number=k
    #工作时间的遍历
    i=len(work)-1
    work_time_count=0

    while i >=0:
        if (work_time_count+work[i]) <= mid:
            if work_time_count==0:
                mid_staff_number+=1
            work_time_count+=work[i]
            i-=1
        else:
            if work_time_count==0:
                return False
            work_time_count=0
    if mid_staff_number <= k:
        return True
    return False
    
def main():
    left=0
    right=17
    ans=0
    t,k=map(int,input().split())
    work=[int(i) for i in input().split()]

    while left < right:
        mid=(left+right) // 2
        if check(mid,k,work):
            right=mid
            ans=mid
        else:
            left=mid+1

    ans_list=[[0,0] for _ in range(k)]
    #员工代号
    worker_id=k-1
    sum_work_time=0

    for i in range(t-1,-1,-1):
        #第一个任务必须特殊处理
        if i ==0:
            if (sum_work_time+work[i])<=ans:
                if sum_work_time==0:
                    ans_list[worker_id][0]=i+1
                    ans_list[worker_id][1]=i+1
                else:
                    ans_list[worker_id][0]=i+1
        #不是第一个的   话正常相加即可
        if (sum_work_time+work[i])<= ans:
            if sum_work_time==0:
                ans_list[worker_id][1]=i+1
            sum_work_time+=work[i]
            if sum_work_time==ans:
                ans_list[worker_id][0]=i+1
                worker_id-=1
                sum_work_time=0
                continue
        else:
            sum_work_time=0
            sum_work_time+=work[i]
            ans_list[worker_id][0]=i+1+1
            worker_id-=1
            ans_list[worker_id][1]=i+1


    for i in range(k):
        start, end = ans_list[i]
        print(f"{start} {end}")

    pass


if __name__ == '__main__':
    main();