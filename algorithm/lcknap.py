#coding:utf-8
#author:zsc347
#create on Nov 24
n=4
p=[10,10,12,18]
w=[2,4,6,8]

#cv:当前背包中物品的总价值
#cap:背包当前的剩余容量

def lubound(k,cap,cv):
    pvl=cv
    rw=cap
    pvu=None
    
    for i in  range(k+1,n+1):
        if rw<w[i]:
            pvu=pvl+rw*p[i]/w[i]
    
    
    pass
if __name__ == '__main__':
    pass