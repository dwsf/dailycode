#coding:utf-8
#author:zsc347
#create on oct 27,2013

import heapq

def huffman(C):
    '''
    build huffman tree
    '''
    n=len(C)
    Q=[]
    for x in C:
        heapq.heappush(Q,[x[1],x[0],None,None])
        
    for i in range(1,n):
        x=heapq.heappop(Q)
        y=heapq.heappop(Q)
        heapq.heappush(Q,[x[0]+y[0],'A'+str(i),x,y])
        
    return heapq.heappop(Q)

def codes(hufftree):
    '''
    get huffman codes from the huffman tree
    '''
    codes={}
    def ltraver(node,prefix):
        if node[2]==None:#leaf node
            codes[node[1]]=prefix
        else:
            ltraver(node[2],prefix+'0')
            ltraver(node[3],prefix+'1')
    ltraver(hufftree,'')
    return codes

if __name__ == '__main__':
    def test(C):
        tree=huffman(C)
        print(tree)
        huffcode=codes(tree)
        print("huffman codes:")
        for x in C:
            print(x[0]+':'+huffcode[x[0]])
    
    C1=[('f',5),('e',9),('d',16),('c',12),('b',13),('a',45)]
    
    def f(n):#fibonacci
        return 1 if n==0 or n==1 else f(n-1)+f(n-2)
        
    C2=[('a',f(0)),('b',f(1)),('c',f(2)),('d',f(3)),('e',f(4)),('f',f(5)),('g',f(6)),('h',f(7)),('i',f(8)),('j',f(9)),('k',f(10))]

    test(C1)
    test(C2)