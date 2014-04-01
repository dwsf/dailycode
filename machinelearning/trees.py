#coding:utf8
#user:zsc347
#create on Dec 24

from math import log
import operator

def clacShannonEnt(dataset):
    numEntries=len(dataset)
    labelCounts={}
    for featVec in dataset:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)
    return shannonEnt 

def splitDataSet(dataSet,axis,value):
    recDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedVec=featVec[:axis]
            reducedVec.extend(featVec[axis+1:])
            recDataSet.append(reducedVec)
    return recDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
    baseEntropy=clacShannonEnt(dataSet)
    bestInfoGain=0.0;bestFeature=-1
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)
        newEntropy=0.0
        for value in uniqueVals:
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*clacShannonEnt(subDataSet)
        infoGain=baseEntropy-newEntropy
        if infoGain>bestInfoGain:
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount=sorted(classCount.iteritems(),operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createTree(dataset,labels):
    def recurCreateTree(dataset,labels):
        classList=[example[-1] for example in dataset]
        if classList.count(classList[0])==len(classList):
            return classList[0]
        if len(dataset[0])==1:
            return majorityCnt(classList[0])
        bestFeat=chooseBestFeatureToSplit(dataset)
        bestFeatLabel=labels[bestFeat]
        mytree={bestFeatLabel:{}}
        del(labels[bestFeat])
        featValues=[example[bestFeat] for example in dataset]
        uniqueVals=set(featValues)
        for value in uniqueVals:
            subLabels=labels[:]
            mytree[bestFeatLabel][value]=recurCreateTree(splitDataSet(dataset,bestFeat,value),subLabels)
        return mytree
    tmpLabels=labels[:]
    return recurCreateTree(dataset,tmpLabels)

def classify(inputTree,featLabels,testVec):
    firstStr=inputTree.keys()[0]
    secondDict=inputTree[firstStr]
    featIndex=featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex]==key:
            if type(secondDict[key]).__name__=='dict':
                classLabel=classify(secondDict[key],featLabels,testVec)
            else:
                classLabel=secondDict[key]
    return classLabel

def storeTree(inputTree,filename):
    import pickle
    fw=open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr=open(filename,'r')
    return pickle.load(fr)
    
######test#####
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    return dataSet, labels


if __name__ == '__main__':
    pass