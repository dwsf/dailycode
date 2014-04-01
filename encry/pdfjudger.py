#coding:utf-8
#author:zsc347

import os
from judger import Judger

class PdfJudger(Judger):
    def __init__(self,filepath):
        Judger.__init__(self, filepath)
        self._keyword=r"/Encrypt"
        
    def is_encryped(self):
        '''
        judge a pdf file to find if it is encryped
        '''
        fbuffer=""
        f=self.ifs
        BUFFSIZE=40960#each time read 1024 bytes
        keyword_size=len(self._keyword)
        f.seek(0,os.SEEK_END)#start from the end of the file
        file_size=f.tell()
        while file_size>BUFFSIZE:
            f.seek(-BUFFSIZE,os.SEEK_CUR)
            file_size-=BUFFSIZE
            tag=f.tell()
            fbuffer=f.read(BUFFSIZE+keyword_size)
            f.seek(tag)
            if fbuffer.find(self._keyword)>=0:
                return True
        f.seek(0)
        fbuffer=f.read(BUFFSIZE+keyword_size)
        return True if fbuffer.find(self._keyword)>=0 else False
    
if __name__ == '__main__':
    path="etest.pdf"
    judger=PdfJudger(path)
    if judger.is_encryped():
        print "yes"
    else:
        print "no"
    pass