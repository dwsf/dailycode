#coding:utf-8
#author:zsc347

from struct import unpack
from judger import Judger,error,ERROR 


class CFBHandler:
    def __init__(self,ifs):  # @ReservedAssignment
        self.ifs=ifs
        self.headinfo=self._get_head_info()
        self.satids=self._get_msat_sector_sids()
        self.sids=self._get_sat_sids()
        self._fsssid=0#first short stream sector id
        self._sssz=0#short stream size
        self.ssids=self._get_ssat_ssids()
        self.dirs=self._get_dirs()
    
    def _get_head_info(self):
        '''
        '''        
        #ssz:sector size
        #sssz:short sector size
        #nsats:the total of sat sectors
        #fdsid:the first directory sector sid
        #stsz:the minimum size of the standard streams
        #fssatsid:first short sat sector sid
        #nssats: the total of ssat sectors
        #fmsatsid:first msat sector sid
        #nmsats:the total msat sectors
        info={}
        f=self.ifs
        f.seek(30)
        t1,t2=unpack('2h',f.read(4))
        info['ssz']=2**t1
        info['sssz']=2**t2
        f.seek(44)
        tmp=unpack('8i',f.read(32))
        info['nsats']=tmp[0]
        info['fdsid']=tmp[1]
        info['stsz']=tmp[3]
        info['fssatsid']=tmp[4]
        info['nssats']=tmp[5]
        info['fmsatsid']=tmp[6]
        info['nmsats']=tmp[7]
        return info

    def sector_offset(self,sid,offset=0):
        while offset>self.headinfo['ssz']:
            sid=self.sids[sid]
            offset-=self.headinfo['ssz']
        off=512+sid*self.headinfo['ssz']
        return off+offset
    
    def ssector_offset(self,ssid,offset=0):
        while offset>self.headinfo['sssz']:
            ssid=self.satids[ssid]
            offset-=self.headinfo['sssz']
        
        if ssid>self._sssz/self.headinfo['sssz']:
            return -1#访问违规
        
        sid=self._fsssid#form root entry
        sec_sst_num=self.headinfo['ssz']/self.headinfo['sssz']
        sec_nth=int(ssid/sec_sst_num)
        
        while sec_nth>1:
            sid=self.sids[sid]
            sec_nth-=1
            
        offsid=self.sector_offset(sid)
        offssid=(ssid%sec_sst_num)*self.headinfo['sssz']
        return offsid+offssid+offset
    
    def _get_msat_sector_sids(self):
        info=self.headinfo
        f=self.ifs
        sids=[]
        f.seek(76)
        tmp=unpack('109i',f.read(4*109))
        for x in tmp:
            if x!=-1:
                sids.append(x)
            else:
                break
        nmstats=info['nmsats']
        if nmstats!=0:
            secnum=info['ssz']/4
            sid=info['fmstatsid']
            while nmstats>0:
                off=self.sector_offset(sid)
                f.seek(off)
                tmp=unpack(str(secnum)+'i',f.read(info['ssz']))
                nmstats-=(secnum-1)
                for x in tmp[0:-1]:
                    if x!=-2:
                        sids.append(x)
                    else:
                        break
                if nmstats>0:
                    sid=tmp[-1]
        return sids
    
    def _get_sat_sids(self):
        f=self.ifs
        info=self.headinfo
        sids=[]
        snum=info['ssz']/4
        for msid in self.satids:
            f.seek(self.sector_offset(msid))
            tmp=unpack(str(snum)+'i',f.read(info['ssz']))
            sids+=tmp
        return sids      
    
    def _get_ssat_ssids(self):
        f=self.ifs
        info=self.headinfo
        sids=self.sids
        ssids=[]
        nssats=info['nssats']
        if nssats==0:
            return ssids
        else:
            ssatid=info['fssatsid']
            snum=info['ssz']/4
            while ssatid!=-2:
                f.seek(self.sector_offset(ssatid))
                tmp=unpack(str(snum)+'i',f.read(info['ssz']))
                ssids+=tmp
                ssatid=sids[ssatid]      
        return ssids    
    
    def _get_dir_info(self,diroff):
        #fsid:the first sector sid,if the stream is short then it is the ssid
        f=self.ifs
        dirinfo={}
        f.seek(diroff+64)
        namesz=unpack('h',f.read(2))[0]-2
        f.seek(diroff)
        dirinfo['name']=f.read(namesz).decode('utf16')
        f.seek(diroff+66)
        dirinfo['type']=unpack('b',f.read(1))[0]
        #0:empty 1:user storage 2:user stream 3:lockbytes 4:property 5:root storage
        dirinfo['color']=unpack('b',f.read(1))[0]
        #0:red 1:black
        dirinfo['ldid'],dirinfo['rdid'],dirinfo['rtdid']=unpack('3i',f.read(12))
        #ldid:left rdid:right rtdid:root did
        f.seek(diroff+116)
        tmp=unpack('2i',f.read(8))
        if dirinfo['type']==5:
            self._fsssid,self._sssz=tmp
        elif dirinfo['type']==2:
            dirinfo['stmsz']=tmp[1]
            if tmp[1]<self.headinfo['stsz']:
                dirinfo['fsid'],dirinfo['fssid']=None,tmp[0]
            else:
                dirinfo['fsid'],dirinfo['fssid']=tmp[0],None
            dirinfo['stmsz']=tmp[1]
        else:
            pass   
        return dirinfo
        
    def _get_dirs(self):
        info=self.headinfo
        sid=info['fdsid']
        secids=[]
        dirs=[]
        while sid!=-2:
            secids.append(sid)
            sid=self.sids[sid]
        
        did=0
        for secid in secids:
            for i in range(info['ssz']/128):
                dirinfo=self._get_dir_info(self.sector_offset(secid)+i*128)
                dirinfo['did']=did
                did+=1
                if dirinfo['type']!=0:#not empty
                    dirs.append(dirinfo)   
        
        return dirs
    
