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
        self.xcod=np.linspace(x1,x2,self.Nx)
    def set_ylim(self,y1,y2):
        self.Xa[1]=y1
        self.Xb[1]=y2
        self.ylim=np.array([y1,y2])
        self.ycod=np.linspace(y1,y2,self.Nx)
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
    fig=plt.figure()
    ax=fig.add_subplot(111)

    Nx=100
    Ny=100
    im=IMG(Nx,Ny)
    im.set_xlim(-3,3)
    im.set_ylim(-3,3)




    M=10
    R=2.0
    dth=2*np.pi/M
    for k in range(M):
        th=dth*k
        Y1=np.zeros(2)
        Y1[0]=R*np.cos(th)
        Y1[1]=R*np.sin(th)
        im.draw(Y1,Y1)
        ax.plot(Y1[0],Y1[1],"ko",markersize=6,markerfacecolor="w")

    im.show(ax)
    #ax.set_ylim([-2,1.2])

    fig.savefig("psf.png",bbox_inches="tight")


    fig2=plt.figure()
    bx=fig2.add_subplot(111)
    N2=int(Nx/2)
    bx.plot(im.xcod,im.Amp[N2,:]/M,"b",label="M=10")
    bx.grid(True)

    im.clear()
    M=20
    R=2.0
    dth=2*np.pi/M
    for k in range(M):
        th=dth*k
        Y1=np.zeros(2)
        Y1[0]=R*np.cos(th)
        Y1[1]=R*np.sin(th)
        im.draw(Y1,Y1)
        #ax.plot(Y1[0],Y1[1],"ko",markersize=6,markerfacecolor="w")

    #im.show(ax)
    bx.plot(im.xcod,im.Amp[N2,:]/M,"k--",label="M=20")
    bx.grid(True)
    fsz=14
    bx.set_xlabel("x",fontsize=fsz)
    bx.set_ylabel("I(x)",fontsize=fsz)
    ax.tick_params(labelsize=fsz-2)
    bx.tick_params(labelsize=fsz-2)
    bx.legend()


    fig2.savefig("psf_profile.png",bbox_inches="tight")

    plt.show()
