#coding:utf-8
#author:zsc347

import sys
import os
from judger import Judger
from office03judger import PptJudger,XlsJudger,DocJudger
from office07judger import XlsxJudger,DocxJudger,PptxJudger
from pdfjudger import PdfJudger


def is_encryped(filepath,filetype):
    judger=Judger(filepath)
    if filetype=='doc':
        judger=DocJudger(filepath)
    elif filetype=='docx':
        judger=DocxJudger(filepath)
    elif filetype=='ppt':
        judger=PptJudger(filepath)
    elif filetype=='pptx':
        judger=PptxJudger(filepath)
    elif filetype=='xls':
        judger=XlsJudger(filepath)
    elif filetype=='xlsx':
        judger=XlsxJudger(filepath)
    elif filetype=='pdf':
        judger=PdfJudger(filepath)

    return judger.is_encryped()
        
    

if __name__ == '__main__':
    filepath=None
    filetype=None
    
    def use_help():
        print"use:encryjudge filepath [-t filetype]"
        
    if len(sys.argv)<2:
        use_help()
    else:
        filepath=sys.argv[1]
        if len(sys.argv)==4 and sys.argv[2]=='-t':
            filetype=sys.argv[3]
        else:
            ext=os.path.splitext(filepath)[1]
            if ext!="":
                filetype=''.join(ext[1:None])
                
    if filetype is None:
        print "file format unknown,please use [-t filetype] to specify it!"
        exit(-1)
        
    result=is_encryped(filepath,filetype)
    if result:
        print "yes"
    else:
        print "no"