class DocJudger(Judger):
    def __init__(self,filepath):  # @ReservedAssignment
        Judger.__init__(self, filepath)
        self.handle=CFBHandler(self.ifs)
    
    #注意这里都是判断是否用密码加密
    def is_encryped(self):
        f=self.ifs
        handle=self.handle
        dirs=handle.dirs
        flag=False
        for d in dirs:
            if d['type']==2 and d['name']=="WordDocument":
                flag=True
                fsid=d['fsid']
                fssid=d['fssid']
        if not flag:
            error(ERROR.FORMATERROR)
            
        if fsid is not None:
            offset=handle.sector_offset(fsid)
        elif fssid is not None:
            offset=handle.ssector_offset(fssid)
        else:
            error(ERROR.FORMATERROR)
            
        f.seek(offset+11)
        tmp=unpack('b',f.read(1))[0]
        if tmp%2==1 and int(tmp/64)==1:
            #F位和M位都为1,python不太好处理二进制数据故化成整数处理
            return True
        else:
            return False
        

class PptJudger(Judger):
    def __init__(self,filepath):  # @ReservedAssignment
        Judger.__init__(self, filepath)
        self.handle=CFBHandler(self.ifs)
        
    def is_encryped(self):
        #定位Current User流,获得offsetToCurrentEdit的值
        f=self.ifs
        handle=self.handle
        dirs=handle.dirs
        flag=False
        offset=0
        for d in dirs:
            if d['type']==2 and d['name']=="Current User":
                flag=True
                fsid=d['fsid']
                fssid=d['fssid']
                break
        if not flag:
            error(ERROR.FORMATERROR)
            
        if fsid is not None:
            offset=handle.sector_offset(fsid)
        elif fssid is not None:
            offset=handle.ssector_offset(fssid)
        else:
            error(ERROR.FORMATERROR)
            
        f.seek(offset+16)
        offsetToCurrentEdit=unpack('i',f.read(4))[0]
        #定位PowerPoint Document流,根据offset to currenteidt的值定位到UserEditAtom的位置
        for d in dirs:
            if d['type']==2 and d['name']=="PowerPoint Document":
                flag=True
                fsid=d['fsid']
                fssid=d['fssid']
                break
        if not flag:
            error(ERROR.FORMATERROR)
        
        if fsid is not None:
            offset=handle.sector_offset(fsid,offsetToCurrentEdit)
        elif fssid is not None:
            offset=handle.ssector_offset(fssid,offsetToCurrentEdit)
        else:
            error(ERROR.FORMATERROR)

        f.seek(offset+4)
        reclen=unpack('i',f.read(4))[0]
        if reclen==32:
            return True
        elif reclen==28:
            return False
        else:
            error(ERROR.FORMATERROR)
        
class XlsJudger(Judger):
    def __init__(self,filepath):  # @ReservedAssignment
        Judger.__init__(self, filepath)
        self.handle=CFBHandler(self.ifs)
        
    def is_encryped(self):
        f=self.ifs
        handle=self.handle
        dirs=handle.dirs
        flag=False
        for d in dirs:
            if d['type']==2 and d['name']=="Workbook":
                flag=True
                fsid=d['fsid']
                fssid=d['fssid']
        if not flag:
            error(ERROR.FORMATERROR)
            
        if fsid is not None:
            offset=handle.sector_offset(fsid)
        elif fssid is not None:
            offset=handle.ssector_offset(fssid)
        else:
            error(ERROR.FORMATERROR)
        
        f.seek(offset)
        while True:
            flag=unpack('i',f.read(4))[0]
            if flag==329216:#\x00\x06\x05\x00
                break#find the start of workbook content
            
        off=f.tell()+12#pass the BOF
        
        f.seek(off)
        rtype,size=unpack('2h',f.read(4))  # @UnusedVariable
        #如果第一个和第二个都不是filepass 说明filepass不存在
        #[WriteProtect--4B] [FilePass --size][...][....]
        if rtype==47:#filepass 标记为47
            return True
        rtype,size=unpack('2h',f.read(4))  # @UnusedVariable
        if rtype==47:
            return True
        else:
            return False

if __name__ == '__main__':
    def testdoc():
        path="etest.doc"
        judger=DocJudger(path)
        flag=judger.is_encryped()
        if flag:
            print "yes"
        else:
            print "no"
            
    def testppt():
        path="etest.ppt"
        judger=PptJudger(path)
        flag=judger.is_encryped()
        if flag:
            print "yes"
        else:
            print "no"
    
    def testxls():
        #path="etest.xls"
        path="test.xls"
        judger=XlsJudger(path)
        flag=judger.is_encryped()
        if flag:
            print "yes"
        else:
            print "no"
                
    def testhandle():
        f=open("etest.doc",'rb')     
        judger=CFBHandler(f)
        print judger.headinfo
        print judger.sids 
        print judger.ssids
        print judger.dirs
        
    testdoc()
    testxls()
    testppt()
        
    pass






