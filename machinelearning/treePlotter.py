#coding:utf8
#author:zsc347
#create on Dec 25

import matplotlib.pyplot as plt

decisionNode=dict(boxstyle='sawtooth',fc='0.8')
leafNode=dict(boxstyle='round4',fc='0.8')
arrowArgs=dict(arrowstyle='<-')

def createPlot(inTree):
    def plotNode(nodeTxt,centerPt,parentPt,nodeType):
        createPlot.ax1.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',
                                xytext=centerPt,textcoords='axes fraction',
                                va='center',ha='center',bbox=nodeType,arrowprops=arrowArgs)
        
    def plotMidText(cntrPt, parentPt, txtString):
        xMid = (parentPt[0]-cntrPt[0])/2.0 + 1.05*cntrPt[0]
        yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
        createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)
    
    def plotTree(myTree, parentPt, nodeTxt):#if the first key tells you what feat was split on
        numLeafs = getNumLeafs(myTree)  #this determines the x width of this tree
        #depth = getTreeDepth(myTree)
        firstStr = myTree.keys()[0]     #the text label for this node should be this
        cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
        plotMidText(cntrPt, parentPt, nodeTxt)
        plotNode(firstStr, cntrPt, parentPt, decisionNode)
        secondDict = myTree[firstStr]
        plotTree.yOff = plotTree.yOff - 0.7/plotTree.totalD
        for key in secondDict.keys():
            if type(secondDict[key]).__name__=='dict':#test to see if the nodes are dictonaires, if not they are leaf nodes   
                plotTree(secondDict[key],cntrPt,str(key))        #recursion
            else:   #it's a leaf node print the leaf node
                plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
                plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
                plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
        plotTree.yOff = plotTree.yOff + 0.7/plotTree.totalD
    
    fig=plt.figure(1,facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False,**axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;
    plotTree(inTree, (0.5,1.0), '')
    plt.show()
        
    

def getNumLeafs(mytree):
    numLeafs=0
    firstStr=mytree.keys()[0]
    secondDict=mytree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            numLeafs+=getNumLeafs(secondDict[key])
        else:
            numLeafs+=1
    return numLeafs
            
def getTreeDepth(mytree):
    maxDepth=0
    firstStr=mytree.keys()[0]
    secondDict=mytree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            thisDepth=1+getTreeDepth(secondDict[key])
        else:
            thisDepth=1
    if thisDepth>maxDepth: maxDepth=thisDepth
    return maxDepth     

###test####
def retrieveTree(i):
    listOfTrees =[{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                  ]
    return listOfTrees[i]





if __name__ == '__main__':
    pass