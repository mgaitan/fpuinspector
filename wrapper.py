from ctypes import cdll
import platform


class Wrapper:
    def __init__(self):
        # load the shared object
        if platform.system()=='Linux':
            self.lib = cdll.LoadLibrary('./libregistros.so.1.0')
        elif platform.system()=='Windows':
            self.lib = cdll.LoadLibrary('./libregistros.dll') #TODO
    
    def get_control(self):
        return self.lib.get_control()
    
    def get_estado(self):
        return self.lib.get_estado()
    
    def get_st0(self):
        return self.lib.get_st0()
        
    def reset(self):
        self.lib.reset()
    
    def finit(self,run=True):
        if run:
            self.lib.finit()    

    def ffree(self, n=0, run=True):
        if run:
            self.lib.ffree(n)
            
    def fld(self, n=0.0, run=True):
        if run:
            self.lib.fld(n)

    def fcom(self, n=0, run=True):
        if run:
            self.lib.fcom(n)

    def fxch(self, n=0, run=True):
        if run:
            self.lib.fxch(n)

    def faddp(self, n=1, run=True):
        if run:
            self.lib.faddp(n)
    
    def fsubp(self, n=1, run=True):
        if run:
            self.lib.fsubp(n)
    
    def fsincos(self, run=True):
        if run:
            self.lib.fsincos()

    def fyl2x(self, run=True):
        if run:
            self.lib.fyl2x()

    def fsqrt(self, run=True):
        if run:
            self.lib.fsqrt()

    #HELPER
    def is_valid(self,line):
        """checks line for a valid asm sentence"""
        line.replace(',',' ')
        commlista = line.split()
        comm = commlista[0]
        params = commlista[1:]
        
        paramline = "("
        i=0
        for p in params:
            if i>0:
                paramline+=", "
            paramline+=str(p)
            i+=1
        paramline += "run=False)"
        commline = "self."+comm + paramline
        
        print commline
        
        try:
            #run=False just check the call is right but do nothing
            exec commline 
            return True
        except:
            return False
