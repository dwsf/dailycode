#coding:utf-8
#author:zsc347

class ERROR:
    FORMATERROR = -1
    ACCESSERROR = -2
    NOTCOMPLETE = -3

def error(err_type):
    if err_type==ERROR.FORMATERROR:
        print "file format error"
    elif err_type==ERROR.ACCESSERROR:
        print "can't access file"
    elif err_type==ERROR.NOTCOMPLETE:
        print "function <Judger.is_encrypted> is not complete,please realize it first!"
    else:
        print "unknown error"
    exit(-1)

class Judger():
    def __init__(self,filepath):
        try:
            f=open(filepath,'rb')
        except:
            error(ERROR.ACCESSERROR)
        self.ifs=f
    
    def is_encryped(self):
        error(ERROR.NOTCOMPLETE)
        
    def __del__(self):
        try:
            self.ifs.close()
        except:
            pass
    

if __name__ == '__main__':
    #error(ERROR.NOTCOMPLETE)
    Judger("aa")
    pass