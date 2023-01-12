import numpy as np
import matplotlib.pyplot as plt

class Ellip:
    def setup(self,Y1,Y2):
        R1=np.linalg.norm(Y1)
        R2=np.linalg.norm(Y2)
        R=R1+R2
        a=R*0.5;
        Y12=Y2-Y1
        self.Y0=(Y1+Y2)*0.5 # center
        e=np.linalg.norm(Y12)*0.5
        b=np.sqrt(a*a-e*e)
        self.a=a
        self.b=b
    def draw(self,ax):
        Nth=100
        th1=0
        th2=-180
        th=np.linspace(th1,th2,Nth)
        th=th/180.*np.pi
        
        x3=self.a*np.cos(th)+self.Y0[0]
        y3=self.b*np.sin(th)+self.Y0[1]
        ax.plot(x3,y3,"-k")


if __name__=="__main__":

    #------------------------------

    # Distant layout
    Y1=np.array([-1,1])
    Y2=np.array([2,1])
    fnout="Gmmij_far.png"

    # Close layout
    Y1=np.array([1,1])
    Y2=np.array([2,1])
    fnout="Gmmij_near.png"

    #------------------------------

    el1=Ellip()
    el2=Ellip()
    el3=Ellip()

    el1.setup(Y1,Y1)
    el2.setup(Y2,Y2)
    el3.setup(Y1,Y2)

    fig=plt.figure()
    ax=fig.add_subplot(111)
    el1.draw(ax)
    el2.draw(ax)
    el3.draw(ax)
    ax.grid(True)

    ax.set_xlim([-3,5])
    ax.set_ylim([-2,1.2])
    fsz=14
    ax.tick_params(labelsize=fsz)
    #ax.set_xlabel("x",fontsize=fsz)
    #ax.set_ylabel("y",fontsize=fsz)
    ax.set_aspect(1.0)
    msz=8
    ax.plot(Y1[0],Y1[1],"ok",markersize=msz,markerfacecolor="w")
    ax.plot(Y2[0],Y2[1],"ok",markersize=msz,markerfacecolor="w")
    ax.plot(0,0,"ok",markersize=msz) #,markerfacecolor="w")
    fig.savefig(fnout,bbox_inches="tight")
    plt.show()

