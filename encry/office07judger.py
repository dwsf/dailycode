#coding:utf-8
#author:zsc347

import os
from judger import Judger

class Office07Judger(Judger):
    def __init__(self,filepath):
        Judger.__init__(self, filepath)
        
    def is_encryped(self):
        keyword=r"<encryption xmlns"
        fbuffer=""
        keyword_size=len(keyword)
        f=self.ifs
        BUFFSIZE=1024#each time read 1024 bytes
        f.seek(0,os.SEEK_END)#start from the end of the file
        file_size=f.tell()
        f.seek(0)
        while file_size>0:
            tag=f.tell()
            fbuffer=f.read(BUFFSIZE+keyword_size)
            f.seek(tag+BUFFSIZE)
            if fbuffer.find(keyword)>=0:
                return True
            file_size-=BUFFSIZE
        return False

class DocxJudger(Judger):
    def __init__(self,filepath):
        self.judger=Office07Judger(filepath)
    
    def is_encryped(self):
        '''
        if the filetype is docx
        '''
        return self.judger.is_encryped()

class PptxJudger(Judger):
    def __init__(self,filepath):
        self.judger=Office07Judger(filepath)
    
    def is_encryped(self):
        return self.judger.is_encryped()

class XlsxJudger(Judger):
    def __init__(self,filepath):
        self.judger=Office07Judger(filepath)
    
    def is_encryped(self):
        return self.judger.is_encryped()    
    
    
if __name__ == '__main__':
    def test():
        path="etest.docx"
        judger=Office07Judger(path)
        if judger.is_encryped():
            print "yes"
        else:
            print "no"
            
    def testdocx():
        path="etest.docx"
        judger=DocxJudger(path)
        if judger.is_encryped():
            print "yes"
        else:
            print "no"
            
    def testpptx():
        path="etest.pptx"
        judger=DocxJudger(path)
        if judger.is_encryped():
            print "yes"
        else:
            print "no"
            
    def testxlsx():
        path="etest.xlsx"
        judger=DocxJudger(path)
        if judger.is_encryped():
            print "yes"
        else:
            print "no"
    
    testdocx()
    testxlsx()
    testpptx()
