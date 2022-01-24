import numpy as np
import matplotlib.pyplot as plt


class IMG:
    def __init__(self,Nx,Ny):
        self.Nx=Nx
        self.Ny=Ny
        self.Xa=np.zeros(2)
        self.Xb=np.zeros(2)
        self.Amp=np.zeros([Ny,Nx])
        self.Nx=Nx
        self.Ny=Ny

    def set_xlim(self,x1,x2):
        self.Xa[0]=x1
        self.Xb[0]=x2
        self.xlim=np.array([x1,x2])
    def set_ylim(self,y1,y2):
        self.Xa[1]=y1
        self.Xb[1]=y2
        self.ylim=np.array([y1,y2])
    def show(self,ax):
        ext=[self.xlim[0],self.xlim[1],self.ylim[0],self.ylim[1]]
        im=ax.imshow(self.Amp,extent=ext,origin="lower",cmap="jet",interpolation="none")
        ax.set_aspect(1.0)
        fsz=14
        ax.set_xlabel("x",fontsize=fsz)
        ax.set_ylabel("y",fontsize=fsz)
        ax.tick_params(labelsize=fsz)
        ax.grid(True)

        return(im)
    def draw(self,Y1,Y2,sig=0.1):
        x1=self.xlim[0]
        x2=self.xlim[1]
        xcod=np.linspace(x1,x2,self.Nx)

        y1=self.ylim[0]
        y2=self.ylim[1]
        ycod=np.linspace(y1,y2,self.Ny)
        [X,Y]=np.meshgrid(xcod,ycod)
        
        rx=X-Y1[0]
        ry=Y-Y1[1]
        ri=np.sqrt(rx*rx+ry*ry)

        rx=X-Y2[0]
        ry=Y-Y2[1]
        rj=np.sqrt(rx*rx+ry*ry)

        rij=ri+rj
        
        R1=np.linalg.norm(Y1) 
        R2=np.linalg.norm(Y2) 
        Rf=R1+R2
        arg=Rf-rij;
        arg*=arg;
        self.Amp+=np.exp(-arg/sig*0.5)

if __name__=="__main__":
    fig1=plt.figure()
    ax=fig1.add_subplot(111)

    Nx=120
    Ny=60
    im=IMG(Nx,Ny)
    im.set_xlim(-3,3)
    im.set_ylim(-1,2)

    Y1=np.array([-1,2])
    Y2=np.array([ 1,2])


    im.draw(Y1,Y1)
    im.draw(Y2,Y2)
    im.draw(Y1,Y2)
    im.show(ax)
    ax.plot(Y1[0],Y1[1],"ko",markersize=12,markerfacecolor="w")
    ax.plot(Y2[0],Y2[1],"ko",markersize=12,markerfacecolor="w")
    ax.set_ylim([-1,2.2])

    fig2=plt.figure()
    ax2=fig2.add_subplot(111)

    im.draw(Y1,Y2)
    im.show(ax2)
    ax2.plot(Y1[0],Y1[1],"ko",markersize=12,markerfacecolor="w")
    ax2.plot(Y2[0],Y2[1],"ko",markersize=12,markerfacecolor="w")
    ax2.set_ylim([-1,2.2])

    fig1.savefig("img_w12_1.png",bbox_inches="tight")
    fig2.savefig("img_w12_2.png",bbox_inches="tight")
    plt.show()
