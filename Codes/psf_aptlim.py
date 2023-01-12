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
    def clear(self):
        self.Amp=np.zeros([Ny,Nx])
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
        Amax=np.max(self.Amp[:])
        im=ax.imshow(self.Amp/Amax,extent=ext,origin="lower",cmap="gray",interpolation="none",vmin=0,vmax=0.8)
        ax.set_aspect(1.0)
        fsz=14
        #ax.set_xlabel("x",fontsize=fsz)
        #ax.set_ylabel("y",fontsize=fsz)
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
    fig=plt.figure(figsize=[8,8])
    plt.tight_layout()

    ax11=fig.add_subplot(221)
    ax12=fig.add_subplot(222)
    ax21=fig.add_subplot(223)
    ax22=fig.add_subplot(224)

    Nx=100
    Ny=100
    im=IMG(Nx,Ny)
    im.set_xlim(-3,3)
    im.set_ylim(-3,3)


    M=24
    R=2.0

    dth=15
    dth=dth/180*np.pi

    msz=4
    for k in range(M):
        th=dth*k
        Y1=np.zeros(2)
        Y1[0]=R*np.cos(th)
        Y1[1]=R*np.sin(th)
        im.draw(Y1,Y1)
        ax11.plot(Y1[0],Y1[1],"ko",markersize=msz,markerfacecolor="w")
    im.show(ax11)

    im.clear()
    M=12+1
    for k in range(M):
        th=dth*k
        Y1=np.zeros(2)
        Y1[0]=R*np.cos(th)
        Y1[1]=R*np.sin(th)
        im.draw(Y1,Y1)
        ax12.plot(Y1[0],Y1[1],"ko",markersize=msz,markerfacecolor="w")
    im.show(ax12)

    im.clear()
    M=8+1
    for k in range(M):
        th=dth*k
        Y1=np.zeros(2)
        Y1[0]=R*np.cos(th)
        Y1[1]=R*np.sin(th)
        im.draw(Y1,Y1)
        ax21.plot(Y1[0],Y1[1],"ko",markersize=msz,markerfacecolor="w")
    im.show(ax21)

    im.clear()
    M=4+1
    for k in range(M):
        th=dth*k
        Y1=np.zeros(2)
        Y1[0]=R*np.cos(th)
        Y1[1]=R*np.sin(th)
        im.draw(Y1,Y1)
        ax22.plot(Y1[0],Y1[1],"ko",markersize=msz,markerfacecolor="w")
    im.show(ax22)

    fig.savefig("psf_apllim.png",bbox_inches="tight")
    plt.show()
