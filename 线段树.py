
class SegmentTree(object):

    def __init__(self):
        self.left = 0
        self.right = 0
        self.summa = 0

MyTree=[SegmentTree() for _ in range(114514)]
a=[0]*(4*114514)
def puthup(x:int):
    MyTree[x].summa=MyTree[x*2].summa+MyTree[x*2+1].summa

def build(x:int,left:int,right:int):
    #left和right代表区间左右边界
    MyTree[x].left=left
    MyTree[x].right=right
    if left & right==0:
        MyTree[x].summa=a[left]
        return
    mid=(left+right)//2
    build(x*2,left,mid)
    build(x*2+1,mid+1,right)
    MyTree[x].summa=MyTree[x*2].summa+MyTree[x*2+1].summa

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
        MyTree[now].summa=the_new_number_of_index
        return

    else:
        mid=(MyTree[now].left+MyTree[now].right)//2
        if the_index_of_change<=mid:
            change(now*2,the_index_of_change,the_new_number_of_index)
        else:
            change(now*2+1,the_index_of_change,the_new_number_of_index)
        MyTree[now].summa=MyTree[now*2].summa+MyTree[now*2+1].summa


        

