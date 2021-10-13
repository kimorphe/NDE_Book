import numpy as np
import matplotlib.pyplot as plt


class DATA:
    def load(self,fname):
        fp=open(fname,"r")
        fp.readline()

        tt=[]   # time
        u_fd=[] # FD
        u_tr=[] # exact
        for row in fp:
            dat=row.strip().split(",")
            tt.append(float(dat[0]))
            u_fd.append(float(dat[1]))
            u_tr.append(float(dat[2]))

        self.tt=np.array(tt)
        self.u_fd=np.array(u_fd)
        self.u_tr=np.array(u_tr)
    def plot(self,ax,exact=False,clr=""):
        ax.plot(self.tt,self.u_fd,"-"+clr)
        if exact:
            ax.plot(self.tt,self.u_tr,"k-")
        ax.grid(True)

        

if __name__=="__main__":

    fig=plt.figure(figsize=[10,5])
    ax=fig.add_subplot(111)

    dat1=DATA()
    dat2=DATA()
    dat3=DATA()

    dat1.load("sdof50.out")
    dat2.load("sdof100.out")
    dat3.load("sdof200.out")

    dat3.plot(ax,exact=True,clr="g")
    dat2.plot(ax,clr="r")
    dat1.plot(ax,clr="b")

    ax.tick_params(labelsize=14)

    plt.show()
    fig.savefig("sdof.png",bbox_inches="tight")
