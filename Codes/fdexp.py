import matplotlib.pyplot as plt
import numpy as np


class DAT:
    def load(self,num):
        fp=open("order"+str(num)+".out","r");
        tmp=fp.readline()

        h=[]
        N=[]
        err=[]
        for row in fp:
            dat=row.strip().split(",")
            h.append(float(dat[0]))
            N.append(int(dat[1]))
            err.append(float(dat[3]))
        fp.close()

        self.h=np.array(h)
        self.N=np.array(N)
        self.err=np.array(err)
        self.num=num-1;
    
    def plot_err(self,ax):
        clrs=["b","r"]
        clr=clrs[self.num]
        ax.loglog(self.h,self.err,"-o"+clr,markersize=10)
        ax.grid(True)

if __name__=="__main__":
    D1=DAT()
    D2=DAT()

    D1.load(1)
    D2.load(2)

    fig=plt.figure()
    ax=fig.add_subplot(111)

    D1.plot_err(ax)
    D2.plot_err(ax)

    ax.tick_params(labelsize=12)

    plt.show()
    fig.savefig("err.png",bbox_inches="tight")
