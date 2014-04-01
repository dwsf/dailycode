#coding:utf-8
#Created on Oct 21, 2013
#author: zsc347

import random
from timeit import Timer


A=[]
LINK=[]

def ini(num):
    global A,LINK
    A=[0]
    LINK=[0]
    for i in range(num):  # @UnusedVariable
        A.append(random.randint(1,num*100))
        LINK.append(0)

def show_LINK():
    B=[0]
    p=LINK[0]
    while p!=0:
        B.append(A[p])
        p=LINK[p]
    print(B)

#insert sort        
def Insort(low,high):
    global A,LINK
    q=LINK[0]=low
    for i in range(low+1,high+1):
        t=A[i]
        q=0
        while LINK[q]!=0:
            if A[LINK[q]]<=t:
                q=LINK[q]
            else:
                break
        LINK[i]=LINK[q]
        LINK[q]=i
    return LINK[0]

def mergeL(q,r):
    global A,LINK
    i=q
    j=r
    k=0
    while i !=0 and j!=0:
        if A[i]<=A[j]:
            LINK[k]=i
            k=i
            i=LINK[i]
        else:
            LINK[k]=j
            k=j
            j=LINK[j]
    if i==0:
        LINK[k]=j
    else:
        LINK[k]=i
    return LINK[0]

def MergeSortL(low,high):
    global A,LINK
    if (high-low+1)<16:
        LINK[0]=Insort(low,high)
    else:
        mid=(low+high)//2
        q=MergeSortL(low,mid)
        r=MergeSortL(mid+1,high)
        LINK[0]=mergeL(q,r)
    return LINK[0]

#quick sort

def partition(p,r):
    global A,LINK
    pivot=A[r]
    j=p-1
    for i in range(p,r):
        if A[i]<=pivot:
            j+=1
            A[j],A[i]=A[i],A[j]
    A[j+1],A[r]=A[r],A[j+1]
    return j+1

def QuickSort(low,high):
    if low<high:
        p=partition(low,high)
        QuickSort(low,p-1)
        QuickSort(p+1,high)
        

if __name__ == '__main__':
    
    #sort:排序方法；size：测试量大小，num:每次测试的重复次数取时间总和，repeat：实验的重复次数
    def exe_time(sort,size,num,repeat):
        result=[]
        while repeat>0:
            s=0
            n=num
            repeat-=1
            if sort=="meargesortl":
                while n>0:
                    n-=1
                    ini(size)
                    t=Timer("MergeSortL(1,len(A)-1)","from __main__ import MergeSortL,A,LINK")
                    s+=t.timeit(1)

            elif sort=="quicksort":
                while n>0:
                    n-=1
                    ini(size)
                    t=Timer("QuickSort(1,len(A)-1)","from __main__ import QuickSort,A,LINK")
                    s+=t.timeit(1)
            
            result.append(s)
        print(result)
        
    ini(20)
    MergeSortL(1,len(A)-1)
    print(A)
    print(LINK)
    show_LINK()
    QuickSort(1,len(A)-1)
    print(A)
            