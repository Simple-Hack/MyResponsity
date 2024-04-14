
class SegmentTree(object):
    def __init__(self):
        self.left = 0
        self.right = 0
        self.summa = 0



def pushup(x:int):
    MyTree[x].summa=MyTree[x*2].summa+MyTree[x*2+1].summa

def build(x:int,left:int,right:int):
    #left和right代表区间左右边界
    MyTree[x].left=left
    MyTree[x].right=right
    if left == right:
        MyTree[x].summa=a[left]
        return
    mid=(left+right)//2
    build(x*2,left,mid)
    build(x*2+1,mid+1,right)
    pushup(x)

def query(x:int,l:int,r:int)->int:
    if MyTree[x].left>=l and MyTree[x].right<=r:
        return MyTree[x].summa
    mid=(MyTree[x].left+MyTree[x].right)//2
    summ=0
    if l <= mid:
        summ+=query(x*2,l,r)
    if r>mid:
        summ+=query(x*2+1,l,r)
    return summ

def change(now:int,the_index_of_change:int,the_new_number_of_index:int):
    if MyTree[now].left==MyTree[now].right:
        MyTree[now].summa+=the_new_number_of_index
        return

    else:
        mid=(MyTree[now].left+MyTree[now].right)//2
        if the_index_of_change<=mid:
            change(now*2,the_index_of_change,the_new_number_of_index)
        else:
            change(now*2+1,the_index_of_change,the_new_number_of_index)
        pushup(now)


n,m=map(int,input().split())
MyTree=[SegmentTree() for _ in range(4*n+100)]
a=[0]+[int(i) for i in input().split()]
build(1,1,n)
lis=[]
for _ in range(m):
    q,l,r=map(int,input().split())
    if q==1:
        change(1,l,r)
    else:
        lis.append(query(1,l,r))

for i in range(len(lis)):
    print(lis[i])
        

