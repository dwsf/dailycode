#coding:utf-8
#author:zsc347
#create on Mar 29,2014

from random import randint

cells=[[0,0,0,0] for x in range(4)]
MOVE=['left','up','right','down']

def availableCells():
    ava=[]
    for i,jlist in enumerate(cells):
        for j,value in enumerate(jlist):
            if value==0:
                ava.append((i,j))
    return ava

def addRandomTile():
    x=2 if randint(1,10)<=9 else 4
    ava=availableCells()
    pos=ava[randint(0,len(ava)-1)]
    cells[pos[0]][pos[1]]=x

def move(direction):
    global cells
    def merge(x):
        if x[0]==x[1]:
            if x[2]==x[3]:
                x=[2*x[0],2*x[2],0,0]
            else:
                x=[2*x[0],x[2],x[3],0]
        else:
            if x[1]==x[2]:
                x=[x[0],2*x[1],x[3],0]
            elif x[2]==x[3]:
                x=[x[0],x[1],2*x[2],0]
            return x
    if direction==0:#left
        cells=[merge(x) for x in cells]
    elif direction==1:#up
        cells[0,0],cells[1,0],cells[2,0],cells[3,0]=merge([cells[0,0],cells[1,0],cells[2,0],cells[3,0]])
        cells[0,1],cells[1,1],cells[2,1],cells[3,1]=merge([cells[0,1],cells[1,1],cells[2,1],cells[3,1]])
        cells[0,2],cells[1,2],cells[2,2],cells[3,2]=merge([cells[0,2],cells[1,2],cells[2,2],cells[3,2]])
        cells[0,3],cells[1,3],cells[2,3],cells[3,3]=merge([cells[0,3],cells[1,3],cells[2,3],cells[3,3]])
    elif direction==2:#right
        cells[0,3],cells[0,2],cells[0,1],cells[0,0]=merge([cells[0,3],cells[0,2],cells[0,1],cells[0,0]])
        cells[1,3],cells[1,2],cells[1,1],cells[1,0]=merge([cells[1,3],cells[1,2],cells[1,1],cells[1,0]])
        cells[2,3],cells[2,2],cells[2,1],cells[2,0]=merge([cells[2,3],cells[2,2],cells[2,1],cells[2,0]])
        cells[3,3],cells[3,2],cells[3,1],cells[3,0]=merge([cells[3,3],cells[3,2],cells[3,1],cells[3,0]])
    elif direction==3:#down
        cells[3,0],cells[2,0],cells[1,0],cells[0,0]=merge([cells[3,0],cells[2,0],cells[1,0],cells[0,0]])
        cells[3,1],cells[2,1],cells[1,1],cells[0,1]=merge([cells[3,1],cells[2,1],cells[1,1],cells[0,1]])
        cells[3,2],cells[2,2],cells[1,2],cells[0,2]=merge([cells[3,2],cells[2,2],cells[1,2],cells[0,2]])
        cells[3,3],cells[2,3],cells[1,3],cells[0,3]=merge([cells[3,3],cells[2,3],cells[1,3],cells[0,3]])
        
    addRandomTile()

def setup():
    addRandomTile()
    addRandomTile()

def play():
    setup()
    print("start game:")
    dt={'a':0,'w':1,'d':2,'s':3}
    while True:
        for l in cells:
            for x in l:
                print(x,end='\t')
            print()
        x=input("derection:")
        d=dt[x]
        move(d)
        
        
if __name__ == '__main__':
    play()
    pass